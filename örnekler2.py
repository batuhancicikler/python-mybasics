# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:36:50 2019

@author: batuhan
"""
#%%
def hesap(girdi):
    
    
    try:
        girdi = eval(girdi)
    except ZeroDivisionError:
        print("0 a bölünemez")
    except NameError:
        print("Geçersiz girdi")
    except AttributeError:
        print("Yanlış kullanım")
    except TypeError:
        print("Yanlış type kullandınız")
    return girdi

def sonuc(girdi):
    
    print("\n"+ str(hesap(girdi)))
    
def main():
    print("Hesap Makinesi\nKullanım şekli: 5 + 5 / 2 * 10\n"
          "Çıkmak için : çıkış yazın")
    
    while True:
        x = input("\nİşlem : ")
        if x == "çıkış": break
        sonuc(x)
    
if __name__ == "__main__": main()

#%%
import time

print("Başlatmak için ENTER, Durdurmak için CTRL + C")

while True:
    try:
        input()
        starttime = time.time()
        print("başladı")
        while True:
            print("Süre : ", round(time.time() - starttime,0), "saniye", end="\n")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Durdu")
        endtime=time.time()
        print("Geçen süre : ", round(endtime - starttime,2), "saniye")
        break
#%% En Büyüğü/Küçüğü Bul
        
def maks(sayı):
    en_büyük = sayı[0]
    for i in sayı:
        if i > en_büyük:
            en_büyük = i
    return en_büyük

def minm(sayı):
    en_küçük = sayı[0]
    for i in sayı:
        if i < en_küçük:
            en_küçük = i
    return en_küçük

#%% Mutlak Sayı, Mutlak sayısı Max ve Min olanlar
    
def mutlak(sayı):
    if sayı < 0:
        sayı = sayı * -1
    else:
        return sayı
    return sayı
    
def absMax(sayı):
    en_büyük = sayı[0]
    
    for i in sayı:
        if mutlak(i) > mutlak(en_büyük):
            en_büyük = i
    return mutlak(en_büyük)
    
def absMin(sayı):
    en_küçük = sayı[0]
    
    for i in sayı:
        if mutlak(i) < mutlak(en_küçük):
            en_küçük = i
    return mutlak(en_küçük)

#%% Ortalama
    
def ort(sayılar):
    toplam = sum(sayılar)
    bolen = len(sayılar)
    return (toplam/bolen)

#%% obeb ve okek
    
def obeb(sayı1, sayı2):
    if sayı1 == 0:
        return sayı2
    if sayı2 == 0:
        return sayı1
    if sayı1 == sayı2:
        return sayı1
    if sayı1 > sayı2:
        return obeb(sayı1 - sayı2, sayı2)
    else:
        return obeb(sayı1, sayı2 - sayı1)

def okek(sayı1, sayı2):
    return ((sayı1 * sayı2) / obeb(sayı1, sayı2))

def okek2(sayı1, sayı2):
    maxim = sayı1 if sayı1 > sayı2 else sayı2
    ortakkat = maxim
    while True:
        if ((ortakkat % sayı1 == 0) and (ortakkat % sayı2 == 0)):
            break
        ortakkat += maxim
    return ortakkat

#%% Fibonacci dizisinin algoritması
    
# 01123581321345589...
    
def fibo(x):
    start = 0
    print(start)
    start2 = 1
    print(start2)
    for i in range(0,x): 
        fibb = start + start2
        print (fibb)
        start = start2
        start2 = fibb
    return fibb

def fibo2(n):   #basamak olarrak
    a, b = 0, 1
    while len(str(a)) < n:
        print(a, end=" ")
        a, b = b, a + b
    return a

#%% Algoritma Analizleri
    
import time

def sumOf(n):
    start = time.time()
    theSum = 0
    for i in range(0,n + 1):
        theSum += i
    end = time.time()
    
    return theSum, end - start

def sumOf2(n):
    start = time.time()
    toplam = (n * (n + 1)) / 2
    end = time.time()
    
    return toplam, end - start

print("Sum1 %d zamanı da %10.7f saniye" %(sumOf(1000000)))
print("Sum2 %d zamanı da %10.7f saniye" %(sumOf2(1000000)))

#%% Kart oyunu

from enum import Enum
from enum import IntEnum
from random import *


full_deste = []
gecici_deste = []
player_kart = []
player2_kart = []

    # kart enum u, deste için
class Kart(IntEnum):
    İKİ = 2
    ÜÇ = 3
    DÖRT = 4
    BEŞ = 5
    ALTI = 6
    YEDİ = 7
    SEKİZ = 8
    DOKUZ = 9
    ON = 10
    JOKER = 11
    KIZ = 12
    KRAL = 13
    AS = 14

    # suit enum u
class Suit(Enum):
    MAÇALAR = "maçalar"
    SİNEKLER = "sinekler"
    KUPALAR = "kupalar"
    KAROLAR = "karolar"
    

    # kart oyunu için bilgi tutacak class
class KartOyunu:
    def __init__(self, kart_value, kart_suit):
        self.kart = kart_value
        self.suit = kart_suit
        
        # tüm deste kartlarıyla ilgilenmesi için gerekli fonksiyon
def deste_olustur():
    for suit in Suit:
        for kart in Kart:
            full_deste.append(KartOyunu(Kart(kart), Suit(suit)))
    return full_deste
    

    # desteden tek kart çekme
def draw_kart(deste):
    rand_kart = randint(0, len(deste) - 1)
    return deste.pop(rand_kart)     # çekilen kartı return edip, desteden çıkartıyor
    
        
    # oyuncuların destelerine, geçici desteden kağıtları dağıtıyor
def halfdeal():
    while(len(gecici_deste) > 0):
        player_kart.append(draw_kart(gecici_deste))
        player2_kart.append(draw_kart(gecici_deste))

deste_olustur()
gecici_deste = list(full_deste)
halfdeal()

for i in range(0, len(player_kart)):
    if(player_kart[i].kart > player2_kart[i].kart):
        print("Player 1 eli kazandı !", player_kart[i].kart)
        print("Player 2 eli kaybetti !", player2_kart[i].kart)
        
    if(player2_kart[i].kart > player_kart[i].kart):
        print("Player 2 eli kazandı !", player2_kart[i].kart)
        print("Player 1 eli kaybetti !", player_kart[i].kart)
    else:
        print("Kazanan Yok")
        
#%%     Big-O Notation ---- O(n^2)

import time
from random import randrange

def findMin(liste):
    minim = liste[0]
    for i in liste:
        en_kücük = True
        for j in liste:
            if i > j:
                en_kücük = False
        if en_kücük:
            minim = i
    return minim

#mylist = [2,1,5,4,8,6,2,0]
#print(findMin(mylist))

for listSize in range(1000, 10001, 1000):
    liste = [randrange(100000) for x in range (listSize)]
    start = time.time()
    print(findMin(liste))
    end = time.time()
    print("%d size, time %f" %(listSize, end - start))
    
    """
        69
        1000 size, time 0.065962
        10
        2000 size, time 0.266887
        30
        3000 size, time 0.612190
        0
        4000 size, time 1.100937
        13
        5000 size, time 1.654031
        11
        6000 size, time 2.375903
        3
        7000 size, time 3.227387
    """
#%% Big-O Notation       
def findMin2(liste2):
    minim = liste2[0]
    for i in liste2:
        if i < minim:
            minim = i
    return minim

for listSize in range(1000, 10001, 1000):
    liste2 = [randrange(100000) for x in range (listSize)]
    start = time.time()
    print(findMin2(liste2))
    end = time.time()
    print("%d size, time %f" %(listSize, end - start))
    
    """
        254
        1000 size, time 0.000998
        60
        2000 size, time 0.000000
        12
        3000 size, time 0.000998
        176
        4000 size, time 0.001003
        7
        5000 size, time 0.000000
        15
        6000 size, time 0.000000
        27
        7000 size, time 0.001091
    """
    
#%% Anagram string check
    
"""
        Bu çözüm tamamen O(n^2) dir. s1 tüm s2 lere bakar sonra bir sonraki s1 elemanıyla
        baştan başlar. Eğer string çok uzun olursa kodun çalışma süresi artacaktır.
