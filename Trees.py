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

def islempostorder(tree):
    operators = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}
    res1 = None
    res2 = None
    
    if tree:
        res1 = islempostorder(tree.getleft())
        res2 = islempostorder(tree.getright())
        if res1 and res2:
            return operators[tree.getRoot()](res1, res2)
        else:
            return tree.getRoot()

pt = parseTree("( ( 3 + 5 ) / 2")

# İşlemleri yapmak için treedeki tüm nodelere gitmemiz gerekiyor  bunun farklı yöntemleri var
# bu nodeleri ziyaret etme işlemine "traversal" denir. 3 tane treversal var preorder inorder postorder

#preorder: önce root node ziyaret edilir ardından rekürsif bir şekilde sol subtreeye git aynı anda
# yine rekürsif bir şekilde sağ subtreeyi de preorder şekilde ziyaret et

#inorder: rekürsif bi şkilde sol subtreeye git ve root nodeyi ziyaret et ve rekürsif olarak sağ subtree
#ye de inorder bir şekilde git

#postorder: rekürsif bi şekilde sağ ve sol subtreelerden root nodeyi ziyaret et


#tree yerine self kullanarak binarytree classının fonksiyonu olarak yapabiliriz
#ancak o zaman da binarytree de değişiklik yapmamız gerekicek
def preorder(tree):
    if tree:
        print(tree.getRoot())
        preorder(tree.getleft())
        preorder(tree.getright())
        
def postorder(tree):
    if tree != None:
        postorder(tree.getleft())
        postorder(tree.getright())
        print(tree.getRoot())
        
def inorder(tree):
    if tree != None:
        inorder(tree.getleft())
        print(tree.getRoot())
        inorder(tree.getright())
        
def printexpr(tree):
    val = ""
    if tree:
        val = "(" + printexpr(tree.getleft())
        val = val + str(tree.getRoot())
        val = val + printexpr(tree.getright()) + ")"
    return val


#%% Binary Heap -- Priority Queue
    
