from django.db import models


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

# VegPriceTrend
class VegPriceTrend(models.Model):
    # 予測を行った野菜を随時追加してください
    
    
    veg_name = models.CharField(choices=vegetable_option, verbose_name="野菜の種類", max_length=255, null=True)
    veg_datetime = models.DateField(verbose_name="実測日", null=True)
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

pref_list = [("gunma", "群馬"),
                 ("chibca","千葉"),
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
                 ("miyazaki","宮崎"),
                 ("tokushima", "徳島"),
                 ("saga","佐賀"),
                 ("kumamoto", "熊本"),
                 ("gifu", "岐阜"),
                 ("oasaka", "大阪")]
    
class WeatherData(models.Model):
    item_list = [('total_rain_average',"平均降雨量"),
                 ('mean_temp_average', "平均気温"), 
                 ('max_temp_average',"最高気温の平均"),
                 ('min_temp_average', "最低気温の平均"),
                 ('mean_humidity_average', "湿度の平均"),
                 ('max_wind_average', "最大風速の平均"),
                 ('max_instantaneous_wind_average', "最大瞬間風速の平均"),
                 ('sunshine_hour_average',"日照時間の平均"),
                 ('total_snow_average', "平均降雪量"),
                 ('snow_deepest_average', "平均積雪量"),
                 ('temp_more_30_days', "30度以上を記録した日数"),
                 ('temp_more_35_days', "35度以上を記録した日数"),
                 ('temp_less_10_days',"10度以下を記録した日数"),
                 ('temp_less_0_days',"0度以下を記録した日数"),
                 ('rain_days',"降雨日数"),
                 ('snow_days',"降雪日数"),
                 ('typhoon_days',"台風が来た数"),
                 ('total_rain_for_3month', "降雨量の合計"),
                 ('total_sunshine_for_3month',"日照時間の合計"),
                 ('total_snow_for_3month', "降雪量の合計")]
    datetime = models.DateField(verbose_name="日付", null=True)
    pref_name = models.CharField(choices=pref_list, verbose_name="都道府県名", max_length=255)
    amount = models.FloatField(verbose_name = "観測量", null=True) 
    item = models.CharField(choices=item_list, verbose_name="観測項目", max_length=255)
    
    def __str__(self):
        return f'{self.datetime}-{self.pref_name}-{self.item}'
    

class VegetablePriceByPref(models.Model):
    datetime = models.DateField(verbose_name="日付", null=True)
    pref_name = models.CharField(choices=pref_list, verbose_name="都道府県名", max_length=255)
    price = models.FloatField(verbose_name="価格", null=True, blank=True)
    vegetable_name = models.CharField(choices=vegetable_option, verbose_name="野菜名", max_length=255)
    
    def __str__(self):
        return f'{self.datetime}-{self.pref_name}-{self.vegetable_name}-{self.price}'
    
month_list = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12)]
class ProduceAmount(models.Model):
    month = models.IntegerField(choices=month_list, verbose_name="月")
    vegetable_name = models.CharField(choices=vegetable_option, verbose_name="野菜名", max_length=255)
    pref_name = models.CharField(choices=pref_list, verbose_name="都道府県名", max_length=255)
    amount = models.FloatField(verbose_name="出荷量", null=True)        
    