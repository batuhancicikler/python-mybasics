# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 18:43:10 2019

@author: batuhan
"""

#%% project euler problem 3... Tam anlamadım, geri dönücem
def largest_prime_fact(n):
    i = 2
    while i * i < n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
                
#%% en büyük 3 basamaklı iki sayının çarpımından oluşan palindrome sayısı
    
def palindromemi(num):                  # sayı tersten de eşit mi diye kontrol ediyor.
    return str(num) == str(num)[::-1]

def enbüyük(a, b):
    c = 0
    for i in range(b, a, -1):           #en büyük rakamı alıp en düşüğe doğru inerken çarpımlarıyla
        for j in range(b, a, -1):       #çıkan rakamın palindrome mi olduğunu kontrol eder
            if palindromemi(i*j):       # en büyüğünü de c nin içinde tutar
                if i*j > c:
                    c = i*j    
    return c

print (enbüyük(100, 999))

#%% 1-20 arasıdaki sayılara eşit şekilde bölünebilen en küçük sayı

def enkücükBöl(n):
    s = False
    while s == False:
        bölenler = [x for x in range(1,21)]
        tümbölenler = zip(n % i for i in bölenler) # n'i bölen tüm 1-20 arasındaki sayılarla eşleştiriyor
        liste = all(item[0] == 0 for item in tümbölenler) # n % i deki tüm değerlerin 0 a eşit olduğuna bakıyor
        if liste:
            s = True
            return n
        else:
            n += 1
            
#%% n.(n'inci) Asal sayı
            
import math

def asal(n):
    asal_sayı = int(2 * n * math.log(n))        
    sieve = ([True] * asal_sayı)                # tüm N leri asal say
    count = 0
    for i in range(2, asal_sayı):
        if sieve[i]:                            # hala asal mı? (true mi?)
            count += 1                          
            if count == n:
                return i
            for j in range(2 * i, asal_sayı, i):    # i nin karelerinden kurtul
                sieve[j] = False
    return count