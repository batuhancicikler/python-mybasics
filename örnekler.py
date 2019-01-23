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

# %d int, %s string, %f%g float point

#%%
liste = [0,1,2,3,4,5,6,"batu","han"]
liste2 = [55,"a","85",3.14]

liste.append("aaa")
liste2.insert(3, "pi")
liste.extend(liste2)
print(liste.index("batu"))
liste2.remove(3.14)
liste.reverse(liste.sort())

#%% listenin tekrar eden elemanlarından kurtulma
a = [5,8,7,6,5,4,2,3,1,1]
def kurtul(nums):
    yeni_nums = []
    for num in nums or len(yeni_nums) == 0:
        if num != yeni_nums:
            yeni_nums.append(num)
    return yeni_nums

print(kurtul(a))

#%% key ile sıralama

strs = ["tv","Az","zz","ab","aa"]

def fonks(s):
    return s[-1]

print(sorted(strs, key=fonks))

#%% Tuple ler
    
tupleler = (1,2,"merhaba")
print (len(tupleler))
print (tupleler[2])

tupleler = (1,2,"görüşürüz")
print (tupleler[2])

tupleler = (1,)

(x, y, z) = (357,45,-2)

print (z)

#%% liste comprehensions

nums = [2,5,7,8]

karesi = [n * n for n in nums]

küpü = [n * n * n for n in nums]

strs = [str(n) for n in nums]

caps = [s.upper() + "!!!" for s in strs]

smals =  [n for n in nums if n <= 5]

#%% Dicts and files

dict1 = {}

dict1["a"] = "alpha"
dict1["g"] = "gamma"
dict1["o"] = "omega"

print (dict1)
print (dict1["a"])

print (50 * "*")
if "z" in dict1: print ("z")
for key in dict1: print (key)

print (50 * "*")
print (dict1.keys())
print (dict1.values())
print (dict1.items())

print (50 * "*")
for key in sorted(dict1.keys()):
    print (key, dict1[key])

print (50 * "*")
for anahtar, değer in dict1.items(): print (anahtar, ">", değer)









