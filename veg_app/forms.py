from .models import VegPriceTrend, VegPrice
from django import forms
from datetime import date

# 野菜を選択するclass
class VegSelectionForm(forms.Form):      
    # 自給率が高いもののみ
    choiceable_vegs = [
        ("kyabetsu","キャベツ"),
        ("retasu","レタス"),
        ("kabu", "かぶ"),
        ("kansho", "かんしょ"),
        ("kyuuri", "きゅうり"),
        ("komatsuna", "小松菜"),
        ("gobou", "ごぼう"),
        ("shishitou", "ししとう"), 
        ("shungiku", "春菊"),
        ("tamanegi", "玉ねぎ"),
        ("daikon", "大根"),
        ("chingensai", "ちんげんさい"),
        ("nasu", "なす"),#
        ("nira", "にら"),
        ("ninjin", "人参"),#
        ("negi", "ねぎ"),#
        ("hakusai", "白菜"),
        ("bareisho", "じゃがいも"),
        ("hourensou", "ほうれん草"),
        ("mizuna", "水菜"),
        ("yamanoimo", "山芋"),
        ("renkon", "レンコン"),
        ("karifurawa", "カリフラワー"),#
        ("serori", "セロリ"),
        ("tomato", "トマト"),
        ("piiman", "ピーマン"),
    ]
    selected_veg=forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={"class": "form-check-input", "size": "10"}),
        choices=choiceable_vegs,
    )
    selected_date = forms.DateField(
        label="Selected Date",
        widget=forms.TextInput(attrs={"type":"date"})
    )

class DateSelection(forms.Form):
    selected_date = forms.DateField(label="Selected Date", widget=forms.TextInput(attrs={"type":"date"}))


class MonthSelection(forms.Form):
    # 対象月を選ぶforms
    month_choice = [
        (1, "1月"),
        (2, "2月"),
        (3, "3月"),
        (4, "4月"),
        (5, "5月"),
        (6, "6月"),
        (7, "7月"),
        (8, "8月"),
        (9, "9月"),
        (10, "10月"),
        (11, "11月"),
        (12, "12月")
    ]
    selected_month = forms.ChoiceField(choices=month_choice)
    
# 期間を指定するform
class DateForm(forms.Form):
    # デフォルト値を記載する
    default_start = date.today().replace(year=date.today().year - 3, month=1, day=1)
    
    start_datetime = forms.DateField(label="開始日時", initial=default_start, widget=forms.DateInput(attrs={"type":"date"}))
    end_datetime = forms.DateField(label="終了日時", widget=forms.DateInput(attrs={"type":"date"}))
    
# 都道府県名を取得するform
class GetPrefName(forms.Form):
    # 都道府県名のリストを作成
    pref_choice = [
        ("gunma", "群馬"),
        ("chiba","千葉"),
        ("ibaraki", "茨城"),
        ("iwate", "岩手"),
        ("kanagawa", "神奈川"),
        ("nagano", "長野"),
        ("hyogo", "兵庫"),
        ("tochigi", "栃木"),
        ("fukuoka","福岡"),
        ("yamanashi","山梨"),
        ("nagasaki", "長崎"),
        ("shizuoka", "静岡"),
        ("kagawa", "香川"),
        ("kumamoto", "熊本"),
        ("hokkaido", "北海道"),
        ("saitama", "埼玉"),
        ("kochi", "高知"),
        ("kagoshima", "鹿児島"),
        ("tokushima", "徳島"),
        ("okinawa","沖縄"),
        ("akita", "秋田"),
        ("nigata", "新潟"),
        ("yamagata", "山形"),
        ("aomori", "青森"),
        ("miyazaki", "宮崎"),
        ("tokyo", "東京"),
        ("tokushima", "徳島"),
        ("saga","佐賀"),
        ("kumamoto", "熊本"),
        ("gifu", "岐阜"),
        ("osaka", "大阪")
    ]
    
    selected_pref = forms.ChoiceField(choices=pref_choice)
    
    
class GetWeatherItem(forms.Form):
    item_list = [
        ("mean_temp_average", "平均気温"),
        ("temp_more_30_days", "30度以上の日数"),
        ("total_sunshine_for_3month", "日照時間の合計"),
        ("rain_days", "降雨日数")
    ]
    selected_weather_item = forms.ChoiceField(choices=item_list)