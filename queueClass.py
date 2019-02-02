# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 01:43:05 2019

@author: batuhan
"""

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

q = Queue()
print("is empty     : ", q.isEmpty())
print("enqueue      : ", q.enqueue(22))
print("enqueue      : ", q.enqueue("Batuhan"))
print("items        : ", q.items)
print("size         : ", q.size())
print("dequeue      : ", q.dequeue())
print("size         : ", q.size())
print("items        : ", q.items)

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