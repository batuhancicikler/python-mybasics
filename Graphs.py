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
        self.connectedTo = {}  #nodenin bğlantılarını tutacak  örn. "3 id li node 4 id liye 7 maliyetinde bağlı"
        
    def komsuEkle(self, num, maliyet = 0):
        self.connectedTo[num] = maliyet #girilen num daki nodeye maliyeti derecesinde bağlantı ekler
    
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
    
"""    
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
"""
    
## Knight's Tour
        
# knightGraph fonksiyonu tüm tahtada dolaşır her bir kutu da
#  legalMoves fonksiyonu yardımıyla oynanabilecek hamleleri işaretler
#   bir diğer yardımcı fonksiyon posToNodeId ise işaretlenen kutucukları
#    satır ve sütun olarak numaralara döndürür
        

def knightGraph(tahtaBoyut):
    kg = Graph()
    for satır in range(tahtaBoyut):
        for sütun in range(tahtaBoyut):
            nodeId = posToNodeId(satır, sütun, tahtaBoyut)
            yeniPos = legalMoves(satır, sütun, tahtaBoyut)
            for e in yeniPos:
                nId = posToNodeId(e[0], e[1], tahtaBoyut)
                kg.kenarEkle(nodeId, nId) # from:nodeId, to: nId
    return kg

def posToNodeId(satır, sütun, tahta_boyut):
    return (satır * tahta_boyut) + sütun

# legalMoves fonksiyonu; knight in tahtadaki pozisyonunu alır ve hareket edebileceği
#  muhtemel 8 hamleyi döndürür. legalCoord yardımcı fonksiyonu oluşturulmuş muhtemel
#   pozisyonun hala tahtada olduğundan emin olur.
    
def legalMoves(x, y, tahtaboyut):
    yeniHamle = []
    hamleOffset = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in hamleOffset:
        yeniX = x + i[0]
        yeniY = y + i[1]
        if legalCoord(yeniX, tahtaboyut) and legalCoord(yeniY, tahtaboyut):
            yeniHamle.append((yeniX, yeniY))
    return yeniHamle

def legalCoord(num, TahtaBoyut):
    if num >= 0 and num < TahtaBoyut:
        return True
    else:
        return False
    
#knightTour fonksiyonu oluşturup 4 parametre alıcaz. n, search treenin derinliği.
# path, şu ana kadar ziyaret edilmiş düğümlerin listesi. u, ziyaret etmek istediğimiz düğüm.
#  ve limit, path üzerindeki node sayısı. knightTour fonksiyonu rekürsif çalışıcak, fonksiyon
#   çağırıldığında ilk olarak base case yi kontrol edecek, eğer path ta 64 düğüm varsa true döndürecek
#    ve başarılı bir tur bulunmuş olucak, eğer path yeterli değilse bir seviye daha derinlikteki düğümü
#     ziyaret etmek için seçer ve fonksiyonu onun üzerinden rekürsif bir şekilde çağırır

# ziyaret edilmemiş nodeler beyaz, ziyaret edilmişler gri. belirli bir düğümün tüm komşuları
#  ziyaret edilmiş ise ve hala 64 düğüm hedefine ulaşamamışsak, çıkmaz sokağa girmiş sayılıyor,
#   bu yüzden böyle bir durumda geriye saracağız. Bu durum kngihtTour fonksiyonu false döndüğünde
#    yapılır.
        
def knightTour(n, path, u, limit):
    u.setColor("gri")
    path.append(u)
    if n < limit:
        numList = list(u.getConnections())
        i = 0
        bitti = False
        while i < len(numList) and not bitti:
            if numList[i].getColor() == "beyaz":
                bitti = knightTour(n + 1, path, numList[i], limit)
            i += 1
        if not bitti: #geri sarmak için
            path.pop()
            u.setColor("beyaz")
    else:
        bitti = True
    return bitti

"""
    varsayalım ki a,b,c,d,e,f düğümlerinin olduğu bir path var, ve bağıntılarımız
    (a, b)(a, d)(b, d)(b, c)(d, e)(e, b)(e, f)(f, c)
    eğer a-b-c yolu üstünden gidersek hepsini gezemeden yol tıkanır. Yani a b c gri iken geri kalanlar beyaz
    o yüzden b ye geri döner c.pop ve c.setcolor("beyaz"), b den d ye d den e ye gider. e den b ve f ye
    yolumuz var ama b zaten gri olduğu için f ye ve ordan c ye gider ve böylece tamamlamış oluruz.
    8 tane kenar(edge) olduğu için bu örnek 8 e 8 tahtası olarak düşünürsek tamamlandı diyebiliriz.
"""

## Dijkstra nın algoritması
"""
    Algoritmanın amacı bir düğümden diğer olası düğümlere olabilecek en kısa mesafeyi seçme algoritmasıdır.
"""
        










        
        
        
        
    