"""
    
def anagramCheck(s1, s2):
    liste = list(s2)
    check = True
    pos = 0
    
    # s1 in 0 ıncı elemanını, aynısını bulana kadar s2 nin tüm elemanlarıyla kıyaslar
    
    while pos < len(s1) and check:
        pos2 = 0
        buldu = False
        while pos2 < len(liste) and not buldu:
            if s1[pos] == liste[pos2]:
                buldu = True
            else:
                pos2 = pos2 + 1
                
        # eğer s1 in elemanlarından birisi listedekiyle eşleşirse listedeki eşleyen elemanı None yapar
        if buldu:
            liste[pos2] = None
        else:
            check = False
            
        pos = pos + 1
        
    return check
        
print("\nİlk anagram fonksiyonu : ", anagramCheck("batu", "abtu"))

"""
        Çözüm 2; Sort and Compare... s1 ve s2 leri kıyaslamaksızın alfabetik olarak sıralarsak
        eğer uzunlukları ve elemanları eşit ise anagramdır. Ancak sort methodu
        kullanmak ta bir bakıma O(n^2) ya da O(n log n) dir. Yani çözüm 1 ve çözüm 2
        nin de order of magnitute si aynıdır.
"""

def anagramCheck2(s1, s2):
    liste1 = list(s1)
    liste2 = list(s2)
    
    liste1.sort()
    liste2.sort()
    
    pos = 0
    eslesme = True
    
    while pos < len(s1) and eslesme:
        if liste1[pos] == liste2[pos]:
            pos = pos + 1
        else:
            eslesme = False
            
    return eslesme
    
print("\nİkinci anagram fonksiyonu : ", anagramCheck2("batu", "abtu"))
    
"""
        Çözüm 3; Count and Compare... Bu yöntemde anagram olup olmadıklarını
        karşılaştırmak için a ları b leri c lerin aynı sayıda olup olmadığını kontrol eder.
        türkçe de 29 harf olduğu için c1 ve c2 29 elemanlı listeler olarak hazırlanır.
        
        stringleri check etmek dışında sadece 29 adım atıyor, bu yüzden O(n) yani linear diyebiliriz.
