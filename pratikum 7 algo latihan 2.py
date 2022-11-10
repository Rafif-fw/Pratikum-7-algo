# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:52:06 2022

@author: Rafif Fernanda
"""

def number():
 print("ordinal number")
 while True:
  print("Tekan 0 untuk menghentikan program")
  x = int(input('masukan angka:'))
  if(x == 1):
   print(x, ' st')
  elif(x == 2):
   print(x, ' nd')
  elif (x == 3) :
   print(x, 'rd')
  elif x == 0 :
   print(x,'th')   
   print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.\n")
   break
  else:
   print(x, 'th')
 
N = number()
print(N)