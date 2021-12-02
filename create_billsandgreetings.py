#membuat tagihan ditambah dengan salam sesuai dengan jam
jam = 17
tagihan_ke = 'Mr. Yoyo'
warehousing = { 'harga_harian': 1000000, 'total_hari':15 } 
cleansing = { 'harga_harian': 1500000, 'total_hari':10 } 
integration = { 'harga_harian':2000000, 'total_hari':15 } 
transform = { 'harga_harian':2500000, 'total_hari':10 }
sub_warehousing = warehousing['harga_harian']*warehousing['total_hari'] 
sub_cleansing = cleansing['harga_harian']*cleansing['total_hari'] 
sub_integration = integration['harga_harian']*integration['total_hari'] 
sub_transform = transform['harga_harian']*transform['total_hari']
total_harga = sub_warehousing+sub_cleansing+sub_integration+sub_transform
print("Tagihan kepada:")
print(tagihan_ke)
if jam > 19: #diatas jam 7 malam
    print("Selamat malam, anda harus membayar tagihan sebesar:")
elif jam > 17: #diatas jam 5 sore 
    print("Selamat sore, anda harus membayar tagihan sebesar:")  
elif jam > 12: #diatas jam 12 siang
    print("Selamat siang, anda harus membayar tagihan sebesar:")
else: #kondisi selain diatas
    print("Selamat pagi, anda harus membayar tagihan sebesar:") 
print(total_harga)