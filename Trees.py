# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:33:01 2019

@author: batuhan
"""
#%% List of Lists 

mytree = ["a",  ["b", ["d", [], []], ["e", [], []] ],  ["c", ["f", [], []], []]]
print(mytree)
print("root : ", mytree[0])
print("sol subtree : ", mytree[1])
print("sağ subtree : ", mytree[2])

#%% Binary Tree
# Bir parentin 2 den fazla edgesi olamaz...

""" root değeri ve empyt 2 dal ile bir ağaç(tree) oluştur """
def binaryTree(r):
    return [r, [], []]

""" sol subtree deki listenin içine yeni bir liste ekler, eğer zaten bir liste bulunuyorsa
o listeyi, yeni eklediğimiz listenin "sol subtreesi" yapar """
def insertLeft(root, yeniDal):
    tree = root.pop(1)
    if len(tree) > 1:
        root.insert(1, [yeniDal, tree, []])
    else:
        root.insert(1, [yeniDal, [], []])
    return root

def insertRight(root, yeniDal):
    tree = root.pop(2)
    if len(tree) > 1:
        root.insert(2, [yeniDal, [], tree])
    else:
        root.insert(2, [yeniDal, [], []])
    return root

""" yukarıdaki tree-making fonksiyonları döndürmek ve set-get işlemleri yapmak
 için gerekli bir kaç fonksiyon daha eklemeliyiz """
 
def getRootVal(root):
    return root[0]

def setRootVal(root, yeniVal):
    root[0] = yeniVal
    
def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = binaryTree(5)

insertLeft(r, "5a")
insertLeft(r, "5a1")

insertRight(r, "5b")
insertRight(r, "5b1")

print("tree : ", r)
print("get root val : ", getRootVal(r))
print("get left child : ", getLeftChild(r))
print("get right child : ", getRightChild(r))
setRootVal(r, 6)

l = getRightChild(r)
insertLeft(l, "6a")
print("tree : ", r)
insertRight(getLeftChild(r), 10)
print("insertright->getleftchild->10", r)

#%% OOP ile (nodes)

class BinaryTree:
    def __init__(self, root):
            self.key = root
            self.left = None
            self.right = None
            
    def insertLeft(self, new):
        if self.left == None:
            self.left = BinaryTree(new)
        else:
            t = BinaryTree(new)
            t.left = self.left
            self.left = t
            
    def insertRight(self, new):
        if self.right == None:
            self.right = BinaryTree(new)
        else:
            t = BinaryTree(new)
            t.right = self.right
            self.right = t
            
    def getRoot(self):
        return self.key
    def setRoot(self, value):
        self.key = value
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
    
#t = BinaryTree("a")
#t.insertLeft("b")
#t.insertRight("c")

#t.getleft().insertRight("d")
#t.getright().insertLeft("e")
#t.getright().insertRight("f")
        
""" Parse tree için hem binary hem de stack lazım. Parse tree için girilen string
ifadeleri parçalayarak liste haline getiririz. sol ve sağ parntezler operatörler ve
operandlar olmak üzere 4 çeşit token var olduğundan sol parantez ile bir işlemin 
başladığını bildiğimizden, eğer current token sol parantez ise yeni bir nodeyi current
tokenin olduğu nodenin leftchild i olarak oluştur ve oluşturulan yeni nodeye geç.

eğer current token operatör ise o nodeyi root olarak ayarla ve rightchild oluşturup ona geç

eğer current token operand ise leaf olarak bırak ve parent e dön

eğer current token sağ parantez ise parente dön
 """
class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpyt(self):
        return self.items == []
    
    def push(self, item):
        self.items.insert(0, item)
        
    def pop(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
    

def parseTree(expr):
    liste = expr.split()
    parseStack = Stack()
    pTree = BinaryTree("")
    parseStack.push(pTree)
    currentTree = pTree
    
    for i in liste:
        """ sol parantez ise sol child oluştur ona geç 
         eğer operand ise int olarak bulunduğu node yi root yap yap 
         eğer operator ise bulunduğu node yi root yap sağına boş node ekle sağa geç"""
        if i == "(":
            currentTree.insertLeft("")
            parseStack.push(currentTree)
            currentTree = currentTree.getleft()
            
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRoot(int(i))
            parent = parseStack.pop()
            currentTree = parent
            
        elif i in ["/", "*", "-", "+"]:
            currentTree.setRoot(i)
            currentTree.insertRight("")
            parseStack.push(currentTree)
            currentTree = currentTree.getright()
            
        elif i == ")":
            currentTree = parseStack.pop()
            
        else:
            raise ValueError
            
    return pTree
    
import operator

def islem(parseTree):
    operators = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}
    
    left = parseTree.getleft()
    right = parseTree.getright()
    
    if left and right:
        fn = operators[parseTree.getRoot()]
        return fn(islem(left), islem(right))
    else:
        return parseTree.getRoot()

pt = parseTree("( ( 3 + 5 ) / 2")

    
    








