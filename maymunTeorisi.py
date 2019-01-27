# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:31:39 2019

@author: batuhan
"""
#%%
import random

def gen(uzunluk):
    alfabe = "abcçdefghıijklmnoöprsştuüvyz "
    per = ""
    for i in range(uzunluk):
        per = per + alfabe[random.randrange(29)] #alfabe içindeki elemanlardan (boşluk dahil) random seçer
    return per

def skor(hedef, test):
    aynı = 0
    for i in range(len(hedef)): 
        if hedef[i] == test[i]: # denk gelmesini istediğimiz kelimenin, algoritmanın yazdığı rastgele kelime
            aynı = aynı + 1     # içinde kaç harfi denk geliyorsa onu sayıyor.
    return aynı / len(hedef)    # batuhan 7 harfliyse bat olduğu zaman 3/7 oranında doğru bilmiş oluyor.

#main içinde algoritmayı, istenilen kelimeyi verene kadar çalıştırdık
def main():
    hedefstr = "batuhan"
    yenistr = gen(50)   # gen fonksiyonunu 50 harflik randomlar şeklinde çalıştırıyoruz.
    skorr2 = 0          # istediğimiz hedefe ne kadar yaklaştığımızı tutacak.
    bestskor = skor(hedefstr, yenistr) # sürekli skor fonksiyonunu tutucak ve döngüyü onun üzerine kurucaz
    while bestskor < 1:
        if bestskor >= skorr2:
            print (bestskor, yenistr)
            skorr2 = bestskor
        yenistr = gen(50)
        bestskor = skor(hedefstr, yenistr)
        
main()