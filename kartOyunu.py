# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 14:01:11 2019

@author: batuhan
"""

from enum import Enum
from enum import IntEnum
from random import *


full_deste = []
gecici_deste = []
player_kart = []
player2_kart = []

    # kart enum u, deste için
class Kart(IntEnum):
    İKİ = 2
    ÜÇ = 3
    DÖRT = 4
    BEŞ = 5
    ALTI = 6
    YEDİ = 7
    SEKİZ = 8
    DOKUZ = 9
    ON = 10
    JOKER = 11
    KIZ = 12
    KRAL = 13
    AS = 14

    # suit enum u
class Suit(Enum):
    MAÇALAR = "maçalar"
    SİNEKLER = "sinekler"
    KUPALAR = "kupalar"
    KAROLAR = "karolar"
    

    # kart oyunu için bilgi tutacak class
class KartOyunu:
    def __init__(self, kart_value, kart_suit):
        self.kart = kart_value
        self.suit = kart_suit
        
        # tüm deste kartlarıyla ilgilenmesi için gerekli fonksiyon
def deste_olustur():
    for suit in Suit:
        for kart in Kart:
            full_deste.append(KartOyunu(Kart(kart), Suit(suit)))
    return full_deste
    

    # desteden tek kart çekme
def draw_kart(deste):
    rand_kart = randint(0, len(deste) - 1)
    return deste.pop(rand_kart)     # çekilen kartı return edip, desteden çıkartıyor
    
        
    # oyuncuların destelerine, geçici desteden kağıtları dağıtıyor
def halfdeal():
    while(len(gecici_deste) > 0):
        player_kart.append(draw_kart(gecici_deste))
        player2_kart.append(draw_kart(gecici_deste))

deste_olustur()
gecici_deste = list(full_deste)
halfdeal()

for i in range(0, len(player_kart)):
    if(player_kart[i].kart > player2_kart[i].kart):
        print("Player 1 eli kazandı !", player_kart[i].kart)
        print("Player 2 eli kaybetti !", player2_kart[i].kart)
        
    if(player2_kart[i].kart > player_kart[i].kart):
        print("Player 2 eli kazandı !", player2_kart[i].kart)
        print("Player 1 eli kaybetti !", player_kart[i].kart)
    else:
        print("Kazanan Yok")