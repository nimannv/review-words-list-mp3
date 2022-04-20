import sys, getopt


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
    
    print('file_path :' , file_path)
    print('word_repeat :' , word_repeat)
    print('description_repeat :' , description_repeat)
    print('just_important :' , just_important)
    print('frame_size : ' , frame_size)


if __name__ == "__main__":
   main(sys.argv[1:])