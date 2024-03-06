from django.shortcuts import render, redirect, get_object_or_404

import csv
from .models import VegPriceTrend, VegPrice, WeatherData, VegetablePriceByPref, ProduceAmount
from .forms import VegSelectionForm, MonthSelection, DateForm, GetPrefName, GetWeatherItem, DateSelection
from .imports import load_csv_data, load_predicted_csv, load_price_data_by_pref, load_weather_csv, load_share_csv
import os

import plotly.graph_objects as go   
from plotly.subplots import make_subplots
from .utils import CreateGraphs, WeatherGraph, GetWeatherInformation
import pandas as pd
from io import BytesIO
import base64
from datetime import date, timedelta, datetime
import numpy as np


# 予測した野菜のlist
vegetable_list = ["キャベツ", "レタス", "かぶ", "かんしょ", "きゅうり", "こまつな", "ごぼう", "ししとう", "しゅんぎく", "たまねぎ",
                  "だいこん", "ちんげんさい", "なす", "にら", "にんじん", "ねぎ", "はくさい", "ばれいしょ", "ほうれんそう", "みずな",
                  "やまのいも", "れんこん", "カリフラワー", "セルリー", "トマト", "ピーマン"] 

vegetable_image_path = {"キャベツ":"./static/images/kyabetsu.jpg", "レタス":"./static/images/retasu.jpg", "かぶ":"./static/images/kabu.jpg", 
                        "かんしょ":"./static/images/kansyo.jpg", "きゅうり":"./static/images/kyuuri.jpg", "こまつな":"./static/images/komatsuna.jpg",
                        "ごぼう":"./static/images/gobou.jpg", "ししとう":"./static/images/shishitou.jpg", "しゅんぎく":"./static/images/syungiku.jpg",
                        "たまねぎ":"./static/images/tamanegi.jpg", "だいこん":"./static/images/daikon.jpg", "ちんげんさい":"./static/images/chingensai.jpg",
                        "なす":"./static/images/nasu.jpg", "にら":"./static/images/nira.jpg", "にんじん":"./static/images/ninjin.jpg",
                        "ねぎ":"./static/images/negi.jpg", "はくさい":"./static/images/hakusai.jpg", "ばれいしょ":"./static/images/bareisyo.jpg",
                        "ほうれんそう":"./static/images/hourensou.jpg", "みずな":"./static/images/mizuna.jpg", "やまのいも":"./static/images/yamanoimo.jpg",
                        "れんこん":"./static/images/renkon.jpg", "カリフラワー":"./static/images/karifurawa.jpg", "セルリー":"./static/images/serori.jpg",
                        "トマト":"./static/images/tomato.jpg", "ピーマン":"./static/images/piman.jpg"}


# ローカルのデータをデータベースに格納する      
# load_csv_data()
# load_predicted_csv()
# load_weather_csv()
# load_price_data_by_pref()
# load_share_csv()

# dbから指定されたデータを取り出す
# some_viewsに指定された野菜のデータのみを抜き出し、グラフにするために、
# 指定された野菜のDataFrameを作成する
def get_veg_data_from_database(selected_veg):
    try:
        # 価格推移のデータ
        selected_veg_trend_data = VegPriceTrend.objects.filter(veg_name=selected_veg)
        selected_veg_trend_df = pd.DataFrame.from_records(selected_veg_trend_data.values())
        # 予測データ
        selected_veg_predict_data = VegPrice.objects.filter(veg_name=selected_veg)
        selected_veg_predict_df = pd.DataFrame.from_records(selected_veg_predict_data.values())
        
        # 2つのデータを格納する
        selected_veg_data  = pd.concat([selected_veg_trend_df, selected_veg_predict_df], axis=0)
        
        return selected_veg_data
    except VegPriceTrend.DoesNotExist:
        return None

def GetPredictedData():
    try:
        data = VegPrice.objects.all()
        df = pd.DataFrame.from_records(data.values())
        return df
    except VegPrice.DoesNotExist:
        return None
    
def GetWeatherDataFromDatabase(selected_pref):
    try:
        # 県名のみ指定（項目については、以下で平均値等出したいのでここでは限定しない）
        selected_data = WeatherData.objects.filter(pref_name=selected_pref)
        selected_df = pd.DataFrame.from_records(selected_data.values())
        return selected_df
    except WeatherData.DoesNotExist:
        return None
    
def GetPriceByPrefFromDatabase(pref_name, vegetable_name):
    try:
        selected_data = VegetablePriceByPref.objects.fillter(pref_name=pref_name, vegetable_name=vegetable_name)
        df = pd.DataFrame.from_records(selected_data.values())
        return df
    except VegetablePriceByPref.DoesNotExist:
        return None

def GetProduceAmountData(vegetable_name):
    try:
        selected_data = ProduceAmount.objects.filter(vegetable_name=vegetable_name)
        df = pd.DataFrame.from_records(selected_data.values())
        return df
    except ProduceAmount.DoesNotExist:
        return None
        
        
        
