import gtts
import hashlib
import os.path

def get_voice(text):
    text_hash = hashlib.sha1(text.encode('utf-8')).hexdigest()
    if not os.path.exists('voices/'+text_hash+'.mp3'):
        voice = gtts.gTTS(text)
        voice.save('voices/'+text_hash+'.mp3')
    return 'voices/'+text_hash+'.mp3'

if __name__ == "__main__":
   get_voice('hello world')