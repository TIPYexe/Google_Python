#1
list = [7,8,9,2,3,1,4,10,5,6]
#print(list)

#2
lista_asc = list.copy()
lista_asc.sort()
print(lista_asc)

#3
lista_desc = list.copy()
lista_desc.sort(reverse=True)
print(lista_desc)

#4
print(lista_asc[1::2])

#5
print(lista_asc[0::2])

#6
for x in list:
    if x%3==0:
        print(x,end="")
        print(" ", end="")
