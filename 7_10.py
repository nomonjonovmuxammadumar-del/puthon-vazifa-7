jami = 0

print("--- Xarajatlar hisoboti ---")
with open("xarajatlar.txt", "r", encoding="utf-8") as f:
    for qator in f:
        satr = qator.strip()
        if satr:
            qismlar = satr.rsplit(" ", 1)
            nomi = qismlar[0]
            summa = int(qismlar[1])
            jami += summa
            print(f"{nomi}: {summa} so'm")

print("---------------------------")
print(f"Jami xarajatlar summasi: {jami} so'm")
