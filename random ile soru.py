import random

zarlar={1:0,2:0,3:0,4:0,5:0,6:0} #sözlük oluşturuldu.
for i in range(100):
    zar=random.randint(1,6)
    zarlar[zar] +=1
for zar  in zarlar:
    print(f"{zar} gelme olasılığı: {zarlar[zar]/100}") 

alti_alti=0
deneme_sayisi=0
while True:
    deneme_sayisi+=1
    zar1=random.randint(1,6)
    zar2=random.randint(1,6)
    if zar1==6 and zar2==6:
        alti_alti+=1
    if alti_alti==10:
        print(f"10 kere 6-6 gelmesi için zarlar {deneme_sayisi} kadar atıldı.")
        break

