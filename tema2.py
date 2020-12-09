# Cerinta 1
"""
def calculator(*argumente):
    sum=0
    for x in argumente:
        try:
            x+=0
        except TypeError:
            pass
        else:
            sum+=x
    print(sum)


calculator(1,2,8, "asdas", 10)
"""

#Cerinta 2

"""
import operator

def recursiva(n):
    #(tot, par, impar) = recursiva(n-1)
    if(n==0):
        return [0,0,0]
    else:
        if(n%2==0):
             return list(map(operator.add, [n,n,0], recursiva(n-1)))
        else:
             return list(map(operator.add, [n, 0, n], recursiva(n - 1)))

        #Recunosc, nu m-as fi gandit singur sa returnez liste sau tuple-uri
        #pentru a avea o singura functie ce returneaza toate valorile
        #insa asta e tot ce am copiat, idea. In rest m

print('Rezultatul este: ', recursiva(9))

"""

#Cerinta 3

"""
def verif_int(n):
    if(isinstance(n, int)):
        print("Este numar intreg")
    else:
        print("0")

verif_int("100")
"""
