r = []
for x in ["A", "C", "G", "T"]:
    for y in ["A", "C", "G", "T"]:
        for z in ["A", "C", "G", "T"]:
            r.append(x+y+z)

print(r)