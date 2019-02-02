# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 01:44:00 2019

@author: batuhan
"""

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