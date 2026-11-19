with open("baholar.txt", "r", encoding="utf-8") as f:
    ballar = [int(qator.strip()) for qator in f if qator.strip()]

soni = len(ballar)
eng_katta = max(ballar)
eng_kichik = min(ballar)
ortacha = sum(ballar) // soni

print(f"Barcha ballar: {ballar}")
print(f"Ballar soni: {soni}")
print(f"Eng katta ball: {eng_katta}")
print(f"Eng kichik ball: {eng_kichik}")
print(f"O'rtacha ball: {ortacha}")
