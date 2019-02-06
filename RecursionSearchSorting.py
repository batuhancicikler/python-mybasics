# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 20:30:00 2019

@author: batuhan

A recursive algorithm must have a base case.
A recursive algorithm must change its state and move toward the base case.
A recursive algorithm must call itself, recursively.
"""
#%% rekürsif liste elemanları toplama
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


def sumList(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        return liste[0] + sumList(liste[1:])
print(sumList([5,3,2,4,6]))

    ## rekursif integer in tabanını string yazdırma
    
def toStr(num, base):
    convertToStr = "0123456789ABCDEF"
    if num < base:
        return convertToStr[num]
    else:
        return toStr(num//base, base) + convertToStr[num%base]
print(toStr(2256, 16))

rStack = Stack()
def toStr2(n, b):
    convert = "0123456789ABCDEF"
    
    while n > 0:
        if n < b:
            rStack.push(convert[n])
        else:
            rStack.push(convert[n % b])
        n = n // b
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

print(toStr2(2256, 16))

#%% sierpinski triangle with turtle

    
def drawTriangle(noktalar, renk, myTurtle):
    myTurtle.fillcolor(renk)
    myTurtle.up()
    myTurtle.goto(noktalar[0][0], noktalar[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(noktalar[1][0],noktalar[1][1])
    myTurtle.goto(noktalar[2][0],noktalar[2][1])
    myTurtle.goto(noktalar[0][0],noktalar[0][1])
    myTurtle.end_fill()
    
def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(noktalar, açı, myTurtle):
    liste = ["red", "blue", "yellow", "orange", "violet"]
    drawTriangle(noktalar, liste[açı], myTurtle)
    if açı > 0:
        sierpinski([noktalar[0],
                   getMid(noktalar[0], noktalar[1]),
                   getMid(noktalar[0], noktalar[2])],
                    açı - 1, myTurtle)
        sierpinski([noktalar[1],
                   getMid(noktalar[0], noktalar[1]),
                   getMid(noktalar[1], noktalar[2])],
                    açı - 1, myTurtle)
        sierpinski([noktalar[2],
                   getMid(noktalar[2], noktalar[1]),
                   getMid(noktalar[0], noktalar[2])],
                    açı - 1, myTurtle)
    
def main():
    import turtle as myTurtle
    myWin = myTurtle.Screen()
    myPoints = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(myPoints, 3, myTurtle)
    myWin.exitonclick()
    
main()
    
#%% tower of hanoi
"""
    
        |             |             |
    from pole --- with pole --- to pole
    1.tower height - 1 kadar ortadaki cubuğa final çubuğu kullanarak git
    2.kalan diskleri final çubuğuna koy
    3.tower height - 1 kadar ortadaki çubuktan final çubuğuna kadar orijinal çubuğu kullanarak git    
"""
def tower(height, fromTower, toTower, withTower):
    if height >= 1:
        tower(height - 1, fromTower, withTower, toTower)
        disk(fromTower, toTower)
        tower(height - 1, withTower, toTower, fromTower)
        
def disk(fp, tp):
    print("From", fp, "'To", tp)
    
tower(3, "A", "B", "C")


#%% Dynamic programming with recursion, greedy algorithm, 63 cents problem
"""
    fonksiyonun sonuca ulaşması aşağı yukarı 30 saniye sürücek
    çünkü her değer için 2-4 graph düğümü her düğüm için ise bir başka düğüm
    oluşturup sonra minMoney i hesaplamak greedy algorithm in dezavantajı
"""

def recur(currency, change):
    minMoney = change
    if change in currency:
        return 1
    else:
        for i in [x for x in currency if x <= change]:
            num = 1 + recur(currency, change - i)
            if num < minMoney:
                minMoney = num
    return minMoney

#print(recur([1,5,10,20], 63) #67 milyon tane rekürsif adım oluşturuyor

"""
bu kadar uzun sürmemesi için zaten önceden bulunan düğümleri tekrar bulmak yerine
onları atlayabiliriz..
"""

def recur2(currency, change, bilinen):
    minim = change
    if change in currency:
        bilinen[change] = 1
        return 1
    elif bilinen[change] > 0:
        return bilinen[change]
    else:
        for i in [c for c in currency if c <= change]:
            num = 1 + recur2(currency, change - i, bilinen)
            
            if num > minim:
                minim = num
                bilinen[change] = minim
    return minim

#print(recur2([1,5,10,20], 63, [0] * 63))  # 221 tane rekürsif adım oluşturuyor
"""
    Yine de bu 2 yaklaşım dinamik açıdan sistematik değil, onun yerine 3 adımlı
    bir algoritma daha uygun olcaktır.
    I. 11 - 1 = 10 (1 change) 1 change + minimum kadar coins
   II. 11 - 5 = 6 (5, 1; 2 change)
  III. 11 - 10 = 1 (1 change)
