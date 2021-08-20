import random

#def generateTripletString(length):
#    result = ""
#    for x in range(length):
#        tripl = ""
#        for i in range(3):
#            tripl += random.choice(["A", "C", "G", "T"])
#        result += tripl
#
#    return result
#
#def splitTripletString(string, n):
#    return [string[i:i+n] for i in range(0, len(string), n)]

# "ACG", "ATG", "GGG", "GACA"
# ["ACG", "ATG"]


def generateTripletList(length):
    result = []
    for x in range(length):
        tripl = ""
        for i in range(3):
            tripl += random.choice(["U", "C", "A", "G"])
        result.append(tripl)

    return result

def countTriplets(list):
    r = {}
    # list = ["AGG", "CCA", "TTG"]
    for i in list:
        # i = "AGG"
        if i not in r:
            r[i] = 1
        else:
            r[i] += 1
    # r = {"AGG" : 1, "CCA" : 1, "TTG" : 1}
    return r

def display(dic):
    # dic = {"AGG" : 1, "CCA" : 1, "TTG" : 1}
    for key in dic:
        # key = "AGG"
        print(f"{key} = {dic[key]}")
        # "AGG = 1"

x = generateTripletList(1000)
c = countTriplets(x)
display(c)

dict =  {
    "UUU" : "Phenylalanin",
    "UUC" : "Phenylalanin"
}

triplet = input("Type in triplet: ")