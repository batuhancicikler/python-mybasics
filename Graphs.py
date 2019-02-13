# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 00:32:50 2019

@author: batuhan
"""

#%% Graphs
# G = (V, E) -> (G graf, E kenarlar, V ise nodeler)
# V = {V0, V1, V2, V3}, E = {(v0,v1,5), (v0, v2, 3)} edge lerdeki v ler nodeleri temsil ederken tamsayı ise
#                                                   aralarındaki maliyeti (weight) temsil ediyor.

class Düğüm:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        
    def komsuEkle(self, num, maliyet = 0):
        self.connectedTo[num] = maliyet
    
    def __str__(self):
        return str(self.id) + "'dan" + str([x.id for x in self.connectedTo]) + "'a bağlı"
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, num):
        return self.connectedTo[num]
    
#Tüm düğüm objelerini yani nodeleri iterate etmek için __iter__ methoduna ihtiyacımız var
        
class Graph:
    def __init__(self):
        self.düğümListe = {}
        self.düğümSayı = 0
        
    def düğümEkle(self, key):
        self.düğümSayı = self.düğümSayı + 1
        yeniDüğüm = Düğüm(key)
        self.düğümListe[key] = yeniDüğüm
        return yeniDüğüm
    
    def düğümGetir(self, num):
        if num in self.düğümListe:
            return self.düğümListe[num]
        else:
            return None
        
    def __contains__(self, num):
        return num in self.düğümListe
    
    def kenarEkle(self, f, t, maliyet = 0):
        if f not in self.düğümListe:
            yd = self.düğümEkle(f)
        if t not in self.düğümListe:
            yd = self.düğümEkle(t)
        self.düğümListe[f].komsuEkle(self.düğümListe[t], maliyet)
        
    def komsuGetir(self):
        return self.düğümListe.keys()
    
    def __iter__(self):
        return iter(self.düğümListe.values())
    
    
g = Graph()
for i in range(6):
    g.düğümEkle(i)
print("Düğüm liste : ", g.düğümListe)
g.kenarEkle(2,4,7) #düğüm 2 den düğüm 4 e 7 maliyetli kenar ekle
g.kenarEkle(1,5,3)
g.kenarEkle(0,6,10)

for v in g:
    for w in v.getConnections():
        print("{}, {}" .format(v.getId(), w.getId()))
        
        
        
        
        
        
    