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
    for num in nums:
        if num not in yeni_nums:
            yeni_nums.append(num)
    return yeni_nums

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

#%% Dicts

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

#%% dicts 2

deneme = {}
deneme["ad"] = "batuhan"
deneme["soyad"] = "cicikler"
deneme["yas"] = 22

s = """Benim adım %(ad)s soyadım ise %(soyad)s \
ve ben %(yas)d yaşındayım.""" %deneme # %s string için %d ise int için

dicts = {1:1, 2:2, 3:3}
print (dicts)

print(10 * "*")

del dicts[2]
print (dicts)

#%% Files

import codecs

f = codecs.open(dosya_ismi.txt, "rU", "utf-8")

for line in f:
    f.write("Deneme textidir")
    
f.close()

#%% verilen iki listeyi sıralayıp birleştirip return et "linear merge"
    
def linear_merge(liste1, liste2):
    result = []
    while len(liste1) and len(liste2):
        if liste1[0] < liste2[0]:
            result.append(liste1.pop(0))
        else:
            result.append(liste2.pop(0))
    result.extend(liste1)
    result.extend(liste2)
    return result

#%% kelime sayma
    
def kelime_sayma_fonksiyonu(dosya_ismi):
    kelime_say_dict = {}
    
    f = open(dosya_ismi.txt, "r")
    for line in f:
        kelimeler = line.split()
        for kelime in kelimeler:
            kelime = kelime.lower() # "Ve" ile "ve" aynı sayılması için
            
            if not kelime in kelime_say_dict:   #ilk sefer için
                kelime_say_dict[kelime] = 1
            else:
                kelime_say_dict[kelime] = kelime_say_dict[kelime] + 1
    f.close()
    return kelime_say_dict

#%% En çok kullanılan 10 kelimeyi sırala
    
def kelime_yazdır(dosya_ismi):
    kelime_say = kelime_sayma_fonksiyonu(dosya_ismi) # hangi kelimenin kaç defa kullanıldığını döndürür
    kelimeler = sorted(kelime_say.keys())            # kelimeleri alfabetik olarak sıralar
                                                #kelimeler key iken kullanma sayıları value
    for kelime in kelimeler:                     # kelimeleri sıralı şekilde  print eder
        print (kelime, kelime_say[kelime])      # kelime -> kelime sayısı

def say(kelime_say_tuple):              # kelime_say daki valueleri döndürmek için SANIRIM
    return kelime_say_tuple[1]

def üste_yazdır(dosya_ismi):            # items değişkeninde kelimeleri kullanım
    kelime_say = kelime_sayma_fonksiyonu(dosya_ismi)    # sırasına göre sıralayacak.
    items = sorted(kelime_say.items(), key=say, reverse=True)
    
    for item in items[:10]:             # sıralanan listeden ilk 10 eleman yani en çok
        print (item[0], item[1])        # kullanılan 10 kelimeyi print edecek.

#%% Regular Expression örnekleri
import re        

strs = "örnek cümle:aslan !!"
es = re.search(r"cümle:\w\w\w\w\w", strs)

if es:
    print("var")
    print(es)
    es.group()
else:
    print("yok")
    
eslesme = re.search(r"iii", "iiingilizce") # eşleşme olur. eslesme.group()== "iii"
eslesme = re.search(r"iii", "inglizce")    # eşleşme olmaz ! eslesme.group() == None

eslesme = re.search(r"..g", "ping") # eşleşme olur . \ hariç her charı bulur eslesme.group() == "ing"

eslesme = re.search(r"\d\d\d", "p123g") # eslesme.group() == "123"
eslesme = re.search(r"\w\w\w", "@@abcd!!") # eslesme.group() == "abc"

#%% Regular Expression Devam --- Repetition Örnekleri

# "i+" i den sonra gelen i leri bulur

eslesme = re.search(r"pi+", "piiiing") # eslesme.group() == "piiiii"
eslesme = re.search(r"i+", "piigiiin") # eslesme.group() == "ii"

# \s* 0 ya da daha fazla boşluk arar

eslesme = re.search(r"\d\s*\d\s*\d", "xx1 2  3xx") # eslesme.group() == "1 2   3"
eslesme = re.search(r"\d\s*\d\s*\d", "xx12 3x") # eslesme.group() == "12 3"

# ^ stringin başlangıcını bulur

eslesme = re.search(r"^b\w+", "futbol") # eslesme.group() == None
eslesme = re.search(r"b\w+", "futbol") # eslesme.group() == "bol"

#%% Regular Expression Devam -- Email Örnekleri

mail = "batuhan-örnek@ornek.com"

eslesme = re.search(r"\w+@\w+", mail)
print (eslesme.group()) # match = örnek@ornek "Noktayı ve tireyi" görmedi

eslesme = re.search(r"[\w.-]+@[\w.-]+", mail)
print(eslesme.group()) # match = batuhan-örnek@ornek.com

