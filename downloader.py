from itertools import islice
import requests
# from nltk.stem import WordNetLemmatizer

FILE_NAME = 'alice.txt'
URL = 'http://www.umich.edu/~umfandsf/other/ebooks/alice30.txt'

def download():
    req = requests.get(URL, stream=True)
    
    file = open(FILE_NAME, 'wt')
    for line in req.iter_lines(decode_unicode=True):
        file.write(line + '\n')
    
    req.close()
    file.close()
    


def split_file():
    line_num = 0

    with open(FILE_NAME, 'rt') as f:
        for i, line in enumerate(f):
            pass
        line_num = i + 1

    print(line_num)

    with open(FILE_NAME, 'rt') as f:
        with open('alice_001.txt', 'w') as f1:
            for line in islice(f, 0, int(line_num / 3)):
                f1.write(clean_line(line).lower())

    with open(FILE_NAME, 'rt') as f:
        with open('alice_002.txt', 'w') as f2:
            for line in islice(f, int(line_num / 3), int(2 * line_num / 3)):
                f2.write(clean_line(line).lower())

    with open(FILE_NAME, 'rt') as f:
        with open('alice_003.txt', 'w') as f3:
            for line in islice(f, int(2 * line_num / 3), line_num):
                f3.write(clean_line(line).lower() + ' ')


def clean_line(line):
    line.replace('\'', ' ')
    return ''.join(ch for ch in line if ch.isalnum() or ch in ['.', '!', '?', ' '])


if __name__ == "__main__":
    download()
    split_file()
