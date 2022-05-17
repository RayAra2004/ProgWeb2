def f_padraoA(c):
  #declaração de variável local
  i = int()
  pa = str()
  #processamento de dados
  for i in range(6):
      #saída de dados
      pa += c * 6 + "\n"

  return pa

def f_padraoB(c):
  #declaração de variável local
  i = int()
  pa = str()
  #processamento de dados
  for i in range(1,7):
    #saída de dados
    pa += c * i + "\n"

  return pa
  
def f_padraoC(c):
  #declaração de variável local
  p = str()
  l = int()
  i = int()
  pa = str()
  #inicialização de varável
  p = " "
  l = 1
  #processamento de dados
  for i in range(5,-1,-1):
    #saída de dados
    pa += p * i + c * l + "\n"
    #processamento de dados
    l += 1

  return pa

def f_padraoD(c):
  #declaração de variável local
  p = str()
  k = int()
  i = int()
  j = int()
  pa = str()
  #inicialização de variável
  p = " "
  k = 3
  #processamento de dados
  for i in range(1,8,2):
    #saída de dados
    pa += p * k + c * i + p * k + "\n"
    #processamento de dados
    k -= 1
  #inicialização de variável
  k = 1
  #processamento de dados
  for j in range(5,0,-2):
    #saída de dados
    pa += p * k + c * j + p * k + "\n"
    #processamento de dados
    k += 1

  return pa

def f_padraoE(c):
  #declaração de variável local
  i = int()
  pa = str()
  #processamento de dados
  for i in range(6,0,-1):
    #saída de dados
    pa += c * i + "\n"

  return pa
    
def f_padraoF(c):
  #declaraçãode variável local 
  i = int()
  p = str()
  a = int()
  pa = str()
  #inicialização de variável
  p = " "
  a = 0
  #processamento de dados
  for i in range(6,0,-1):
    #saída de dados
    pa += p * a + c * i + "\n"
    #processamento de dados
    a += 1

  return pa
