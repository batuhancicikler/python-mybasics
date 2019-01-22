# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:44:14 2019

@author: batuhan
"""

#%% İki sayının toplamı

    a = 5
    b = 9
    toplam = a + b
    print(toplam)
    
#%% Kullanıcıdan girilen iki sayının toplamı
    
    a = int(input("Birinci sayı : "))
    b = int(input("İkinci sayı : "))
    
    print("{} ile {} toplamı eşittir {}".format(a, b, a + b))
    
#%% İki sayının ortalaması
    
  a = float(input("Ortalamasını istediğiniz ilk sayı : "))
  b = float(input("Ortalamasını istediğiniz ikinci sayı : "))
    
  print("{} sayısı ile {} sayısının ortalaması eşittir {}".format(a,b, (a+b)/2))
  
#%% Virgülle girilen sayıların ortalamasını alır
  
girdi = input("Ortalamasını almak istediğiniz sayıları giriniz : ")

    # Önce virgülle ayıralım
    
girdiX = girdi.split(",")

toplam = 0
    
    # Şimdi döngüyle toplatıcaz
    
for i in girdiX:
    
    #her i girdi elemanlarından birinin integerini alır.
    toplam = toplam + int(i)
    
    #şimdi de toplamları girdideki eleman sayısına böldürelim.
print("{} sayılarının ortalaması {}".format(girdiX, (toplam / len(girdiX))))

#%% 3 e ve 5 e tam bölünen sayıları listele

for i in range(0,101):
    if((i%3 == 0) and (i%5 == 0)):
        print(i)

#%% belirtilen başlangıc, bitiş ve adım değerine göre aralarındaki sayıları toplama

baslangıc = int(input("baslangıc : "))
aralık = int(input("aralık : "))
bitis = int(input("bitis : "))
toplam = 0
for i in range(baslangıc, bitis + 1, aralık):  #range kodunda 3. değer kaç atlama ile gezeceğini hesaplar
    toplam = toplam + i
print(toplam)

#%% 0 dan 100 e kadar çift sayıların toplamı
i=0
toplam = 0
while(i<=100):
    if(i%2 == 0):
        toplam = toplam + i
    i = i + 1
print(toplam)

#%% girilen metni harflerine ayırma

a = input()

for i in a:
    print(i)

#%%

def repeat(s, exclaim):
    
    result = s * 3
    if exclaim:
        result = result + "!!!"
    return result

#%%
    
text = "%d küçük domuz çıktı, ya da bu %s, ve ben %s" % (3, "huf", "puf")

#%d int, %s string, %f%g float point