# 新しいfrontpageを作成する
def frontpage(request):
    if request.method == "GET":
        # 今日の予測値を全て記載する
        # 予測値の格納されたデータを読み込む
        df = GetPredictedData()
        # dfから今日の価格を野菜ごと取得する
        # 今日の日付を取得
        today_date = date.today()
        # 先週1週間のdatetimeを取得する
        last_week_start = today_date - timedelta(days=today_date.weekday()+7)
        last_week_end = last_week_start + timedelta(days=6)
        # dictに保存していく
        view_dict = {}
        for vegetable in vegetable_list:
            # 今日の予測値を取得するためのコード
            today_price = df[(df["veg_name"]==vegetable)&(df["veg_datetime"]==today_date)]["veg_price"]
            # 先週比を取得するためのコード
            specific_span_price = df[(df["veg_name"]==vegetable)&(df["veg_datetime"]>=last_week_start)&(df["veg_datetime"]<=last_week_end)]["veg_price"].mean()
            # 先週比を計算し、格納
            comparison_rate = np.round(today_price/specific_span_price*100, 2)
            
            image_path = vegetable_image_path.get(vegetable)
            
            if not today_price.empty and not np.isnan(specific_span_price):
                view_dict[vegetable] = {"today_price": today_price.values[0], "comparison_rate": comparison_rate.values[0], "image_path":image_path}
            elif today_price.empty and not np.isnan(specific_span_price):
                view_dict[vegetable] = {"today_price": "データがありません", "comparison_rate": comparison_rate.values[0], "image_path":image_path}
            elif not today_price.empty and np.isnan(specific_span_price.values[0]):
                view_dict[vegetable] = {"today_price": today_price, "comparison_rate": "データがありません", "image_path":image_path}
            else:
                view_dict[vegetable] = {"today_price": "データがありません", "comparison_rate": "データがありません", "image_path":image_path}

        
        return render(request, "veg_app/new_frontpage.html", {"view_dict":view_dict})
        

# URLパラメーターで指定された野菜IDを受け取り、野菜ごとの専門ページをレンダリング
def vegetable_detail(request, vegetable_name):
    if request.method == "GET":
        # 指定野菜の価格推移を取得する
        price_transit = get_veg_data_from_database(vegetable_name)
        first_date_of_this_month = datetime.now().replace(day=1).date()
        price_transit["actual_predict"] = price_transit["veg_datetime"].apply(lambda x: "actual" if x<first_date_of_this_month else "predict")
        # 指定野菜の出荷量のデータを取得
        share_data = GetProduceAmountData(vegetable_name=vegetable_name)
        # 予測データ
        df = GetPredictedData()
        df = df[df["veg_name"]==vegetable_name]
        
        
        # plotの初期化
        produce_plot = None
        price_plot = None
        weather_plot = None
        veg_name = vegetable_name
        veg_img = vegetable_image_path[veg_name]
        weather_data_dict = {}
        month_form = MonthSelection(request.GET)
        pref_form = GetPrefName(request.GET)
        weather_form = GetWeatherItem(request.GET)
        date_form = DateSelection(request.GET)
        
        
        # monthごとの生産量の棒グラフを制作するコード
        # 棒グラフの作成自体はutils.pyに記載
        # form = MonthSelection(request.POST)
        if month_form.is_valid():
            selected_month = int(month_form.cleaned_data["selected_month"])
            produce_plot = CreateGraphs.ProduceAmountPlot(share_data, selected_month)
        
        # 日時指定を行わないコード
        price_plot = CreateGraphs.PriceTransitPlot(price_transit)
        # 日時指定を行う場合のコード(現状ではうまく行ってません)
        # if date_form.is_valid():
        #     start_date = date_form.cleaned_data["start_date"]
        #     end_date = date_form.cleaned_data["end_date"]
        #     price_transit_tmp = price_transit[(price_transit["veg_datetime"]>=start_date)&(price_transit["veg_datetime"])<=end_date]
        #     price_plot = CreateGraphs.PriceTransitPlot(price_transit_tmp)
            
        # 直近の気象データ
        # weatherデータからデータを読み込み、平均値や合計日数などを習得しDataFrame化→contextに追加し、htmlで記載する
        # 県名はformsから取得する
       
        # if pref_form.is_valid():
        #     selected_pref = pref_form.cleaned_data["selected_pref"]
        #     weather_data = GetWeatherDataFromDatabase(selected_pref=selected_pref)
            # 気象情報と平均値を格納していく
            # weather_data_dict = GetWeatherInformation(weather_data)
            # if weather_form.is_valid():
            #     selected_weather_item = weather_form.cleaned_data["selected_weather_item"]
            #     weather_plot = WeatherGraph(weather_data, selected_weather_item)
            
        if date_form.is_valid():
            selected_date = date_form.cleaned_data["selected_date"]
            predicted_price = df[df["veg_datetime"]==selected_date]
            predicted_price = predicted_price["veg_price"].mean()
        
        
        context = {
            # 詳細ページの野菜名
            "veg_name":veg_name,
            "veg_img":veg_img,
            "price_transit":price_transit,
            # "share_data":share_data,
            # "weather_data":weather_data,
            # 産地のグラフ
            "produce_plot":produce_plot,
            # 価格推移のグラフ
            "price_plot":price_plot,
            # 予測値のデータ
            "predicted_price":predicted_price,
            # 気象情報のデータ
            # "weather_data_dict":weather_data_dict,
            # 気象情報の推移
            # "weather_plot":weather_plot,
            # form
            "month_form":month_form,
            "date_form":date_form
            # "pref_form":pref_form,
            # "weather_form":weather_form,
            
        }      
    return render(request, "veg_app/vegetable_detail.html", context)