# Program yang mendemonstrasikan konversi list-set-tuple
def konversiListSet(inputList):
    print("PROGRAM KONVERSI LIST KE SET DAN SET KE LIST")
    listSet = set(inputList)
    print("List:", inputList, "ke Set:", listSet)
    print("Tipe Data Sebelum:", type(inputList), "Tipe Data Sesudah:", type(listSet))
    listAwal = list(listSet)
    print("Set:", listSet, "ke List:", listAwal)
    print("Tipe Data Sebelum:", type(listSet), "Tipe Data Sesudah:", type(listAwal))
    print()

def konversiTupleSet(inputTuple):
    print("PROGRAM KONVERSI TUPLE KE SET DAN SET KE TUPLE")
    tupleSet = set(inputTuple)
    print("Tuple:", inputTuple, "ke Set:", tupleSet)
    print("Tipe Data Sebelum:", type(inputTuple), "Tipe Data Sesudah:", type(tupleSet))
    tupleAwal = tuple(tupleSet)
    print("Set:", tupleSet, "ke Tuple:", tupleAwal)
    print("Tipe Data Sebelum:", type(tupleSet), "Tipe Data Sesudah:", type(tupleAwal))
    print()

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
konversiListSet(data1)
data2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
konversiTupleSet(data2)

