from django.db import models

# VegPriceTrend
class VegPriceTrend(models.Model):
    # 予測を行った野菜を随時追加してください
    vegetable_option = [
        ("キャベツ","キャベツ"),
        ("レタス","レタス"),
        #("枝豆", "枝豆"),
        #("えのき茸", "えのき茸"),
        ("かぶ", "かぶ"),
        #("かぼちゃ", "かぼちゃ"),
        #("かんしょ", "かんしょ"),
        ("きゅうり", "きゅうり"),
        ("小松菜", "小松菜"),
        ("ごぼう", "ごぼう"),
        ("さつまいも", "さつまいも"),
        #("さやいんげん", "さやいんげん"),
        #("さやえんどう", "さやえんどう"),
        ("島唐辛子", "島唐辛子"),
        #("しめじ", "しめじ"),
        ("春菊", "春菊"),
        #("しょうが", "しょうが"),
        #("たけのこ", "たけのこ"),
        ("玉ねぎ", "玉ねぎ"),
        ("大根", "大根"),
        ("ちんげんさい", "ちんげんさい"),
        ("なす", "なす"),
        #("nameko", "なめこ"),
        ("にら", "にら"),
        ("人参", "人参"),
        #("にんにく", "にんにく"),
        ("ねぎ", "ねぎ"),
        ("白菜", "白菜"),
        ("じゃがいも", "じゃがいも"),
        ("ほうれん草", "ほうれん草"),
        ("水菜", "水菜"),
        #("三つ葉", "三つ葉"),
        ("山芋", "山芋"),
        ("レンコン", "レンコン"),
        #("アスパラガス","アスパラガス"),
        ("カリフラワー", "カリフラワー"),
        #("スイートコーン", "スイートコーン"),
        ("セロリ", "セロリ"),
        ("トマト", "トマト"),
        #("パセリ", "パセリ"),
        ("ピーマン", "ピーマン"),
        #("ブロッコリ", "ブロッコリ"),
        #("ミニトマト", "ミニトマト"),
        #("生しいたけ", "生しいたけ"),
        #("うど", "うど"),
        #("そら豆", "そら豆"),
        #("ふき", "ふき"),
        #("実えんどう", "実えんどう")
    ]
    
    veg_name = models.CharField(choices=vegetable_option, verbose_name="野菜の種類", max_length=255, null=True)
    veg_datetime = models.DateField(verbose_name="実測日", null=True)
    # veg_year = models.DecimalField(verbose_name="年", max_digits=4, decimal_places=0, null=True)
    # veg_month = models.DecimalField(verbose_name="月", max_digits=2, decimal_places=0, null=True)
    veg_price = models.IntegerField(verbose_name="価格", null=True)

    def __str__(self):
        return f'{self.veg_name}-{self.veg_price}-{self.veg_datetime}'
    


# VegPrice
class VegPrice(models.Model):
    # 予測を行った野菜を随時追加してください
    vegetable_option = [
        ("kyabetsu","キャベツ"),
        ("retasu","レタス"),
        ("edamame", "枝豆"),
        ("enokidake", "えのき茸"),
        ("kabu", "かぶ"),
        ("kabocha", "かぼちゃ"),
        ("kansho", "かんしょ"),
        ("kyuuri", "きゅうり"),
        ("komatsuna", "小松菜"),
        ("gobou", "ごぼう"),
        ("satsumaimo", "さつまいも"),
        ("sayainngen", "さやいんげん"),
        ("sayaendou", "さやえんどう"),
        ("shishitou", "ししとう"),
        ("shimeji", "しめじ"),
        ("shungiku", "春菊"),
        ("shouga", "しょうが"),
        ("takenoko", "たけのこ"),
        ("tamanegi", "玉ねぎ"),
        ("daikon", "大根"),
        ("chingensai", "ちんげんさい"),
        ("nasu", "なす"),
        ("nameko", "なめこ"),
        ("nira", "にら"),
        ("ninjin", "人参"),
        ("ninniku", "にんにく"),
        ("negi", "ねぎ"),
        ("hakusai", "白菜"),
        ("bareisho", "じゃがいも"),
        ("hourensou", "ほうれん草"),
        ("mizuna", "水菜"),
        ("mitsuba", "三つ葉"),
        ("yamanaimo", "山芋"),
        ("renkon", "レンコン"),
        ("asparagus","アスパラガス"),
        ("karifurawa", "カリフラワー"),
        ("suitocorn", "スイートコーン"),
        ("serori", "セロリ"),
        ("tomato", "トマト"),
        ("paseri", "パセリ"),
        ("piiman", "ピーマン"),
        ("burokkori", "ブロッコリ"),
        ("minitomato", "ミニトマト"),
        ("namashitake", "生しいたけ"),
        ("udo", "うど"),
        ("soramame", "そら豆"),
        ("fuki", "ふき"),
        ("jitsuenndou", "実えんどう")
    ]
    
    veg_name = models.CharField(choices=vegetable_option, verbose_name="野菜の種類", max_length=255, null=True)
    veg_datetime = models.DateField(verbose_name="予測日", null=True)
    veg_price = models.IntegerField(verbose_name="価格", null=True)

    def __str__(self):
        return f'{self.veg_name}-{self.veg_datetime}'
    
    