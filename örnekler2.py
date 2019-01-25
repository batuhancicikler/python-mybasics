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
    
def fibo():
    start = 0
    print(start)
    start2 = 1
    print(start2)
    for i in range(0,10): #range kadar basamağı getiricek
        fibb = start + start2
        print (fibb)
        start = start2
        start2 = fibb
    return fibb

#%%








