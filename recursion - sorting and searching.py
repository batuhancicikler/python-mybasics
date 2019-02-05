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
print(seqSearch(test, 5))
print(seqSearch(test, "batu"))
print(seqSearch(test, 55))

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
    
    
    

    





    
    




