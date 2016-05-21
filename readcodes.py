import os
from os.path import join

def main() :
    dest = '/Users/XmacZone/Documents/Unity Projects/WEROUND/Assets/Scripts'
    i=0
    with open( "output.txt", "w" ) as outfile:
        for root, dirs, files in os.walk( dest ):
            for OneFileName in files :
                if OneFileName.find( '.cs' ) == -1 :
                    continue
                OneFullFileName = join( root, OneFileName )
                with open(OneFullFileName) as codefile:
                    for line in codefile:
                        outfile.write(line)
                        i+=1
    print(i)

if __name__ == "__main__" :
    main()
