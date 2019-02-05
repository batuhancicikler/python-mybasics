# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 18:26:00 2019

@author: batuhan
"""

#%% Monty Hall Problemi

import random, argparse

def sim(kapılar, degistir, verb):
    
    #kazanan kapı random seç
    win = random.randint(0, kapılar - 1)
    if verb:
        print("Ödül {} kapının arkasında" .format(win + 1))
        
    # yarışmacının seçtiği kapı
    secim = random.randint(0, kapılar -1)
    if verb:
        print("Yarışmacı {}. kapıyı seçti" .format(secim + 1))
        
    #sunucu win ve secim hariç olan kapıyı açar
    kapalı_kapılar = list(range(kapılar))
    while len(kapalı_kapılar) > 2:
        #rastgele seç
        sunucu_ac = random.choice(kapalı_kapılar)
        
        #sunucu kazanan kapıyı veya yarışmacının seçtiği kapıyı açamaz
        if sunucu_ac == win or sunucu_ac == secim:
            continue
        
        kapalı_kapılar.remove(sunucu_ac)
        if verb:
            print("Sunucu {}. kapıyı açtı" .format(sunucu_ac + 1))
    
    # koşulun doğru olup olmadığını kontrol eder.. yanlış ise AssertionError gönderir
    assert len(kapalı_kapılar) == 2
    
    #yarışmacı değiştirmek istiyor mu ?
    
    if degistir:
        if verb:
            print("yarışmacı {} kapısını" .format(secim + 1), end="")
        
        kalankapı = list(kapalı_kapılar)
        kalankapı.remove(secim)
        
        # seçimi, mümkün olan kapıya değiştir
        secim = kalankapı.pop()
        if verb:
            print("{} 'e değiştiriyor" .format(secim + 1))
            
    # yarışmacı kazandı mı ?
    
    kazandıMı = (secim == win)
    if verb:
        if kazandıMı:
            print("Yarışmacı kazandı", end="\n")
        else:
            print("Yarışmacı kaybetti", end="\n")
    return kazandıMı


def main():
    #cmd komutlarıyla script kullanımı için argparse
    parser = argparse.ArgumentParser(description="Monty Hall problemi simulasyonu")
    parser.add_argument("--kapılar", default=3, type=int, metavar="int",
                        help="teklif edilen kapı sayısı")
    parser.add_argument("--hak", default=10000, type=int, metavar="int",
                        help="uygulanacak tur sayısı")
    parser.add_argument("--verb", default=False, action="store_true",
                        help="her turdaki sonucu göster")
    args = parser.parse_args()
    
    print("Simulasyon {} tur..." .format(args.hak))
    
    #turları uygulayıp hangi grubun kazandığına bakılacak
    kapı_degismeyenler = 0
    kapı_degisenler = 0
    for i in range(args.hak):
        # önce kapı değişmeyenleri hesaplayalım
        kazandıMı = sim(args.kapılar, degistir=False, verb=args.verb)
        if kazandıMı:
            kapı_degismeyenler += 1
            
        # simdi de kapı değişince kazananları hesaplayalım
        kazandıMı = sim(args.kapılar, degistir=True, verb=args.verb)
        if kazandıMı:
            kapı_degisenler += 1
            
    print("{1} kadar turda {0:5} tane kapı değişenler kazandı ({2}% oranında)" 
          .format(kapı_degisenler, args.hak, (kapı_degisenler/args.hak * 100) ))
    
    print("{1} kadar turda {0:5} tane kapı değişmeyenler kazandı ({2}% oranında)" 
          .format(kapı_degismeyenler, args.hak, (kapı_degismeyenler/args.hak * 100) ))
    
if __name__ == "__main__":
    main()
    





