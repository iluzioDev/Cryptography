#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 2023

@author: iluzioDev

This script implements the multiplication used in the SNOW 3G and AES algorithms.
"""
import Snow3GAESMult.lfsr
import functools

ROW = '■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'

SNOW3G_BYTE = '10101001'
AES_BYTE = '00011011'

def mult(byte1, byte2, algorithm_byte):
  """This function implements the multiplication used in the SNOW 3G and AES algorithms.

  Args:
      byte1 (str): First byte to be multiplied
      

  Returns:
      str: Result of the multiplication.
  """
  if type(byte1) is not str and type(byte2) is not str and type(algorithm_byte) is not str:
    return None
  
  length = len(byte1) if len(byte1) > len(byte2) else len(byte2)
  byte1 = byte1.zfill(length)
  byte2 = byte2.zfill(length)
  
  exponents = lfsr.binary_to_polynomial(byte2)
  
  if len(algorithm_byte) < length:
    algorithm_byte = algorithm_byte.zfill(length)
  
  result = []
  
  for i in exponents:
    if i == '1':
      result.append(byte1)
    else:
      aux = byte1
      for j in range(int(i[1:])):
        overflow = aux[0]
        aux =  aux[1:] + '0'
        if overflow == '1':
          aux = lfsr.xor(aux, algorithm_byte)
      result.append(aux)
      
  if len(result) != 0:
    result = functools.reduce(lfsr.xor, result)
  else:
    result = '0' * length
  return result

def modified_mult(byte1, integer):
  """This function implements the modified multiplication used in the SNOW 3G algorithm.
  """
  if type(byte1) is not str and type(integer) is not int:
    return None
  
  length = len(byte1)

  result = byte1
  power = integer
  for i in range(power):
    overflow = result[0]
    result =  result[1:] + '0'
    if overflow == '1':
      result = lfsr.xor(result, SNOW3G_BYTE)
  
  return result

def modified_function(byte1, integer1 = 16, integer2 = 39, integer3 = 6, integer4 = 64):
  if type(byte1) is not str and type(integer1) is not int and type(integer2) is not int and type(integer3) is not int and type(integer4) is not int:
    return None

  result = []
  result.append(modified_mult(byte1, integer1))
  result.append(modified_mult(byte1, integer2))
  result.append(modified_mult(byte1, integer3))
  result.append(modified_mult(byte1, integer4))

  return result

def main():
  """Main function of the script.
  """
  while(True):
    print(ROW)
    print('■      WELCOME TO THE SNOW 3G AND AES MULTIPLICATION TOOL      ■')
    print(ROW)
    print('What do you want to do?')
    print('[1] SNOW 3G multiplication.')
    print('[2] AES multiplication.')
    print('[3] Convert hexadecimal to binary.')
    print('[4] Modified SNOW 3G multiplication.')
    print('[0] Exit.')
    print(ROW)
    option = input('Option  ->  ')
    print(ROW)
  
    if int(option) not in range(5):
      print('Invalid option!')
      continue

    if option == '0':
      print('See you soon!')
      print(ROW)
      break
    
    if option == '1':
      print('SNOW 3G multiplication.')
      print(ROW)
      print('Please, enter the two bytes to be multiplied.')
      byte1 = input('Byte 1  ->  ')
      byte2 = input('Byte 2  ->  ')
      print(ROW)
      print('Result: ' + mult(byte1, byte2, SNOW3G_BYTE))
    
    if option == '2':
      print('AES multiplication.')
      print(ROW)
      print('Please, enter the two bytes to be multiplied.')
      byte1 = input('Byte 1  ->  ')
      byte2 = input('Byte 2  ->  ')
      print(ROW)
      print('Result: ' + mult(byte1, byte2, AES_BYTE))
      
    if option == '3':
      hexadecimal = input('Hexadecimal number  ->  ')
      print(ROW)
      print('Result: ' + bin(int(hexadecimal, 16))[2:])

    if option == '4':
      print('Modified SNOW 3G multiplication.')
      print(ROW)
      print('Please, enter the byte to be multiplied.')
      byte1 = input('Byte 1  ->  ')
      print(ROW)
      print('Result: ' + str(modified_function(byte1)))
  return
