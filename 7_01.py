with open("ismlar.txt", "w", encoding="utf-8") as f:
    for i in range(1, 6):
        ism = input(f"{i}-ismni kiriting: ")
        f.write(ism + "\n")

print("Ismlar 'ismlar.txt' fayliga muvaffaqiyatli yozildi.")
