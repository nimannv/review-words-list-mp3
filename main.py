from email import parser
import sys, getopt
import voice, parser

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
            word_repeat = arg.strip()
        elif opt in ("-d", "--des-repeat"):
            description_repeat = int(arg.strip())
        elif opt in ("-i"):
            just_important = True
        elif opt in ("-f", "--frame"):
            frame_size = int(arg.strip())
    
    item_list = parser.get_words_list(file_path, just_important)
    for item in item_list:
        voice.get_voice(item['word'])


if __name__ == "__main__":
   main(sys.argv[1:])