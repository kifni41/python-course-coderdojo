def cek_kelulusan(nilai) :
	print('fungsi cek kelulusan')
	hasil = False
	if nilai > 50 :
		lulus = True
	return hasil

#calling function
lulus = cek_kelulusan(5)
print(lulus)

##################################

#cannot call here, because not defined yet
#print hitung_segitiga(454,44)

def hitung_segitiga(alas,tinggi) :
	hasil = alas * tinggi / 2
	return hasil

print hitung_segitiga(3,4)
print hitung_segitiga(10,30)
print hitung_segitiga(4,333)

