# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 01:43:05 2019

@author: batuhan
"""

def obeb(a, b):
        while a%b != 0:
            olda = a
            oldb = b
            
            a = oldb
            b = olda % oldb
        return b

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self):                              #print için method
        return str(self.num)+"/"+str(self.den)
        
    def show(self):
        print(self.num, "/", self.den)              #print harici göstermek için. artık gereksiz
    
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den
    
    def __add__(self, other):                       # Toplama
        yeninum = self.num * other.den + self.den * other.num
        yeniden = self.den * other.den
        
        lowest = obeb(yeninum, yeniden)
        
        return Fraction(yeninum//lowest, yeniden//lowest)
    
    def __sub__(self, other):                       #çıkartma
        yeninum = self.num * other.den - self.den * other.num
        yeniden = self.den * other.den
        
        lowest = obeb(yeninum, yeniden)
        
        return Fraction(yeninum//lowest, yeniden//lowest)
    
    def __mul__(self, other):                       #çarpma
        yeninum = self.num * other.num
        yeniden = self.den * other.den
        
        lowest = obeb(yeninum, yeniden)
        
        return Fraction(yeninum//lowest, yeniden//lowest)
    
    def __truediv__(self, other):
        yeninum = self.num * other.num
        yeniden = self.den * other.den
        
        lowest = obeb(yeninum, yeniden)
        
        return Fraction(yeninum//lowest, yeniden//lowest)
    
    def __eq__(self, other):                        #eşitlik
        first = self.num * other.den
        second = self.den * other.num
        return first == second
    
    def __lt__(self, other):   #last then
        first = self.num * other.den
        second = self.den * other.num
        return first < second
    
    def __gt__(self, other):   #greater then
        first = self.num * other.den
        second = self.den * other.num
        return first > second
    
        
def main():
    f = Fraction(1,2)
    g = Fraction(5,4)
    print (f, "'nın payı ; ", f.getNum())
    print (g, "'nın paydası ; ", g.getDen())
    h = f + g
    j = Fraction(3,6)
    print (f, "+", g, "=", h)
    print(f, "-", j, "=", f-j)
    print (g, "ve", f, "eşit mi ?", g == f)
    print (f, "ve", j, "eşit mi ?", f == j)
    print (f, "ve", j, "eşit değil mi ?", f != j)
    print (g, "*", j, "=", g * j)
    print (f, "/", h, "=", f / h)
    print (g, "büyük mü", j, "den", g > j)
    print (h, "küçük mü", j, "den", h < j)
    
main()


#%%

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
    semboller = [i for i in expr]
    
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
            try:
                while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[sembol]):
                    postfixListe.append(opStack.pop())
                opStack.push(sembol)
                
            except KeyError:
                print("\n")
                print("*" * 50)
                print("INPUTUNUZ HATALI, İŞLEMLER ARASINDA BOŞLUK BIRAKMAYIN")
                print("*" * 50)
                print("\n")
                
    while not opStack.isEmpty():
        postfixListe.append(opStack.pop())
        
    return " ".join(postfixListe)

print("Infix to Postfix", infixtoPostfix("((A+B)*C)/D"))
print("Infix to Postfix", infixtoPostfix("A*B+(C / D)"))
print("Infix to Postfix", infixtoPostfix("9+3*5/(6-4)"))

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

#%%

class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, other):
        return self.items.insert(0, other)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def reverse(self):
        liste = []
        for i in range(len(self.items)):
            liste.append(self.items.pop())
        return liste

q = Queue()
print("is empty     : ", q.isEmpty())
print("enqueue      : ", q.enqueue(22))
print("enqueue      : ", q.enqueue("Batuhan"))
print("items        : ", q.items)
print("size         : ", q.size())
print("dequeue      : ", q.dequeue())
print("size         : ", q.size())
print("items        : ", q.items)
print("enqueue      : ", q.enqueue(55))
print("enqueue      : ", q.enqueue(True))
print("items        : ", q.items)
print("reversed     : ", q.reverse())

import random

def potatoGame(strs):
    nums = random.randint(len(strs) + 1, len(strs) + 5)
    potato = Queue()
    for isim in strs:
        potato.enqueue(isim)
    while potato.size() > 1:
        for i in range(nums):
            potato.enqueue(potato.dequeue())
        potato.dequeue()
    return potato.dequeue()

print("Potato Game : ", potatoGame(["Batuhan", "Ali", "Murat", "Yakup"]))
    


    ### printer problem ###
    
"""
    Görev : Bilgisayar laboratuvarını çıktı almak için kullanan öğrenciler,
            1 ile 20 sayfa arasında çıktı alabilirler ve çıktı kalitesine göre
            çıktıyı alma süresi doğru orantılı. dakikada 10 sayfa verebiliyor, eğer 
            kalite artarsa dakikada 5 sayfa verebilir. First come first serve mantığı
            ile queue kullanarak öğrenciler derse geç kalmadan çıktı almalarını sağlayacak
            kod
