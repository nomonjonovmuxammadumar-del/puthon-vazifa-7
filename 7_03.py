yangi_ism = input("Yangi ism kiriting: ")

with open("ismlar.txt", "a", encoding="utf-8") as f:
    f.write(yangi_ism + "\n")

print(f"'{yangi_ism}' ismi fayl oxiriga qo'shildi.")
