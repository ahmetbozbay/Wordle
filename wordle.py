import random
from colorama import Fore
from tkinter import *
def game():
    bes_harfli_kelime_a=[]
    dosya = open("abesharf.txt","r",encoding="utf-8")
    oku = dosya.readlines()
    oku = [each_string.lower() for each_string in oku]
    for i in oku:
        bes_harfli_kelime_a.append(i)
    ch = '\n'
    ab='̇'
    bes_harfli_kelime_a = [elem.replace(ch , '') for elem in bes_harfli_kelime_a]
    bes_harfli_kelime_a = [elem.replace(ab, '') for elem in bes_harfli_kelime_a]
    bulunacakkelime=random.choice(bes_harfli_kelime_a)
    bulunacakkelime=list(bulunacakkelime)
    can=5
    step=1
    while can > 0:
        girilen_metin=input("ADIM "+str(step)+ " : BEŞ HARFLİ BİR KELİME YAZINIZ >>> ")
        girilen_metin=list(girilen_metin)
        step += 1
        for i in range(5):
            if girilen_metin == bulunacakkelime:
                print(Fore.MAGENTA+"Helalllllllllllllll")
                exit()
            elif len(girilen_metin)!=len(bulunacakkelime):
                print("Lütfen 5 harfli kelime yazınız.\nCanınız eksilmemiştir.")
                can+=1
                step-=1
                break
            elif(girilen_metin[i]==bulunacakkelime[i]):
                girilen_metin[i] = Fore.GREEN + girilen_metin[i]+Fore.LIGHTWHITE_EX
            elif girilen_metin[i] in bulunacakkelime:
                girilen_metin[i] = Fore.YELLOW + girilen_metin[i]+Fore.LIGHTWHITE_EX
            elif girilen_metin[i]!=bulunacakkelime[i]:
                girilen_metin[i] = Fore.LIGHTWHITE_EX + girilen_metin[i]+Fore.LIGHTWHITE_EX
        girilen_metin = ' '.join([str(elem) for elem in girilen_metin])
        print(girilen_metin)
        can-=1
        if can==1:
            print("Son canın iyi düşün biraz !!")
        elif can==0:
            bulunacakkelime = ' '.join([str(elem) for elem in bulunacakkelime])
            print("Doğru cevap :" + str(bulunacakkelime))
        print("KALAN HAKKINIZ : "+ str(can))
game()