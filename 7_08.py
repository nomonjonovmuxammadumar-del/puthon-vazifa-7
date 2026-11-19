with open("sonlar.txt", "r", encoding="utf-8") as f_in, open("juft_sonlar.txt", "w", encoding="utf-8") as f_out:
    for qator in f_in:
        satr = qator.strip()
        if satr:
            son = int(satr)
            if son % 2 == 0:
                f_out.write(f"{son}\n")

print("Juft sonlar 'juft_sonlar.txt' fayliga muvaffaqiyatli yozildi.")
