
file  = open("test1.txt", "r")
satirlar=file.readlines()

list =[]
randomlist=[]
eleman_agirliklariList=[]
eleman_degerleriList=[]
populasyonList=[]

for satir in satirlar:
    list.append(satir.strip(('[\n]')))

for eleman in list[0].split(","):
    randomlist.append(float(eleman.strip("''")))

for eleman in list[6].split(","):
    eleman_agirliklariList.append(int(eleman))

for eleman in list[7].split(","):
    eleman_degerleriList.append(int(eleman))

populasyon_boyutu=list[1]
turnuvaEleman_sayisi=list[2]
mutasyon_olasiligi = list[3]
iterasyon_sayisi=list[4]
canta_boyutu=int(list[5])
print(canta_boyutu)

count = 0
randomlist_boyut=len(randomlist)
for i in range(int(populasyon_boyutu)):
    eleman = ''
    eleman_agirlik = 0
    eleman_deger = 0
    for j in range(len(eleman_agirliklariList)):
        if randomlist[count%randomlist_boyut] < 0.5:
            eleman+='0'
        else:
            eleman+='1'
            eleman_agirlik += eleman_agirliklariList[j]
            eleman_deger += eleman_degerleriList[j]

        count+=1
    evaluate = eleman_deger if eleman_agirlik <= canta_boyutu else 0
    populasyonList.append((eleman,evaluate))
print (populasyonList)



file.close()