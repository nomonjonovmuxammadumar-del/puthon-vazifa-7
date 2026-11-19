qidirilayotgan_ism = input("Qidirilayotgan ismni kiriting: ").strip()

with open("ismlar.txt", "r", encoding="utf-8") as f:
    ismlar = [qator.strip() for qator in f]

if qidirilayotgan_ism in ismlar:
    print("Ism topildi")
else:
    print("Ism topilmadi")
