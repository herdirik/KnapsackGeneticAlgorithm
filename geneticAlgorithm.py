
file  = open("test1.txt", "r")
satirlar=file.readlines()
list =[]
randomlist=[]

for satir in satirlar:
    list.append(satir.strip(('[\n]')))

for eleman in list[0].split(","):
    randomlist.append(eleman.strip("''"))

populasyon_boyutu=list[1]

file.close()