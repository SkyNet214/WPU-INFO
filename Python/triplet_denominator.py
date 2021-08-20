dict =  {
    "UUU" : "Phenylalanin",
    "UUC" : "Phenylalanin",
    "ACU" : "Threonin"
}

while True:
    try:
        triplet = input("Type in triplet: ")
        print(dict[triplet])
    except:
        print("unknown")