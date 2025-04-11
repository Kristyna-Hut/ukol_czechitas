import json

with open ("alice.txt", mode = "r", encoding = "utf-8") as alice:
    slovnik = {}
    alice_text = alice.read()

    alice_text = alice_text.replace("\n", " ").lower()
    
    for pismeno in alice_text:
        if pismeno != " ":
            if pismeno in slovnik:
                slovnik[pismeno] += 1
            else:
                slovnik[pismeno] = 1

with open ("ukol.json", mode = "w", encoding = "utf-8") as ukol_json:
    json.dump(slovnik, ukol_json, ensure_ascii = False)

