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

#%% List - Dict compare

import random

for i in range(1000, 10001, 2000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random,x")
    
    x = list(range(i))
    lst_time = t.timeit(number = 1000)
    
    x = {j : None for j in range(i)}
    d_time = t.timeit(number=1000)
    
    print("Number   Liste Süresi  Dict Süresi")
    print("%d,    %f,     %f" % (i, lst_time, d_time))

#%% Stack örnekleri  

class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        #self.items.append(item)
        self.items.insert(0, item)
        
    def pop(self):
        #return self.items.pop()
        return self.items.pop(0)
    
    def peek(self):
        #return self.items[len(self.items) - 1]
        return self.items[0]
    
    def size(self):
        return len(self.items) 
    
    def reverse(self):
        reversedlist = []
        while not self.isEmpty():
            reversedlist.append(self.items.pop(0))
        return reversedlist        

s = Stack()
print("is empty : ", s.isEmpty())
s.push(4)
s.push("Dog")
print("peek : ", s.peek())
print("pop : ", s.pop())
print("size : ", s.size())
print("is empty : ", s.isEmpty())
s.push("Batuhan")
s.push(22)
print("reversed : ", s.reverse())



def reversemyStr(myStr):
    yeni_stack = Stack()
    for char in myStr:
        yeni_stack.push(char)
    revstr = ""
    while not yeni_stack.isEmpty():
        revstr = revstr + yeni_stack.pop()
    return revstr

def parantezDenge(parantez):
    a = Stack()
    denge = True
    index = 0
    while index < len(parantez) and denge:
        sembol = parantez[index]
        if sembol in "({[":
            a.push(sembol)
        else:
            if a.isEmpty():
                denge = False
            else:
                top = a.pop()
                if not matches(top, sembol):
                    denge = False
        index = index + 1
        
    if denge and a.isEmpty():
        return True
    else:
        return False

def matches(openp, closep):     # Boolean döndürür
    opens = "([{"
    closes = ")]}"
    return opens.index(openp) == closes.index(closep)

print("Parantez ", parantezDenge("(()(()())())"))
print("Parantez ", parantezDenge("{[(())]"))
print("Parantez ", parantezDenge("(()"))
print("Parantez ", parantezDenge("()()())))"))
print("Parantez ", parantezDenge("([{()}])"))



def convertTo(num, base):
    binn = Stack()
    while num > 0:
        binn.push(num % base)
        num = num // base
    
    binString = ""
    while not binn.isEmpty():
        binString = binString + str(binn.pop())
    return binString
    
print("Convert To ", convertTo(233, 2))  
    
   ### Infix to Postfix ###

"""
    --> önce operatörleri (+-*/) tutması için Stack ve çıktı için boş bir liste oluştur.
    --> input infix i split kullnarak listeye çevir (semboller)
    --> listeyi(semboller) soldan sağa sembol olarak tara
            -> eğer sembol operand{x + y: (x,y)} ise çıktı listesinin en sonuna yolla
            -> eğer sembol sol parantez ise stack e push et
            -> eğer sembol sağ parantez ise sol parantez stack den çıkana kadar pop yap ve
               öperatörleri listenin sonuna ekle 
                (bu işlemde pop u bir değişkene eşitleyerek takip ediyor)
            -> eğer sembol (+-*/) ise {yani kodun else kısmı}, önce stackte var olan eşit
                ya da büyük önceliği olan(prec) sembolleri pop et stack boşaldığı zaman (+-*/) ları ekle
                ve çıktı listesine ekle.
    --> input tamamen işlendikten sonra stack ı kontrol et, eğer herhangi bir operatör hala duruyorsa
        append(pop) ile listenin sonuna ekle
"""


def infixtoPostfix(expr):
    prec = {}
    prec["**"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixListe = []
    semboller = expr.split()
    
    for sembol in semboller:
        if sembol in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or sembol in "0123456789":
            postfixListe.append(sembol)
        elif sembol == "(":
            opStack.push(sembol)
        elif sembol == ")":
            sonSembol = opStack.pop()
            while sonSembol != "(":
                postfixListe.append(sonSembol)
                sonSembol = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[sembol]):
                postfixListe.append(opStack.pop())
            opStack.push(sembol)
    while not opStack.isEmpty():
        postfixListe.append(opStack.pop())
    return " ".join(postfixListe)

print("Infix to Postfix", infixtoPostfix("( ( A + B ) * C ) / D"))
print("Infix to Postfix", infixtoPostfix("A * B + ( C / D )"))
print("Infix to Postfix", infixtoPostfix("9 + 3 * 5 / ( 6 - 4 )"))

    ### postfix üzerinden işlem yapma ###
    
"""
    --> Boş bir stack oluştur
    --> split ile input u listeye çevir
    --> soldan sağa sembolleri kontrol et
        -> eğer sembol rakam ise; string den int e çevir, değeri stack e pushla
        -> eğer sembol operatör ise; 2 tane rakam(operand) için stackten 2 tane popla,
            aritmatik işlemi pop-operatör sembol-pop arasında yap ve sonucu stack e geri pushla
    --> 
"""

def postfixEval(expr):
    evalStack = Stack()
    tokens = expr.split()
    
    for token in tokens:
        if token in "0123456789":
            evalStack.push(int(token))
        else:
            sayı1 = evalStack.pop()
            sayı2 = evalStack.pop()
            sonuc = islem(token, sayı1, sayı2)
            evalStack.push(sonuc)
            
    return evalStack.pop()

def islem(operator, operand1, operand2):
    if operator == "*":
        return operand1 * operand2
    
    if operator == "+":
        return operand1 + operand2
    
    if operator == "-":
        return operand1 -   operand2
    
    else:
        return operand1 / operand2

print("Postfix Eval : ", postfixEval("7 8 + 3 2 + /"))
            










