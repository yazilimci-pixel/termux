import colorama 
import random 
from colorama import Fore,Back,Style
import gtts
colorama.init()
from time import sleep
import os
from gtts import gTTS
print(""" 
--------------İsimler-------------
Sude
Dilek
Berna
Kamil
""")
isim = input("İsme Özel Diss Atıyorum...\nİsminiz;")
if isim == "Sude":
    ses = gTTS(text="Cuvarayı Bıraksan İnek Bir Öğrenci Olcan Ama Sen Zekisin Fakat Yaratıcım kadar değil ağla Sude",lang="tr",slow=False)
    ses.save("dis.mp3")
    os.system("dis.mp3")
elif isim == "Dilek":
    ses = gTTS(text="Senin Hakkında Konuşamam Valla Döverler ama iyi birisin dilek bu arada yok ya ben gelmedim",lang="tr",slow=False)
    ses.save("dis.mp3")
    os.system("dis.mp3")
elif isim == "Berna":
    ses = gTTS(text="Peri nerde ya şaka maka sana ne disi atıcam",lang="tr",slow=False)
    ses.save("dis.mp3")
    os.system("dis.mp3")
elif isim == "Kamil":
    ses = gTTS(text="Benim Canım Yaratıcım Beni Geliştiren Ellerin Dert Görmesin Umarım Daha İyi Yerlere Gelirsin Seni Çok Seviyorum",lang="tr",slow=False)
    ses.save("dis.mp3")
    os.system("dis.mp3")