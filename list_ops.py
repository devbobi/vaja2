
def sestevek(sez):
    print(sum(sez))

def average(sez):
    print(sum(sez)/ len(sez))

def najvecji(sez):
    print(max(sez))
    
def najmanjsi(sez):
    print(min(sez))
    
def main():
    sez = [12,5,8,21,3,16,9,14]
    sestevek(sez)
    average(sez)
    najvecji(sez)
    najmanjsi(sez)
main()