
def sestevek(sez):
    print(sum(sez))

def average(sez):
    print(sum(sez)/ len(sez))

def najvecji(sez):
    print(max(sez))
    
def najmanjsi(sez):
    print(min(sez))

def st_lihih(sez):
    stevec = 0
    for i in sez:
        if i%2==1:
            stevec+=1
    print("st lihih: " , stevec)


def izpis_vecjih_od(sez):
    for i in sez:
        if i>10:
            print(i)



def main():
    sez = [12,5,8,21,3,16,9,14]
    sestevek(sez)
    average(sez)
    najvecji(sez)
    najmanjsi(sez)
    st_lihih(sez)
    izpis_vecjih_od(sez)
    sez.sort()
    print(sez)
    a = int(input("vpisi stevilo "))
    sez.append(a)
    print(a)
    a = int(input("vpisi stevilo "))
    if a in sez:
        sez.remove(a)
    else:
        print("to st ne obstaja v seznamu")
        
main()