book_count = 10
print('Ibu berkata "Baca semua buku "')
read_count = 0
understood_count = 0
print(f"jumlah buku yang sudah dibaca dan dipahami {read_count}")

while read_count < book_count * 2:
    read_count += 1
    if understood_count == 9:
        print(f'Buku ke {understood_count + 1} belum paham')
    else:
        understood_count += 1
        print(f'Buku ke {understood_count} sudah dibaca dan dipahami')
    #print("baca satu buku yang belum dibaca")
    #jumlah_buku_yang_sudah_dibaca += 0
    print(f"buku ke {understood_count} sudah dibaca dan paham")

print(f"Jumlah buku yang sudah dibaca dan dipahami {understood_count}")
if understood_count == book_count:
    print(' Bu semua buku sudah dibaca dan dipahami')
else:
    print(f'Bu, tidak semua buku dipahami, Budi hanya paham {understood_count} buku')
