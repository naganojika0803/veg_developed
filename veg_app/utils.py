# import文
from io import BytesIO
import base64
import plotly.graph_objects as go
from datetime import datetime

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