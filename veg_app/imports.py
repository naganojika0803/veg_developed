#######
# データベースにデータを格納するための関数
#######

# import文
import pandas as pd
import csv
from .models import VegPriceTrend, VegPrice, WeatherData, VegetablePriceByPref, ProduceAmount
from .forms import VegSelectionForm
import os


# データベースに格納するためのデータをimportする関数を作成する
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
                    veg_price=veg_price
                )

def load_predicted_csv():
    pred_csv_list = [file for file in os.listdir("../../../../../detail/repredicted_data") if file.endswith('.csv')]
    # フルパスに変換
    pred_list = [os.path.join("../../../../../detail/repredicted_data", file) for file in pred_csv_list]
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

# 産地ごとのデータ
def load_price_data_by_pref():
    csv_list = [file for file in os.listdir("./../../../../detail/VegetablePriceByPref") if file.endswith(".csv")]
    # フルパスに変換
    pred_list = [os.path.join("./../../../../detail/VegetablePriceByPref", file) for file in csv_list]
    for csv_path in pred_list:
        print(f'{csv_path} is started')
        df = pd.read_csv(csv_path)
        for index, row in df.iterrows():
            datetime = row["datetime"]
            pref_name = row["pref_name"]
            price = row["price"]
            vegetable_name = row["vegetable"]
                    
            VegetablePriceByPref.objects.create(
                datetime=datetime,
                pref_name = pref_name,
                price = price,
                vegetable_name = vegetable_name
            )
    
# 産地ごとの気象データ
def load_weather_csv():
    csv_path = "./../../../../data_for_BItool/use_data/new_weather_df.csv"
    print(f'{csv_path} is started')
    df = pd.read_csv(csv_path)
    # 読み込んだ後、datetimeがdatetitime列の最大値+timedelta(days=1)からのデータに限定し、読み込む
    weather_data_list = []
    for index, row in df.iterrows():
        weather_information = row["key"]
        weather_value = row["value"]
        datetime = row["datetime"]
        pref_name = row["pref"]
             
        weather_data_list.append(WeatherData(
        datetime=datetime,
        pref_name=pref_name,
        amount=weather_value,
        item=weather_information
        ))
    # データベースに一括で追加
    WeatherData.objects.bulk_create(weather_data_list)
                
                
def load_share_csv():
    csv_path = "../../../../../data_for_BItool/use_data/share.csv"
    with open(csv_path, "r", encoding="utf-8") as f:
        df = pd.read_csv(csv_path)
        share_data_list = []
        for index, row in df.iterrows():
            month = row["month"]
            vegetable_name = row["item"]
            pref_name = row["pref"]
            amount = row["amount"]
            
            share_data_list.append(ProduceAmount(
                month = month,
                vegetable_name = vegetable_name,
                pref_name = pref_name,
                amount = amount
            ))
    ProduceAmount.objects.bulk_create(share_data_list)
    
            
            
            
            
    

