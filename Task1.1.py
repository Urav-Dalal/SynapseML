modern_family=['CLaiRe_DunPhY','PHiL_dUnpHY','GLoRiA_PriTCheTt','CaMErOn_TuCKEr','StELLa']
indices = [index for index,y in enumerate(modern_family)]
characters=[]
for item in modern_family:
    characters.append(item)

for i in range(len(characters)):
    characters[i]=characters[i].lower()

for j in range(len(characters)):
    characters[j]=characters[j].replace("_","-")


temp=list(map(lambda a:len(a),characters))


indices = [sum(p) for p in zip(indices,temp)]


indices.sort(reverse = True)

Phew_finally = {indices[m]:characters[m] for m in range(len(characters))}
print(Phew_finally)
