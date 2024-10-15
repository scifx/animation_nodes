from ... data_structures cimport DoubleList, BooleanList, LongList
from ... algorithms.random_number_generators cimport XoShiRo256Plus

def convert_DoubleList_to_BooleanList(DoubleList inList):
    cdef BooleanList outList = BooleanList(length = inList.length)
    cdef long i
    for i in range(len(inList)):
        outList.data[i] = inList.data[i] != 0
    return outList

def convert_LongList_to_BooleanList(LongList inList):
    cdef BooleanList outList = BooleanList(length = inList.length)
    cdef long i
    for i in range(len(inList)):
        outList.data[i] = inList.data[i] != 0
    return outList

def convert_BooleanList_to_LongList(BooleanList inList):
    cdef LongList outList = LongList(length = inList.length)
    cdef long i
    for i in range(len(inList)):
        outList.data[i] = 1 if inList.data[i] != 0 else 0
    return outList

def convert_BooleanList_to_DoubleList(BooleanList inList):
    cdef DoubleList outList = DoubleList(length = inList.length)
    cdef long i
    for i in range(len(inList)):
        outList.data[i] = 1 if inList.data[i] != 0 else 0
    return outList

def generateRandomBooleans(Py_ssize_t seed, Py_ssize_t count, float probablity):
    cdef Py_ssize_t i
    cdef XoShiRo256Plus rng = XoShiRo256Plus(seed)
    cdef BooleanList bools = BooleanList(length = count)
    for i in range(count):
        bools.data[i] = rng.nextFloat() < probablity
    return bools
