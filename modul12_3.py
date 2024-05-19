# Program yang Menampilkan Kata yang Muncul Dalam Kedua File Text
def munculKata(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        linesFile1 = f1.readlines()
        linesFile2 = f2.readlines()
    # Memproses setiap baris dan memisahkan kata-kata
    wordsFile1 = []
    for line in linesFile1:
        for word in line.split():
            if word.isalpha():
                wordsFile1.append(word.lower())
    wordsFile2 = []
    for line in linesFile2:
        for word in line.split():
            if word.isalpha():
                wordsFile2.append(word.lower())
    # Memasukkan Kata Dalam Set
    tempatKata = set(wordsFile1).intersection(set(wordsFile2))
    print(tempatKata)

munculKata('romeo.txt', 'romeo-full.txt')