class BinHeap():
    def __init__(self):
        self.heapL = [0]
        self.size = 0
        
    # yeni item eklemek içn insert methodu oluşturmadan önce
    #eklenecek itemin üstteki rootlarla yer değiştirmesini sağlayacak percUp methodu yazılır
    def percUp(self, i):
        while i//2 > 0:
            if self.heapL[i] < self.heapL[i // 2]:
                temp = self.heapL[i // 2]
                self.heapL[i // 2] = self.heapL[i]
                self.heapL[i] = temp
            i = i // 2
            
    def insert(self, item):
        self.heapL.append(item)
        self.size = self.size + 1
        self.percUp(self.size)
        
    def percDown(self, i):
        while i * 2 <= self.size:
            minC = self.minChild(i)
            if self.heapL[i] > self.heapL[minC]:
                temp = self.heapL[i]
                self.heapL[i] = self.heapL[minC]
                self.heapL[minC] = temp
            i = minC
            
    def minChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapL[i*2] < self.heapL[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
            
    def delMin(self):
        val = self.heapL[1]
        self.heapL[1] = self.heapL[self.size]
        self.size = self.size - 1
        self.heapL.pop()
        self.percDown(1)
        return val
    
    def buildHeap(self, liste):
        i = len(liste) // 2
        self.size = len(liste)
        self.heapL = [0] + liste[:]
        while i > 0:
            self.percDown(i)
            i = i - 1
            
bh = BinHeap()
bh.buildHeap([5,4,2,7,8,9,42,18])
print(bh.size)
print(bh.heapL)
print(bh.delMin())
print(bh.heapL)
print(bh.insert(1))
print(bh.heapL)


#%% Search Tree

# girilen listenin ilk elemanı root olur ardından eğer roottan büyük eleman girilirse
# sağ subtreeye yerleştirilir, roottan küçük olanlar ise sol subtreeye

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1
    
    def _put(self, key, val, current):
        if key < current.key:
            if current.hasLeft():
                self._put(key, val, current.left)
            else:
                current.left = TreeNode(key, val, parent = current)
        else:
            if current.hasRight():
                self._put(key, val, current.right)
            else:
                current.right = TreeNode(key, val, parent = current)
                
    # put methodu ile birlikte __setitem__ kullanarak [] operatörünü uygulayabiliriz
    # örnek : myTree["abc"] = 558122 [] = key, 558122 = value
    
    def __setitem__(self, key,value):
        self.put(key, value)
        
    # tıpkı sette olduğu gibi get _get ve __getitem__ yapıcaz
    
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None
    
    def _get(self, key, current):
        if not current:
            return None
        elif current.key == key:
            return current
        elif key < current.key:
            return self._get(key, current.left)
        else:
            return self._get(key, current.right)
        
    def __getitem__(self, key):
        return self.get(key)
    
    # get ile beraber __contains__ methodu ile "in" komutunu kullanabiliriz
    
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
        
    # delete fonksiyonu için ilk olarak silinecek key tree içinde aranır.
    # eğer birden fazla o keyden varsa TreeNode de _get kullanılarak bulunur.
    # eğer 1 tane varsa roottur yani silinecektir ama root key ile aranan key bir kere daha
    # check edilir. Eğer del operatoru calısmaz ise error verdiririz.
    
    def delete(self, key):
        if self.size > 1:
            removeNode = self._get(key, self.root)
            if removeNode:
                self.remove(removeNode)
                self.size -= 1
            else:
                raise KeyError("Key, Tree'de değil")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Key, Tree'de değil")
            
    def __delitem__(self, key):
        self.delete(key)
        
        # silinen elemanın yerine ne gelicek ?
        
    def findNew(self):
        yeni = None
        if self.hasRight():
            yeni = self.right.findMin()
        else:
            if self.parent:
                if self.isLeft():
                    yeni = self.parent
                else:
                    self.parent.right = None
                    yeni = self.parent.findNew()
                    self.parent.right = self
        return yeni
    
    def toparla(self):
        # eğer current node hiç child e sahip değil ise direk referansı sil.
        if self.isLeaf():
            if self.isLeft():
                self.parent.left = None
            else:
                self.parent.right = None
                
        elif self.hasAny():
            if self.hasLeft():
                if self.isLeft():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isLeft():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent
                
    def remove(self, current):
        if current.isLeaf():
            if current == current.parent.left:
                current.parent.left = None
            else:
                current.parent.right = None
                
        elif current.hasBoth():
            new = current.findNew()
            new.toparla()
            current.key = new.key
            current.value = new.value
            
        else:
            if current.hasLeft():
                if current.isLeft():
                    current.left.parent = current.parent
                    current.parent.left = current.left
                elif current.isLeft():
                    current.left.parent = current.parent
                    current.parent.right = current.left
                else:
                    current.replaceNode(current.left.key,
                                        current.left.value,
                                        current.left.left,
                                        current.left.right)
            else:
                if current.isLeft():
                    current.right.parent = current.parent
                    current.parent.left = current.right
                elif current.isRight():
                    current.right.parent = current.parent
                    current.parent.right = current.right
                else:
                    current.replaceNode(current.right.key,
                                        current.right.value,
                                        current.right.right,
                                        current.right.left)
                    
    def findMin(self):
        current = self
        while current.hasLeft():
            current = current.left
        return current
                
    # binary search treenin son arayüzmethodu iterasyon(iterate). Bunun için inorder traversali ile
    # birlikte __iter__ fonksiyonunu kurcaz, bununla beraber yield fonksiyonunu kullanmamız grekiyor
    # return a benzer bir şekilde yield direk döndürmek yerine döndürdüğü sonuçta donar, bir sonraki
    # yield edilişinde kaldığı yerden devam eder. İtera edilebilir objeler olşturan fonkisyonlara
    # generator fonksiyonlar denir.
    # __iter__ fonksiyonu, for x in operasyonunu döndürür iterasyon için yani aslında rekürsif yapıdadır
    
class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        
    def hasLeft(self):
        return self.left
    
    def hasRight(self):
        return self.right
    
    def isLeft(self):
        return self.parent and self.parent.left == self
    
    def isRight(self):
        return self.parent and self.parent.right == self
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.right or self.left)
    
    def hasAny(self):
        return self.right or self.left
    
    def hasBoth(self):
        return self.right and self.left
    
    def replaceNode(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.left = lc
        self.right = rc
        if self.hasLeft():
            self.left.parent = self
        if self.hasRight():
            self.right.parent = self

benimTree = BinarySearchTree()
benimTree[1] = "Batuhan"
benimTree[2] = "Cicikler"
benimTree[3] = "Samsun"

print(benimTree[2])
print(benimTree.length())

#%%












  
    








