#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 2023

@author: iluzioDev

This script implements RSA algorithm.
"""
import math
import RSA.modules.functions as functions
from RSA.modules.constants import *

def encrypt(message, e, n):
  """
  Encrypts a message using RSA algorithm.

  Args:
      message (str): Message to encrypt.
      e (int): Public exponent.
      n (int): Public modulus.

  Returns:
      str: Encrypted message.
  """
  message = ''.join([char for char in message.upper() if char in ALPHABET])
  block_size = math.floor(math.log(n, len(ALPHABET)))
  coded = []
  encrypted = []
  
  for i in range(0, len(message), block_size):
    block = message[i:i + block_size]
    if len(block) < block_size:
      block += "X" * (block_size - len(block))
    num = sum(ALPHABET.index(char) * pow(len(ALPHABET), block_size - 1 - j) for j, char in enumerate(block))
    coded.append(num)
    encrypted.append(functions.fast_exponentiation(num, e, n))
  
  print('Block size: ' + str(block_size))
  print(ROW)
  print('Message: ' + message)
  print(ROW)
  print('Coded message: ' + " ".join(str(num) for num in coded))
  print(ROW)
  
  return "".join(str(num) + " " for num in encrypted)

def main():
  """
  Main function of the script.
  """
  while(True):
    print(ROW)
    print('■                           WELCOME TO THE RSA CIPHER TOOL!                           ■')
    print(ROW)
    print('What do you want to do?')
    print('[1] RSA Cipher.')
    print('[0] Exit.')
    print(ROW)
    option = input('Option  ->  ')
    print(ROW)
  
    if int(option) not in range(2):
      print('Invalid option!')
      continue
    
    if int(option) == 0:
      break
  
    if int(option) == 1:
      p = int(input('Enter a prime number (p): '))
      print(ROW)
      if not functions.lehman_peralta(p):
        print('Not a prime number!')
        continue
      q = int(input('Enter a prime number (q): '))
      print(ROW)
      if not functions.lehman_peralta(q):
        print('Not a prime number!')
        continue
      d = int(input('Enter a number (d): '))
      print(ROW)
      
      n = (p - 1) * (q - 1)
      mcd, reverse, *_ = functions.euclid_extended(d, n)
      if reverse < 0:
        reverse = n + reverse
      if mcd != 1:
        print('Invalid number!')
        continue
      print('Euler\'s value: ' + str(reverse))
      print(ROW)
      
      message = input('Enter a message: ')
      print(ROW)
      
      encrypted = encrypt(message, reverse, p * q)
      print('Encrypted message: ' + encrypted)
  return