"""
    
class Printer:
    def __init__(self, sayfa):
        self.sayfarate = sayfa
        self.islem = None
        self.sayac = 0
        
    def zaman(self):
        if self.islem != None:
            self.sayac = self.sayac - 1
            if self.sayac <= 0:
                self.islem = None
        
    def mesgul(self):
        if self.islem != None:
            return True
        else:
            return False
        
    def siradaki(self, yeni_islem):
        self.islem = yeni_islem
        self.sayac = yeni_islem.sayfaGetir() * 60 / self.sayfarate
        
class Task:
    def __init__(self, time):
        self.damga = time
        self.sayfa = random.randrange(1, 21)
        
    def zamanEtiketi(self):
        return self.damga
    
    def sayfaGetir(self):
        return self.sayfa
    
    def bekle(self, currenttime):
        return currenttime - self.damga
    

def simulation(numSec, pagePerMin):
    
    printer = Printer(pagePerMin)
    printQueue = Queue()
    waitTime = []
    
    for currentsec in range(numSec):
        
        if newPrintTask():
            task = Task(currentsec)
            printQueue.enqueue(task)
            
        if (not printer.mesgul()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitTime.append(nextTask.bekle(currentsec))
            printer.siradaki(nextTask)
            
        printer.zaman()
        
    ortalamaBekle = sum(waitTime)/len(waitTime)
    print("Kalan işlem %3d, Ortalama bekleme süresi %6.2f saniye" %(printQueue.size(), ortalamaBekle))
    
def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False
    
for i in range(10):
    simulation(3600, 10)
    
#%%
    
class Deque:
    def __init__(self):
        self.items = []
        
    def addFront(self, item):
        self.items.append(item)
       
    def addRear(self, item):
        self.items.insert(0, item)
        
    def removeFront(self):
        return self.items.pop()
        
    def removeRear(self):
        return self.items.pop(0)
        
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
d = Deque()
print("add front : ilk")
d.addFront("ilk")
print("add front : ikinci")
d.addFront("ikinci")
print("add rear : üçüncü")
d.addRear("üçüncü")
print("size : ", d.size())
print(d.items)
print("remove rear : ", d.removeRear())
print("remove front : ", d.removeFront())
print("is empty : ", d.isEmpty())
print(d.items)


print("*" * 25)
   ### palindrome check ###

def palcheck(strs):
    char = Deque()
    
    for ch in strs:
        char.addRear(ch)
        
    equal = True
    
    while char.size() > 1 and equal:
        ilk = char.removeFront()
        son = char.removeRear()
        if ilk != son:
            equal = False
    return equal

print("palindrome string : batuhan ->", palcheck("batuhan"))
print("palindrome string : ahpha ->", palcheck("ahpha"))

#%% Node Class

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
        
    def setNext(self, newnext):
        self.next = newnext
        
n = Node(95)
print(n.getData(), n.getNext())
n.setData("Batu")
n.setNext(5)
print(n.getData(), n.getNext())

print("*" * 25)

  ### Unordered List

class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        if self.tail is None:
            self.tail = temp
        self.length += 1
        
    def append(self, item):
        new = Node(item)
        last = self.tail
        if last:
            last.setNext(new)
        else:
            self.head = new
        self.tail = new
        self.length += 1
            
    def insert(self, index, item):
        if index == 0:
            self.add(item)
        elif index > self.size():
            raise IndexError("Out of range")
        elif index == self.size():
            self.append(item)
        else:
            new = Node(item)
            current = self.head
            before = None
            count = 0
            
            while count != index:
                before = current
                current = current.getNext()
                count = count + 1
            before.setNext(new)
            new.setNext(current)
        self.length += 1
            
    def size(self):
        """
            O(n)
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
        """
        return self.length
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def remove(self, item):
        current = self.head
        before = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                before = current
                current = current.getNext()
                
        if before == None:
            self.head = current.getNext()
        else:
            if current.getNext() is None:
                self.tail = before
            before.setNext(current.getNext())
        self.length -= 1
        
    def pop(self, index=None):
        if index is None:
            index = self.length - 1
        if index > self.length - 1:
            raise IndexError("Out of range")
        current = self.head
        before = None
        found = False
        if current:
            count = 0
            while current.getNext() is not None and not found:
                if count == index:
                    found = True
                else:
                    before = current
                    current = current.getNext()
                    count += 1
            if before is None:
                self.head = current.getNext()
                if current.getNext() is None:
                    self.tail = current.getNext()
            else:
                self.tail = before
                before.setNext(current.getNext())
                    

mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
print(mylist.size())
print(mylist.search(100))
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))
mylist.append(55)
print(mylist.search(55))
mylist.insert(1, 93)
print(mylist.search(93))
mylist.pop(1)
print(mylist.search(77), mylist.search(55), mylist.search(93))

print("*" * 25)

    ### OrderedList


class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        return self.length
    
    def remove(self, item):
        current = self.head
        found = False
        before = None
        while not found:
            if current.getData() == item:
                found = True
            else:
                before = current
                current = current.getNext()
        if before is None:
            self.head = current.getNext()
            if current.getNext() is None:
                self.tail = current
        else:
            before.setNext(current.getNext())
        self.length -= 1
        
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
    
    def add(self, item):
        current = self.head
        before = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                self.tail = item
                before = current
                current = current.getNext()
        
        new = Node(item)
        if before is None:
            new.setNext(self.head)
            self.head = new
        else:
            new.setNext(current)
            before.setNext(new)
        if self.tail is None:
            self.tail = new
        self.length += 1
            
    def pop(self, index=None):
        current = self.head
        before = None
        found = False
        if index is None:
            index = self.length - 1
        if index > self.length - 1:
            raise IndexError("Out of range")
        if current:
            count = 0
            while current.getNext() is not None and not found:
                if count == index:
                    found = True
                else:
                    before = current
                    current = current.getNext()
                    count += 1
            if before is None:
                self.head = current.getNext()
                if current.getNext() is None:
                    self.tail = current.getNext()
            else:
                self.tail = before
                before.setNext(current.getNext())
            
orlist = OrderedList()
print(orlist.isEmpty())
print(orlist.size())
orlist.add(5)
orlist.add(8)
print(orlist.search(8))
orlist.remove(5)
print(orlist.search(5))
print(orlist.size())
orlist.pop()
print(orlist.size())



















