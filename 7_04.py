with open("mahsulotlar.txt", "w", encoding="utf-8") as f:
    for i in range(1, 6):
        mahsulot = input(f"{i}-mahsulot nomini kiriting: ")
        f.write(mahsulot + "\n")

print("\nFayldagi barcha mahsulotlar:")
with open("mahsulotlar.txt", "r", encoding="utf-8") as f:
    for qator in f:
        print(qator.strip())
