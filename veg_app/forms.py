from .models import VegPriceTrend, VegPrice
from django import forms

# 野菜を選択するclass
class VegSelectionForm(forms.Form):      
    # 自給率が高いもののみ
    choiceable_vegs = [
        ("kyabetsu","キャベツ"),
        ("retasu","レタス"),
        #("edamame", "枝豆"),
        #("enokidake", "えのき茸"),
        ("kabu", "かぶ"),
        #("kabocha", "かぼちゃ"),
        #("kansho", "かんしょ"),
        ("kyuuri", "きゅうり"),
        ("komatsuna", "小松菜"),
        ("gobou", "ごぼう"),
        ("satsumaimo", "さつまいも"),
        #("sayainngen", "さやいんげん"),
        #("sayaendou", "さやえんどう"),
        ("shimatogarashi", "島唐辛子"), # 島唐辛子だよ
        #("shimeji", "しめじ"),
        ("shungiku", "春菊"),
        #("shouga", "しょうが"),
        #("takenoko", "たけのこ"),
        ("tamanegi", "玉ねぎ"),
        ("daikon", "大根"),
        ("chingensai", "ちんげんさい"),
        ("nasu", "なす"),#
        #("nameko", "なめこ"),
        ("nira", "にら"),
        ("ninjin", "人参"),#
        #("ninniku", "にんにく"),
        ("negi", "ねぎ"),#
        ("hakusai", "白菜"),
        ("bareisho", "じゃがいも"),
        ("hourensou", "ほうれん草"),
        ("mizuna", "水菜"),
        #("mitsuba", "三つ葉"), #
        ("yamanoimo", "山芋"),
        ("renkon", "レンコン"),
        #("asparagus","アスパラガス"),#
        ("karifurawa", "カリフラワー"),#
        #("suitocorn", "スイートコーン"),#
        ("serori", "セロリ"),
        ("tomato", "トマト"),
        #("paseri", "パセリ"),
        ("piiman", "ピーマン"),
        #("burokkori", "ブロッコリ"),#
        #("minitomato", "ミニトマト"),#
        #("namashitake", "生しいたけ"),#
        #("udo", "うど"),#
        #("soramame", "そら豆"),#
        #("fuki", "ふき"),#
        #("jitsuenndou", "実えんどう")#
    ]
    selected_veg=forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={"class": "form-check-input", "size": "10"}),
        choices=choiceable_vegs,
    )
    selected_date = forms.DateField(
        label="Selected Date",
        widget=forms.TextInput(attrs={"type":"date"})
    )
