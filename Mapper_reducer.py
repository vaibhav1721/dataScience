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

def reducer():
    word_count = 0
    old_key = None
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        this_key,count = data
        if old_key and old_key != data:
            print("{0}\t{1}".format(old_key,word_count))
            word_count = 0
        old_key = this_key
        word_count += float(count)
    if old_key != None:
        print("{0}\t{1}".format(old_key,word_count))

if __name__ == '__main__':
   # mapper()
    reducer()