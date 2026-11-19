with open("matn.txt", "r", encoding="utf-8") as f:
    qatorlar = f.readlines()

print(f"Fayldagi qatorlar soni: {len(qatorlar)}")
