wyniki=[60,50,60,58,54,54,58,50,52,54,48,69,34,55,51,52,44,
51,69,64,66,55,52,61,46,31,57,52,44,18,41,53,55,61,51,44]

koszty=[.25, .27, .25, .25, .25, .25, .33, .31, .25, .29,
.27, .22, .31, .25, .25, .33, .21, .25, .25, .25, .28, .25,
.24, .22, .20, .25, .30, .25, .24, .25, .25, .25, .27, .25,
.26, .29]

dlugosc=len(wyniki)
najwyzszy_wynik=0

for i in range(dlugosc):
	print ('Wynik roztworu #'+ str(i), 'to:', wyniki[i])
	if wyniki[i]>najwyzszy_wynik:
		najwyzszy_wynik=wyniki[i];
print ('Liczba testow :', dlugosc)
print ('Najwyzszy wynik to:', najwyzszy_wynik)

najlepsze_roztwory=[]
for i in range(dlugosc):
	if najwyzszy_wynik == wyniki[i]:
	   najlepsze_roztwory.append(i)

print('Roztwory o najwyzszym wyniku:', najlepsze_roztwory)

koszt=100.0
najbardziej_oplacalny=0

for i in range(dlugosc):
	if wyniki[i]==najwyzszy_wynik and koszty[i]<koszt:
		najbardziej_oplacalny=i
		koszt=koszty[i]
print('Roztwor o najwyzszym wyniku i najnizszych kosztach produkcji ma numer',
 najbardziej_oplacalny, 'i kosztuje', koszty[najbardziej_oplacalny])
