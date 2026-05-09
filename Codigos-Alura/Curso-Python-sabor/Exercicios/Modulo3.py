def exer1():
    ordem = [1,2,3,4,5,6,7,8,9,10]
    nomes = ["Joao", "Maria", "Fernando", "Marcela"]
    eu = [2003, "Arthur"]
    print(ordem,"\n",nomes,"\n",eu)

def exer2():
    lista = [1,2,3,4,5,6,7,8]
    for numero in lista:
        print(f'--> {numero}')

def exer3():
    lst= [1,2,3,4,5,6,7,8,9,10]
    smImpr = 0
   
    for numero in lst:
        if numero % 2 != 0:
            smImpr += numero
    
    print(smImpr)

def exer4():
    lst= [10,9,8,7,6,5,4,3,2,1]
    cntdr = 11
   
    for numero in lst:
            if numero < cntdr:
                print(numero)
                cntdr -= 1
                continue

def exer5():
    lst = []
    cntdr = 0

    lst.append(int(input("Insira um valor: ")))
    print(lst)

    for numero in lst:
     while cntdr < 11:
      print(numero * cntdr)
      cntdr +=1

 
def exer6():
    lst = [1,2,3,4,5,6,7,8,9,10]     
    sm = 0

    for numero in lst:
        sm += numero
    
    print(sm)

def main():
    exer6()
if __name__ == '__main__':
    main()