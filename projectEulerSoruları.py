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

from functools import reduce

def okek(*values):
    values = [value for value in values]
    if values:
        n = max(values)
        m = n
        values.remove(n)
        while any(n % value for value in values):
            n += m
        return n
    return 0

print(reduce(okek, range(1,21)))
            
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

#%% sum square difference
    
def squaresumOf(n = 10):
    square = []
    sqtoplam, sumtoplam = 0, 0
    for i in range(1, n + 1):
        square.append(i * i)
        
    for x in range(1, n + 1):
        sumtoplam = sumtoplam + x
    
    for j in square:
        sqtoplam = sqtoplam + j
        
    sumtopkare = sumtoplam * sumtoplam
    
    print("Toplamların karesi : ", sumtopkare)
    print("Karelerinin toplamları : ", sqtoplam)
    print("Aralarındaki fark : ", sumtopkare - sqtoplam)

#%% sum square difference (DAHA BASİT)
    
def sumsquare(n):
    top = 0
    kareTop = 0
    for i in range(1, n + 1):
        top += i                   # top toplamları tutarken, kareTop ise karelerin toplamlarını tutuyor
        kareTop += i**2
    
    fark = top**2 - kareTop         # Burada toplamların karesini alıp (top**2) daha sonra kareTop dan çıkartıyoruz
    return fark

#%% Largest product in a series 13 digit, Tam anlamadım geri dönücem
    
veri = list("\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450")

print("Başlangıc basamağı : ",len(veri))
liste = list()

while True:
    x = list(veri[0:13])
    carpım = 1
    for i in x:
        carpım *= int(i)
    liste.append(carpım)
    veri.pop(0)
    
    if len(veri) == 12:
        break
    
print("En büyük çarpım : ", max(liste))
print("Bitince kalan basamak sayısı : ", len(veri))

#%% 1000 basamaklı fibonacci sayısının indexi

def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        
for index, num in enumerate(fibo()):
    if len(str(num)) == 1000:
        print(index)
        break
    
#%% 100 sayısının faktoriyelindeki rakamların toplamı

def factoriyel(n):
    fact = 1
    sumFac = 0
    for i in range(1,n + 1):
        fact = fact * i
    for j in str(fact):
        sumFac = sumFac + int(j)
    return sumFac
        
## YAA DAAA
    
def euler20(n):
    sayac = 1
    for i in range(2, n + 1):
        sayac *= i
    sayac = sum(map(int, str(sayac)))
    return sayac


















        
        
        
        





