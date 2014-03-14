#!/usr/bin/python


def aproximacionpi(n):
  suma=0.0
  for i in range (1,n+1):
    a = float (i-1)/n
    b = float (i)/n
    xi = ((i)-(0.5)) / float(n)
    fxi = 4.0/(1.0 + xi*xi)
    suma += fxi
  s = suma / float (n)
  return s
 
 
n = int(raw_input('Introduzca el numero de intervalos: '))
veces = int(raw_input('Introduzca el numero de veces: '))
while n <= 0:
  print 'El numero de intervalos debe ser mayor que 0'
  n = int(raw_input('Introduzca el numero de intervalos: '))
l=[]
for i in range (1,veces+1):
  api = aproximacionpi(n*i)
  l = l+[api]
print l  

  