#%% Regular Expression Devam -- GROUP EXTRACTION

mail = "batuhan-örnek@ornek.com"

eslesme = re.search(r"([\w.-]+)@([\w.-]+)", mail) #parantez ile gruplandılar
print(eslesme.group()) #tüm mail
print(eslesme.group(1)) #birinci grup
print(eslesme.group(2)) #ikinci grup

#findall

strs = "Benim adım Batuhan, soyadım Cicikler ve ben -22- yaşındayım."

satır = re.findall(r"[\w\,.-]+", strs)
for kelime in satır:
    print(kelime)
    
#%% Findall, Group Extraction with Files
    
f = open("test.txt", "r")
strings = re.findall(r"(Lorem Ipsum)", f.read())
print(strings)
for strs in strings:
    print(strs)
f.close() # Eğer grup listelemesinde parantezler de match oluyorsa
            ## o zaman parantez içindeki patternleri ?: ile başlatın
            ## örnek (?:Lorem Ipsum)
            
#%% 

import os
import sys

try:
    file = open("filename.txt", "rU")
    text = file.read()
    f.close()
except IOError:
    sys.stderr.write("problem reading: " + "filename.txt")


def List(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        path = os.path.join(dir, filename)
        print (path)
        print (os.path.abspath(path))


#%% sıralama
def sırala(liste):
    for num in range(len(liste) - 1, 0, -1):
        for i in range(num):
            if liste[i] > liste[i + 1]:
                temp = liste[i]
                liste[i] = liste[i + 1]
                liste[i + 1] = temp
    return liste

#%%
    
import numpy as np

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis = 0)

skorlar = [3.0, 1.0, 0.2]
print(softmax(skorlar))

import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
skorlar = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(skorlar).T, linewidth=2)
plt.show()

#%% atılan 2 zarın toplamlarının 7 den büyük gelme olasılığı

import numpy as np
import random

def sim(n = 100000):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        toplam = dice1 + dice2
        
        if toplam > 7:
            count += 1
    return count/n
print("atılan 2 zarın toplamlarının 7 den büyük gelme olasılığı : ", np.round(sim()*100,2), "%")

#%% 30 yeşil, 20 kırmızı, 10 beyaz top olan kutudan 5 tane top çekince
 ## çekilen topların 3 beyaz 2 kırmızı ya da hepsinin aynı renk gelme olasılığı
 
dic = {}
for i in range(60):
    if i < 10:
        dic[i] = "beyaz"
    elif i > 9 and i < 30:
        dic[i] = "kırmızı"
    else:
        dic[i] = "yeşil"
        
sart1 = 0
sart2 = 0
n = 100000

for i in range(n):
    liste = []
    for i in range(5):
        liste.append(dic[random.randint(0, 59)])
        
    liste = np.array(liste)
    
    beyaz = sum(liste == "beyaz")
    kırmızı = sum(liste == "kırmızı")
    yeşil = sum(liste == "yeşil")
    
    if beyaz == 3 and kırmızı == 2:
        sart1 += 1
        
    if (beyaz or kırmızı or yeşil) == 5:
        sart2 += 1
        
print("3 beyaz 2 kırmızı olasılığı : ", sart1 / n * 100, "%")
print("5 aynı renk olasılığı : ", sart2 / n * 100, "%")

#%%
import random

hamleler = ["taş", "kağıt", "makas", "çıkış"]

def taskagıtmakas():
    print("Taş Kağıt Makas Oyunu")
    print("Hamleler : ", hamleler)
    kullanıcı_skor = 0
    pc_skor = 0
    
    while True:
        kullanıcı = str(input("Hamleni Oyna : "))
        if kullanıcı not in hamleler:
            print("Yanlış hamle")
        else:
            if kullanıcı != "çıkış":
                pc_secim = random.choice(["taş","kağıt","makas"])
                print("Bilgisayarın hamlesi : ", pc_secim)
                
                if kullanıcı == pc_secim:
                    print("Berabere !")
                elif kullanıcı == "taş" and pc_secim == "kağıt":
                    print("Kaybettin !")
                    pc_skor += 1
                elif kullanıcı == "taş" and pc_secim == "makas":
                    print("Kazandın !")
                    kullanıcı_skor += 1
                elif kullanıcı == "kağıt" and pc_secim == "taş":
                    print("Kazandın !")
                    kullanıcı_skor += 1
                elif kullanıcı == "kağıt" and pc_secim == "makas":
                    print("Kaybettin !")
                    pc_skor += 1
                elif kullanıcı == "makas" and pc_secim == "kağıt":
                    print("Kazandın !")
                    kullanıcı_skor += 1
                elif kullanıcı == "makas" and pc_secim == "taş":
                    print("Kaybettin !")
                    pc_skor += 1
                else:
                    pass
            else:
                print("{} defa kazandın, {} defa kaybettin" .format(kullanıcı_skor, pc_skor))
                break
    
taskagıtmakas()

            
            
            
            
    
    
    
    