"""

def anagramCheck3(s1, s2):
    
    c1 = [0] * 29
    c2 = [0] * 29
    
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")     # s1 in i elemanının unicodesi - "a" nın unicodesi, yani 
        c1[pos] = c1[pos] + 1           # s1[i] ile a eşit ise pos 0 olacak
        
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1
        
    j = 0
    check = True
    
    while j < 29 and check:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            check = False
            
    return check

print("\nÜçüncü anagram fonksiyonu : ", anagramCheck3("batu", "abtu"))

#%% List Time Analysis



def test1():
    liste = []
    for i in range(1000):
        liste = liste + [i]
        
def test2():
    liste = []
    for i in range(1000):
        liste.append(i)
        
def test3():
    liste = [i for i in range(1000)]
    
def test4():
    liste = list(range(1000))
    
import timeit
    
Timer = timeit.Timer

print("\n")
t1 = Timer("test1()", "from __main__ import test1")
print("concat", t1.timeit(number=1000), "milisaniye")

t2 = Timer("test2()", "from __main__ import test2")
print("append", t2.timeit(number=1000), "milisaniye")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension", t3.timeit(number=1000), "milisaniye")

t4 = Timer("test4()", "from __main__ import test4")
print("list range", t4.timeit(number=1000), "milisaniye")
    
print("\n")
print("*" * 50)
print("\n")
    
popzero = Timer("x.pop(0)", "from __main__ import x")
popend = Timer("x.pop()", "from __main__ import x")

x = list(range(200000))
print("x.pop(0) : ", popzero.timeit(number=1000))
print("x.pop() : ", popend.timeit(number=1000))























