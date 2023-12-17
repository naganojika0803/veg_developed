import csv
from .models import VegPriceTrend
 
def import_csv_to_database(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            VegPriceTrend.objects.create(
                    datetime=row["datetime"],
                    year=row["year"],
                    month=row["month"],
                    day=row["day"],
                    edamame=row['edamame'],
                    enokidake=row['enokidake'],
                    kabu=row['kabu'],
                    kabocha=row['kabocha'],
                    kansho=row['kansho'],
                    kyuuri=row['kyuuri'],
                    komatsuna=row['komatsuna'],
                    gobou=row['gobou'],
                    satsumaimo=row['satsumaimo'],
                    sayainngen=row['sayainngen'],
                    sayaendou=row['sayaendou'],
                    shishitou=row['shishitou'],
                    shimeji=row['shimeji'],
                    shungiku=row['shungiku'],
                    shouga=row['shouga'],
                    takenoko=row['takenoko'],
                    tamanegi=row['tamanegi'],
                    chingensai=row['chingensai'],
                    nasu=row['nasu'],
                    nameko=row['nameko'],
                    nira=row['nira'],
                    ninjin=row['ninjin'],
                    ninniku=row['ninniku'],
                    negi=row['negi'],
                    hakusai=row['hakusai'],
                    bareisho=row['bareisho'],
                    hourensou=row['hourensou'],
                    mizuna=row['mizuna'],
                    mitsuba=row['mitsuba'],
                    yamanaimo=row['yamanaimo'],
                    renkon=row['renkon'],
                    asparagus=row['asparagus'],
                    karifurawa=row['karifurawa'],
                    kyabetsu=row['kyabetsu'],
                    suitocorn=row['suitocorn'],
                    serori=row['serori'],
                    tomato=row['tomato'],
                    paseri=row['paseri'],
                    piiman=row['piiman'],
                    burokkori=row['burokkori'],
                    minitomato=row['minitomato'],
                    retasu=row['retasu'],
                    namashitake=row['namashitake'],
                    udo=row['udo'],
                    soramame=row['soramame'],
                    fuki=row['fuki'],
                    jitsuenndou=row['jitsuenndou'],
            )
 
 
import_csv_to_database("../../../../../detail/vegetable_price_transition.csv")
 
 