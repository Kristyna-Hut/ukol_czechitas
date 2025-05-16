import csv
import json

def ocisti_seznam(seznam):
    nove_casti = []
    for udaj in seznam:
        ocistena = udaj.strip()
        if ocistena != "":
            nove_casti.append(ocistena)
    return nove_casti

with open("netflix_titles.tsv", mode="r", encoding="utf-8") as soubor:
    netflix = csv.DictReader(soubor, delimiter="\t")

    upravene_zaznamy = []

    for radek in netflix:
        novy = {}

        novy["title"] = radek["PRIMARYTITLE"].strip()

        if radek["DIRECTOR"].strip() != "":
            seznam_reziseru = radek["DIRECTOR"].split(",")
            novy["directors"] = ocisti_seznam(seznam_reziseru)
        else:
            novy["directors"] = []

        if radek["CAST"].strip() != "":
            seznam_hercu = radek["CAST"].split(",")
            novy["cast"] = ocisti_seznam(seznam_hercu)
        else:
            novy["cast"] = []

        if radek["GENRES"].strip() != "":
            seznam_zanru = radek["GENRES"].split(",")
            novy["genres"] = ocisti_seznam(seznam_zanru)
        else:
            novy["genres"] = []

        rok = int(radek["STARTYEAR"])
        novy["decade"] = (rok // 10) * 10

        upravene_zaznamy.append(novy)

with open("hw02_output.json", mode="w", encoding="utf-8") as ukol2_json:
    json.dump(upravene_zaznamy, ukol2_json, ensure_ascii=False, indent=4)
