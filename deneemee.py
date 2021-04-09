from gtts import gTTS
import os
while True:
     yazi = input("Yazıyı Sese Dönüştür...\nCümle;")
     ses = gTTS(text=yazi, lang="tr", slow=False)
     ses.save("kamil.mp3")
     os.system("kamil.mp3")