"""
def recur3(currency, change, minim, kullanılan):
    for para in range(change + 1):
        paraCount = para
        yeniPara = 1                # son kullanılan paraları tutarak "kullanılan" içinden print etmek için
        for j in [c for c in currency if c <= para]:
            if minim[para - j] + 1 < paraCount:
                paraCount = minim[para - j] + 1
                yeniPara = j
        minim[para] = paraCount
        kullanılan[para] = yeniPara
    return minim[para]
    
def printPara(kullanılan, change):
    para = change
    while para > 0:
        buPara = kullanılan[para]
        print(buPara)
        para = para - buPara
        
def main():
    amount = 63
    currency = [1,5,10,20]
    kullanılan = [0] * (amount + 1)
    paraCount = [0] * (amount + 1)
    
    print("verilen nakit : ", amount)
    print(recur3(currency, amount, paraCount, kullanılan, "en az adet bozukluk olabilir"))
    print("Bozukluklar : ")
    print(printPara(kullanılan, amount))
    print("kullanılan para listesi : ")
    print(kullanılan)
    
main()

#%%

def fact(n):
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)
    
liste = [5,3,2,0,-5]

def rev(l):
    """
        önce listenin son elemanını + son eleman hariç gerisinin fonksiyon halini birlikte al
    """
    if not l: return []
    return [l[-1]] + rev(l[:-1])
        
    
def triangle(n, lol=None):
    if lol is None: lol = [[1]]
    if n == 1:
        return lol
    else:
        prev_row = lol[-1]
        new_row = [1] + [sum(i) for i in zip(prev_row, prev_row[1:])] + [1]
        return triangle(n - 1, lol + [new_row])
    
#%% Sequential Search
        
## index sıralı şeklinde sıralanmış listelerden bir elemanı aramak senquential searcha örnek
        
def seqSearch(liste, item):
    pos = 0                 #index numarasını temsil ediyor
    found = False
    while pos < len(liste) and not found:
        if liste[pos] == item:
            found = True
        else:
            pos += 1
    return found

test = [1,5,2,6,4,"batu"]
print("sequential(ardışık) search : ",seqSearch(test, 5))
print("sequential(ardışık) search : ",seqSearch(test, "batu"))
print("sequential(ardışık) search : ",seqSearch(test, 55))

"""
    Ancak liste sıralı bir şekilde olursa mesela [1,2,3,5,6] ve biz 4 ü aratmak istersek tüm elemanlara bakmak
    mantıksız, o yüzden eğer aradığımız eleman o sıradaki elemandan küçük ise kodu durdurmamızda fayda var
"""

def orderedseqSearch(liste, item):
    pos = 0         # index numarası
    found = False
    stop = False
    while pos < len(liste) and not found and not stop:
        if liste[pos] == item:
            found = True
        else:
            if liste[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found
test2 = [2,3,6,7,15,28,33,52,53,55]
print("ordered(sıralı) sequential(ardışık) search : ",orderedseqSearch(test2, 14))
print("ordered(sıralı) sequential(ardışık) search : ",orderedseqSearch(test2, 33))

"""
    listede n kadar eleman olduğu için her ne kadar O(n/2) gibi görünsede O(n) olduğunu
    unutma.
    listeden bir elemanı ararken ilk elemana baktığında geriye n-1 kadar eleman kalıyor.
    Tüm elemanlara bakmak yerine Binary Search yapmak daha mantıklı, ortadaki iteme bakılır,
    eğer aradığımız item o ise kod biter eğer o itemden büyük ise kalan yarıma bakabiliriz.
"""
#%% Binary Search

"""
    listeden bir elemanı ararken ilk elemana baktığında geriye n-1 kadar eleman kalıyor.
    Tüm elemanlara bakmak yerine Binary Search yapmak daha mantıklı, ortadaki iteme bakılır,
    eğer aradığımız item o ise kod biter eğer o itemden büyük ise kalan yarıma bakabiliriz.
    
    liste = [1,2,3,4,5,6,7,8,9,10] 6 yı ararken ortası 5 olarak alırız, 6>5 olduğu için
    bir sonraki ortayı 7 olarak alırız 6<7 olduğu için ordan da 6 ya ulaşırız.
    
    böylece karşılaştırmak için kalan eleman sayısı n/2, n/4, n/8... şeklinde gider
