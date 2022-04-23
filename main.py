from email import parser
from gc import collect
import sys, getopt
import voice, parser
from pydub import AudioSegment
import time

def main(argv):
    file_path = ''
    word_repeat = 1
    description_repeat = 1
    just_important = False
    frame_size = None

    try:
        opts, args = getopt.getopt(argv,"hs:w:d:if:",["source=","word-repeat=","des-repeat=","frame="])
    except getopt.GetoptError:
        print ('explain how to execute it in a right way')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('main.py -s <source> -w <word_repeat> -d <description_repeat> \n -i: Just important word. \n -f: frame size, count of word in single MP3 file.')
            sys.exit()
        elif opt in ("-s", "--source"):
            file_path = arg.strip()
        elif opt in ("-w", "--word-repeat"):
            word_repeat = int(arg.strip())
        elif opt in ("-d", "--des-repeat"):
            description_repeat = int(arg.strip())
        elif opt in ("-i"):
            just_important = True
        elif opt in ("-f", "--frame"):
            frame_size = int(arg.strip())
    
    # Get items
    item_list = parser.get_words_list(file_path, just_important)

    #--------
    between_long = AudioSegment.silent(duration=1000)
    between_short = AudioSegment.silent(duration=1000)
    review_voice = AudioSegment.empty()

    # Collect all voices
    for item in item_list:
        word_voice_file_name = voice.get_voice(item['word'])
        word_voice = AudioSegment.from_mp3(word_voice_file_name)

        for _ in range(word_repeat):
            review_voice += word_voice + between_short
        review_voice += between_short

        if description_repeat > 0:
            for _ in range(description_repeat):
                desc_voice_file_name = voice.get_voice(item['description'])
                desc_voice = AudioSegment.from_mp3(desc_voice_file_name)
                review_voice += desc_voice + between_short
  
        review_voice += between_long
            
    # Export review file
    review_voice.export("review-files-mp3/review-"+str(time.time())+".mp3", format="mp3")

if __name__ == "__main__":
   main(sys.argv[1:])