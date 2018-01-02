import sys
import string
try:
    maketrans = ''.maketrans
except AttributeError:
    # fallback for Python 2
    from string import maketrans

def mapper():
    for line in sys.stdin:
        data = line.strip().split(" ")

        for i in data:
            cleanedData = i.translate(maketrans("","",string.punctuation)).lower()
            print("{0}\t{1}".format(cleanedData, 1))


if __name__ == '__main__':
    mapper()