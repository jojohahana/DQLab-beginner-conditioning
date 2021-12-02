# Declare tagihan
tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan) #panjang (banyaknya tagihan) dalam list tagihan tsb
total_tagihan = 1
while i < jumlah_tagihan: 
    # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
    # pengulangan akan dihentikan
    if tagihan[i] < 0:
        total_tagihan = -1
        print("terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan += tagihan[i]
	#i += 1 --> check lagi problemnya dimana
print(total_tagihan)

