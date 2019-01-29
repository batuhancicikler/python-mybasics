# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:44:57 2019

@author: batuhan
"""

#%% Sub-class / Inherit class / Mantık Kapıları

class LogicGate:
    
    def __init__(self, n):
        self.label = n
        self.output = None
        
    def getLabel(self):
        return self.label               # kullanıcının girdiği n
    
    def getOutput(self):
        self.output = self.mantıkKapısı()   # getOutput() çalıştırıldığında mantıkKapısı fonk. döndürsün
        return self.output
    
class Binary(LogicGate):
    
    def __init__(self, n):
        LogicGate.__init__(self, n)             # super(Binary).__init__(self, n)
        
        self.pinA = None
        self.pinB = None
        
    def getpinA(self):
        
        if self.pinA == None:
            return int(input("Pin A giriniz : "+ self.getLabel()+ "---->"))     # Pin A giriniz : >Gate 1< ---->
        else:
            return self.pinA.getFrom().getOutput()
    
    def getpinB(self):

        if self.pinB == None:
            return int(input("Pin B giriniz : "+ self.getLabel()+ "---->"))
        else:
            return self.pinB.getFrom().getOutput()
    
    def sonrakiPin(self, kaynak):
        if self.pinA == None:
            self.pinA = kaynak
        else:
            if self.pinB == None:
                self.pinB = kaynak
            else:
                raise RuntimeError("Boş Pin Yok !!")
    
class Unary(LogicGate):
    
    def __init__(self, n):
        LogicGate.__init__(self, n)
        
        self.pin = None
        
    def getPin(self):
        
        if self.pin == None:
            return int(input("Bir pin giriniz : "+ self.getLabel()+ "---->"))
        else:
            return self.pin.getFrom().getOutput()
        
    def sonrakiPin(self, kaynak):
        
        if self.pin == None:
            self.pin = kaynak
        else:
            print("Boş pin yok !")
    
class VeKapısı(Binary):
    
    def __init__(self, n):
        Binary.__init__(self, n)
        
    def mantıkKapısı(self):
        a = self.getpinA()
        b = self.getpinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0
        
class VeyaKapısı(Binary):
    
    def __init__(self, n):
        Binary.__init__(self, n)
        
    def mantıkKapısı(self):
        a = self.getpinA()
        b = self.getpinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0
        
class NotKapısı(Unary):
    
    def __init__(self, n):
        Unary.__init__(self, n)
        
    def mantıkKapısı(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1
        
class Connector:        # Bir kapıdan diğerine bağlamak için
    
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        
        tgate.sonrakiPin(self)
        
    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate


g1 = VeKapısı("Gate 1")             # g1 kapısının sonucu ile g2 kapısının sonucunu
g2 = VeKapısı("Gate 2")             # Connertor c1 ve c2 sayesinde Veya kapısına alıp 
g3 = VeyaKapısı("Gate 3")           # Not kapısından c3 ile geçiriyor.
g4 = NotKapısı("Gate 4")

c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

g4.getOutput()