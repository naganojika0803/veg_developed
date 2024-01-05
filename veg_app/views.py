from django.shortcuts import render, redirect

import csv
from .models import VegPriceTrend, VegPrice
from .forms import VegSelectionForm
import os

import plotly.graph_objects as go   
from plotly.subplots import make_subplots
import pandas as pd
from io import BytesIO
import base64


# 野菜ごとのトレンドが格納されているcsvファイルを読み込む
# 全て同じディレクトリに存在しているのでfor文で順番に行っていく
# ディレクトリ内のファイルを取得

def load_csv_data():
    trend_csv_list = [file for file in os.listdir("../../../../../detail/price_trend") if file.endswith('.csv')]
    # フルパスに変換
    trend_list = [os.path.join("../../../../../detail/price_trend", file) for file in trend_csv_list]
    for csv_path in trend_list:
        print(csv_path, "start")
        with open(csv_path, "r", encoding="utf-8") as f:
            df = pd.read_csv(csv_path)
            for index, row in df.iterrows():
                veg_name = row["veg_name"]
                veg_datetime = row["datetime"]
                veg_price = int(row["price"])
            
                VegPriceTrend.objects.create(
                    veg_name=veg_name,
                    veg_datetime=veg_datetime,
                    # veg_year=veg_year,
                    # veg_month=veg_month,
                    veg_price=veg_price
                )
        
#load_csv_data()

# 予測値を格納しているcsvファイルをdbに保存する　
def load_predicted_csv():
    pred_csv_list = [file for file in os.listdir("../../../../../detail/predicted_data") if file.endswith('.csv')]
    # フルパスに変換
    pred_list = [os.path.join("../../../../../detail/predicted_data", file) for file in pred_csv_list]
    for csv_path in pred_list:
        print(csv_path, "start")
        with open(csv_path, "r", encoding="utf-8") as f:
            df = pd.read_csv(csv_path)
            for index, row in df.iterrows():
                veg_name = row["kind_of_veg"]
                veg_datetime = row["datetime"]
                veg_price = int(row["pred"])
            
                VegPrice.objects.create(
                    veg_name=veg_name,
                    veg_datetime=veg_datetime,
                    veg_price=veg_price
                )
        
#load_predicted_csv()

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
    


# グラフの描写と予測値を返す関数
from .utils import create_graph

def some_view(request):
    graphic_transit = None
    graphic_box = None
    graphic_hist = None
    view_list = []
    
    if request.method == "POST":
        form = VegSelectionForm(request.POST)
        if form.is_valid():
            selected_veg = form.cleaned_data["selected_veg"]
            selected_date = form.cleaned_data["selected_date"]
            # データベースから選択された野菜のデータを取得
            for veg in selected_veg:
                selected_veg_data = get_veg_data_from_database(veg)

            graphic_transit, graphic_box, graphic_hist = create_graph(selected_veg_data, selected_veg)
            
            # 以下に予測値を返すコードを記載
            for veg in selected_veg:
                prediction_price = VegPrice.objects.filter(
                    veg_name=veg,
                    veg_datetime=selected_date
                ).first()
                # 値を格納
                view_list.append({"selected_veg":veg,
                                  "selected_date":selected_date,
                                  "prediction_price":prediction_price.veg_price})
                
    else:
        form = VegSelectionForm() 
    context = {
        "view_list":view_list,
        "graphic_transit":graphic_transit,
        "graphic_hist":graphic_hist,
        "graphic_box":graphic_box,
        "graphic_form":form
}

    return render(request, "veg_app/frontpage.html", context)
