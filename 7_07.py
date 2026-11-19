with open("matn.txt", "r", encoding="utf-8") as f:
    matn = f.read()

sozlar = matn.split()

eng_uzun = ""
for soz in sozlar:
    if len(soz) > len(eng_uzun):
        eng_uzun = soz

print(f"Eng uzun so'z: {eng_uzun}")
