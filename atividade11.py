#importação de função externa
from fun import f_padraoA, f_padraoB, f_padraoC, f_padraoD, f_padraoE, f_padraoF

def main():
  #declaração de variável local
  opcao = str()
  caracter = str()
  
  #entrada de dados
  opcao = input()
  #processamento de dados
  while(opcao == "a" or opcao == "b" or opcao == "c" or opcao == "d" or opcao == "e" or opcao == "f"):
    caracter = input()
    #processamento de dados
    if(opcao == "a"):
      #invocação de função
      print(f_padraoA(caracter))

    if(opcao == "b"):
      #invocação de função
      print(f_padraoB(caracter))
      
    if(opcao == "c"):
      #invocação de função
      print(f_padraoC(caracter))

    if(opcao == "d"):
      #invocação de função
      print(f_padraoD(caracter))

    if(opcao == "e"):
      #invocação de função
      print(f_padraoE(caracter))

    if(opcao == "f"):
      #invocação de função
      print(f_padraoF(caracter))

    opcao = input()
    

  return 0
if __name__=="__main__":
  main()
