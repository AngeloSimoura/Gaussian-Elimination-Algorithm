# -*- coding: utf-8 -*-
"""Atividade Avaliativa 01_CalcNumerico.ipynb
"""

#Questão 1
import random
n=3
A = []
B = []
X = []
S=0
SPI="Possível e Indeterminado"
SPD="Possível e Determinado"
SI="Impossível"


#funcao que classifica em SPI,SPD ou SI
def classifica():
    T=0
    for i in range (0,n):
        for j in range(0,n):
            T+=A[i][j]
        if T==0:
          if B[i]==0:
              return SPI
          else:
              return SI
        else:
            T=0
    return SPD

#criação da matriz A
for i in range(n):
    A = A + [[0]*n] # cria uma nova lista [0]*n

#criação do vetor resultado
for i in range(n):
    X.append(0)

#copulação das matriz A e vetor B com números aleatórios
for x in range(0,n,1):
    for y in range(0,n,1):
      #print("Digite um valor para a linha %i e coluna %i : " %(x, y)) #print(f'{"Digite um valor para a linha "}{x}{" e coluna "}{y}{"da matriz A: "}')
      #A[x][y]=float(input(f'{"Digite um valor para a linha "}{x}{" e coluna "}{y}{" da matriz A: "}'))
      A[x][y]=random.randint(1,10)

for x in range(0,n,1):
    #B.append(float(input(f'{"Digite um valor para a posicao "}{x}{" do vetor dos termos independentes: "}')))
    B.append(random.randint(1,10))

#matriz e vetor teste    
'''

A=[
   [1 ,4  ,52],
   [27,110,-3],
   [22,2  ,14]
   ]

B=[
   57,
   134,
   38
   ]

'''

#printar matriz A e vetor B gerados
print("\nMatriz A:")
for i in range(n):    
  print(A[i])

print("\nVetor dos Termos Independentes B:")
for i in range(n):    
  print(B[i])

#algoritmo Eliminação de Gauss
for i in range(0,n-1):
    maxValor = A[i][i] #pivo
    maxLinha = i
    for j in range(i,n-1):
        if abs(maxValor) < abs(A[j+1][i]):
            maxValor=A[i+1][j];
            maxLinha=j+1;
    if maxValor != A[i][i]:
        for cont in range(0,n):
            aux = A[i][cont]
            A[i][cont]=A[maxLinha][cont]
            A[maxLinha][cont]=aux;
            aux=B[i]
            B[i]=B[maxLinha]
            B[maxLinha]=aux
    for j in range(i+1,n):
        fator=A[j][i]/A[i][i]
        A[j][i]=0
        for k in range(i+1,n):
            A[j][k]=A[j][k]-(fator*A[i][k])
        B[j]=B[j]-(fator*B[i])


#def pivoteamentoParcial(A,B,i):

#printar resultados
print("\nMatriz A na forma de matriz triangular superior=")
for i in range(n):    
  print(A[i])
  #print(f'{A[i]}{" ["}{B[i]}{"]"}')

print("\nVetor dos Termos Independentes B após algoritmo:")
for i in range(n):    
  print(B[i])


#chama a função que classifica o sistema e printa o resultado
C=classifica()
print(f'\nSistema {C}')

#printa o vetor resultado somente se o sistema for Possível e Determinado
if C==SPD:
    print("\n\nVetor Resultado:")
    #Questão 2
    X[n-1]=B[n-1]/A[n-1][n-1]
    for i in range(n-1,-1,-1):
      for j in range(i+1,n):
        S+=A[i][j]*X[j]
      X[i]=(B[i]-S)/A[i][i]
      S=0    
    print(f'X:{X}')

