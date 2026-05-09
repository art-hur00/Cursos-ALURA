
def exer1():
    numero_escolhido = int(input("Escolha uma numero: "))
    verfnm = numero_escolhido % 2
    if verfnm == 0:
        print('O numero e par!')
    else:
        print("O numero e impar")

def exer2():
    idd = int(input("Qual a sua idade?\n(Responda apenas em numeros!) "))
    if idd < 0 or idd > 120:
        print("Por favor nao minta.")
    else:
        if idd <= 12:
            print("crianca")
        elif idd <=18:
            print("Adolecente")
        else:
            print('Adulto')

def exer3():
    
    respEspNm = ("cavalo")
    respEspSn = (int("12"))
    
    respUsNm = (input("Insira seu nome: "))
    respUsSn = (int(input("Insira sua senha: ")))
    
    if respUsNm != respEspNm and respUsSn != respEspSn:
        print("Usuario e senha incorretos")
    elif respUsNm != respEspNm:
        print("Usuario incorreto")
    elif respUsSn != respEspSn:
        print("Senha incorreta")
    elif respUsNm != respEspNm and respUsSn == respEspSn:
        print("Usuario incorreto, Senha Correta")
    elif respUsNm == respEspNm and respUsSn != respEspSn:
        print("Usuario Correto, Senha Incorreta")
    elif respUsNm == respEspNm and respUsSn == respEspSn:
        print("Usuario Correto, Senha Correta! \nBem Vindo Sr.Cavalo")
    else:
        print("Deu merda.")

def exer4():

    cordX = int(input("Insira a cordenada: X: "))
    cordY = int(input("Insira a cordenada: Y: "))

    if cordX > 0 | cordY > 0:
        print("Primeiro Quadrante")
    elif cordX < 0 | cordY > 0:
        print("Segundo Quadrante")
    elif cordX < 0 | cordY < 0:
        print("Terceiro Quadrante")
    elif cordX > 0 | cordY < 0:
        print("Quarto Quadrante")
    else:
        print("o ponto está localizado no eixo ou origem.")

def main():
    exer4()
    
if __name__ == '__main__':
    main()