"""

def binarySearch(liste, item):
    if len(liste) <= 1:
        if liste[0] == item:
            return True
        else:
            return False
    else:
        orta = len(liste) // 2
        if liste[orta] == item:
            return True
        else:
            if item < liste[orta]:
                return binarySearch(liste[:orta], item)
            else:
                return binarySearch(liste[orta:], item)

liste = [1,2,3,4,5,6]
print("binary search 1 : ", binarySearch(liste, 1))
print("binary search 4 : ", binarySearch(liste, 4))
print("binary search 3 : ", binarySearch(liste, 3))
print("binary search 10 : ", binarySearch(liste, 10))
print("binary search 7 : ", binarySearch(liste, 7))
print("binary search 5 : ", binarySearch(liste, 5))
print("binary search 2 : ", binarySearch(liste, 2))
print("binary search 6 : ", binarySearch(liste, 6))

#%% Hashing

def hashing(strs, tablesize):
    toplam = 0
    for i in range(len(strs)):
        toplam = toplam + ord(strs[i])
    return toplam % tablesize

"""
    put -> yeni value ekler, eğer key de value var ise üstüne yazar
    get -> key deki value yi return eder
    del -> kel-value çiftini siler kullanımı : map del[key]
    len() -> map ta store edilen key-value çiftlerinin sayısını return eder
    in -> key in map ise True döner değil ise False
"""

class HashTable():
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def push(self, key, data):
        hashvalue = self.hashfonksiyon(key, len(self.slots)) # girilen değer % table size işlemini
                                                                # hashvalue(index) değerine atamak
        if self.slots[hashvalue] == None:         # hashvalue boş ise key ve data yerleştirilir
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:                                   
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:                               #hashvalue boş değil ise ve key de bizim belirlediğimizden
                nextslot = self.rehash(hashvalue, len(self.slots)) # farklı ise;
                while self.slots[nextslot] != None and self.slots[nextslot] != key: #(hashvalue + 1) % 11
                    nextslot = self.rehash(nextslot, len(self.slots)) #ile yeni bir hash değeri
                #döndürürüz, eğer yeni hash değeri de boş değil ve key farklıysa aynı işlemi yeniden yaparız
                if self.slots[nextslot] == None: # ykarıda elde ettiğimiz nextslot indexi boş mu ?
                    self.slots[nextslot] = key  # boş ise data ve keyi oraya yerleştir.
                    self.data[nextslot] = data
                else:                           # boş değil ise datayı yerleştir
                    self.data[nextslot] = data 
                    
    def hashfonksiyon(self, key, size):
        return key%size
        
    def rehash(self, oldhash, size):
        return (oldhash + 1)%size
    
    def get(self, key):
        startslot = self.hashfonksiyon(key, len(self.slots))
        
        data = None
        stop = False
        found = False
        pos = startslot
        
        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos, len(self.slots))
                if pos == startslot:
                    stop = True
        return data
                        # getitem ve setitem ile dictlerde çalıştığımız gibi [] ile veri ekleyebilceğiz 
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, data):
        self.push(key, data)
    
h = HashTable()
h[54] = "cat"   # key --- value 54 kısmı push methodunun keyi iken "cat" ise valuesi
h[12] = "batuhan"
h[56] = "dog"
print("slots : ", h.slots)
print("data : ", h.data)
print("get : ", h[56])
        

#%% Levenshtein distance -- iki string arasındaki fark bir cümleyi diğeri ile
    # aynı yapana kadar yapman gereken silme, ekleme, değiştirmeler ile belirlenir
    
    
"""
    cat ile chello arasındaki farkın algoritması
    cat, cht(a ile h değişti), che(t ile e değişti), chel (l eklendi),
    chell (l eklendi), chello (o eklendi)
"""

def levenshtein(a, b):
    if not a: return len(b) #string a boş ise minimum distance b kadardır
    if not b: return len(a) #string b boş ise minimum distance a kadardır
    
    # ikiside boş değil ise; başlangıç karakterlerini boş verip
    # rekürsif bir şekilde a[1:] ile b[1:] arasındaki mesafe hesaplanır
    
    #eğer ilk karakterler farklıysa a[0] ı b[0] ile değiştiririz.
    
    #ardından ilk karakter a[0] ı çıkartır, minimal distanceyi rekürsif bi şekilde hesaplarız
    #a[0] ı kaldırdığımız için sonucu 1 arttırmamız gerek
    
    #sonra ise b[0] ı a nın başına insert etmemizgerekiyor ve b nin ilk karakterini
    #kaldırarak problemi küçültürüz
    return min(levenshtein(a[1:], b[1:]) + (a[0] != b[0]),
    levenshtein(a[1:], b) + 1,
    levenshtein(a, b[1:]) + 1)
    
    #minimal distanceyi almış bulunuk. İlk karakterin yerini değiştir, ilk karakteri kaldır, ilk karakteri ekle

print(levenshtein("batugg5", "batafew23"))
    
    
    

    





    
    




