# import文
from io import BytesIO
import base64
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import japanize_matplotlib
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

# 表示させるグラフを作成する関数
def create_graph(selected_veg_data, selected_veg):
    # 推移グラフでは将来、過去のデータを用いる
    # 箱ひげ図とヒストグラムは過去のデータのみ用いる
    # 今月の初日の日付を格納
    first_date_of_this_month = datetime.now().replace(day=1).date()
    
    past_data = selected_veg_data[selected_veg_data["veg_datetime"]<first_date_of_this_month]
    predicted_data = selected_veg_data[selected_veg_data["veg_datetime"]>=first_date_of_this_month]
    
    # 推移グラフ
    fig_transit = go.Figure()
    # ユーザーが選択した野菜の推移グラフを描写
    for veg in selected_veg:
        # 実測値でのグラフ
        fig_transit.add_trace(go.Scatter(x=past_data["veg_datetime"],
                                         y=past_data[past_data['veg_name'] == veg]['veg_price'],
                                         mode="lines", name="実測値"))
        # 予測値のグラフ
        fig_transit.add_trace(go.Scatter(x=predicted_data["veg_datetime"],
                                         y=predicted_data[predicted_data["veg_name"]==veg]["veg_price"],
                                         mode="lines", name="予測値",line=dict(color='darkred')))
        
    # レイアウトの設定
    fig_transit.update_layout(height=500, xaxis_title="日付", yaxis_title="価格", 
                              plot_bgcolor="#B0C4DE", paper_bgcolor='#B0C4DE')
    
    # グラフを画像として保存
    buffer_transit = BytesIO()  # メモリ上にバイナリデータを格納するためのバッファ 
    fig_transit.write_image(buffer_transit, format="png") # Plotlyで作成したプロットをPNGで保存
    buffer_transit.seek(0) # バッファのポインタを先頭に戻す
    image_transit = buffer_transit.getvalue() # バッファの内容(PNG画像データ)を取得
    buffer_transit.close() # バッファを閉じ、メモリを解放
    
    # 箱ひげ図
    fig_box = go.Figure()
    for veg in selected_veg:
        fig_box.add_trace(go.Box(y=past_data[past_data['veg_name'] == veg]['veg_price'], name=veg))
    # レイアウト設定
    fig_box.update_layout(height=500, yaxis_title="価格",
                          plot_bgcolor="#B0C4DE", paper_bgcolor='#B0C4DE')
    # グラフを画像として保存
    buffer_box = BytesIO()
    fig_box.write_image(buffer_box, format="png")
    buffer_box.seek(0)
    image_box = buffer_box.getvalue()
    buffer_box.close()
    
    # ヒストグラム
    fig_hist = go.Figure()
    for veg in selected_veg:
        fig_hist.add_trace(go.Histogram(x=past_data[past_data['veg_name'] == veg]['veg_price'],
                                       nbinsx=20, opacity=0.7, name=veg))
    # レイアウト設定
    fig_hist.update_layout(height=500, xaxis_title="価格", yaxis_title="頻度",
                           plot_bgcolor="#B0C4DE", paper_bgcolor='#B0C4DE')
    # グラフを画像として保存
    buffer_hist = BytesIO()
    fig_hist.write_image(buffer_hist, format="png")
    buffer_hist.seek(0)
    image_hist = buffer_hist.getvalue()
    buffer_hist.close()
    
    # 画像をBase64エンコード
    graphic_transit = base64.b64encode(image_transit).decode("utf-8")
    graphic_box = base64.b64encode(image_box).decode("utf-8")
    graphic_hist = base64.b64encode(image_hist).decode("utf-8")
    
    # return
    return graphic_transit, graphic_box, graphic_hist



def WeatherGraph(weather_df, item):
    """
    weather_df:気象情報が格納されたDataFrame
    weather_item:可視化する気象情報
    """
    # 可視化するデータはviews.pyの関数でデータを事前に抽出します(県名)
    # 項目を指定してplotを行うデータを抽出する
    fig_title = {"mean_temp_average":"平均気温", 
                 "temp_more_30_days":"30度以上の日数", 
                 "total_sunshine_for_3month":"日照時間の平均",
                 "rain_days":"降雨日数"}
    plot_df = weather_df[weather_df["item"]==item]
    plt.figure(figsize=(12,8))
    sns.lineplot(data=plot_df, x="datetime", y="amount")
    plt.title(f"{fig_title[item]}の推移")
    plt.xlabel("日付")
    plt.ylabel("amount")
    plt.tight_layout()
    graph = GraphToImage()

    return graph

# グラフを保存する過程を関数化
def GraphToImage():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    img = buffer.getvalue()
    graph = base64.b64encode(img).decode("utf-8")
    buffer.close()
    return graph
    

class CreateGraphs(object):
# Vegetable_detailで生産量の棒グラフを作成する
    def ProduceAmountPlot(share_data, month):
        # share_data：野菜ごと分けられた月毎、出荷都道府県ごとの出荷量のデータ
        # month：対象月
        plot_df = share_data[share_data["month"]==month].sort_values("amount", ascending=False)
        plt.figure(figsize=(12,8))
        sns.barplot(data=plot_df, x="pref_name", y="amount")
        vegetable_name = plot_df.iloc[0]["vegetable_name"]
        plt.title(f"{vegetable_name}の{month}月  入荷量（令和元年）")
        plt.xlabel("都道府県")
        plt.ylabel("入荷量")
        plt.tight_layout()
        graph = GraphToImage()
        
        return graph
    
    def PriceTransitPlot(price_data):
        vegetable_name = price_data.loc[0,"veg_name"]
        plt.figure(figsize=(12,8))
        sns.lineplot(data=price_data[price_data["actual_predict"]=="actual"], x="veg_datetime", y="veg_price", color="blue", label="実測値")
        sns.lineplot(data=price_data[price_data["actual_predict"]=="predict"], x="veg_datetime", y="veg_price", color="red", label="予測値")
        plt.title(f'{vegetable_name}の価格推移')
        plt.xlabel("datetime")
        plt.ylabel("価格")
        plt.legend()
        plt.tight_layout()
        graph = GraphToImage()
        
        return graph
        
        
def GetWeatherInformation(weather_data):
    weather_information = {}
    # 直近90日の平均値
    today = datetime.now().date()
    start_day = today - timedelta(days=30)
    end_day = today - timedelta(days=1)
    weather_data["datetime"] = pd.to_datetime(weather_data["datetime"])
    weather_data_this_year = weather_data[(weather_data["datetime"]>=start_day)&(weather_data["datetime"]<=end_day)]
    weather_data_past  = weather_data[weather_data["datetime"]<=start_day]
        
    item_list = ["mean_temp_average", "temp_more_30_days", "total_sunshine_for_3month", "rain_days"]
        
    for item in item_list:
        weather_information[f"this_year_{item}"] = np.mean(weather_data_this_year[item])
        weather_information[f"past_{item}"] = np.mean(weather_data_past[item])
            
    return weather_information
        
        
    
    
    
    
    

