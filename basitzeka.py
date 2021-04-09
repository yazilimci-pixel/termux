import colorama 
import random 
from colorama import Fore,Back,Style
colorama.init()
from time import sleep
import os
from gtts import gTTS
cümleler = ["Şimdi neden seni hazmedemediğimi daha iyi anlıyorum Bünye Haram Lokmayı kaldırmıyor Söylemeyi unutmuşum","Bazıları göz yaşını siler bazıları ise ağlatanı","Aklımdan geçtin gittin kim bilir yine kime gidiyordun","Sadece işi düşünce gelene dost mu deniyordu Puşt mu deniyordu Hoşt mu deniyordu","Senin gibi bozuklukları kumbarada biriktirir geleceğe yatırım yaparım Ha çok mu sıkıştım hiç düşünmem hemen harcarım","Seni adam ederdim ama çoktan köpeğim olmuşsun ne lüzumu var","Tipi Tarlabaşı ama egosu sanırsın Nişantaşı","Apartman lambasının bile fark etmediği insanlarla uğraşıyoruz","Taş gibi kızsın ama OKEY taşı Elden elde gidiyorsun farkında değilsin","El üstünde tuttum anlamadın Ayaklar altında rahat mısın"]
a = 0
while True:
      a +=1
      rastgele = random.choice(cümleler)
      ses = gTTS(text=rastgele,lang="tr",slow=False)
      ses.save("Secilen.mp3")
      os.system("Secilen.mp3")
      input("Enter Bas..")
      if a == 10:
           break