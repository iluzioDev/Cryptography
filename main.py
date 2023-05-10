#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed 10 May 2023

@author: iluzioDev

This script implements a menu to choose the encryption mode.
"""
from AES.aes import main as aes
from CBC.cbc import main as cbc
from ChaCha20.ChaCha20 import main as chacha20
from DiffieHellman.DiffieHellman import main as diffiehellman
from EllipticCurve.EllipticCurve import main as ellipticcurve
from GPSL1CA.gpsl1ca import main as gpsl1ca
from RC4.RC4 import main as rc4
from RSA.rsa import main as rsa
from RSASIGNATURE.rsasignature import main as rsa_signature
from Snow3GAESMult.snow3g_aes_mult import main as snow3g_aes_mult
from vigenere.vigenere import main as vigenere

ROW = '■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'

def main():
  """
  Main function
  """
  while(True):
    print(ROW)
    print('■                 WELCOME TO THE RSA SIGNATURE MODE!                 ■')
    print(ROW)
    print('What do you want to do?')
    print('[1] AES.')
    print('[2] CBC.')
    print('[3] ChaCha20.')
    print('[4] Diffie-Hellman.')
    print('[5] Elliptic Curve.')
    print('[6] GPS L1CA.')
    print('[7] RC4.')
    print('[8] RSA.')
    print('[9] RSA Signature.')
    print('[10] Snow3G-AES-Mult.')
    print('[11] Vigenere.')
    print('[0] Exit.')
    print(ROW)
    option = input('Option  ->  ')
    print(ROW)
    
    if int(option) not in range(12):
      print('Invalid option!')
      continue
    
    if option == '0':
      print('See you soon!')
      print(ROW)
      break
    
    if int(option) == 1:
      aes()
      continue
    if int(option) == 2:
      cbc()
      continue
    if int(option) == 3:
      chacha20()
      continue
    if int(option) == 4:
      diffiehellman()
      continue
    if int(option) == 5:
      ellipticcurve()
      continue
    if int(option) == 6:
      gpsl1ca()
      continue
    if int(option) == 7:
      rc4()
      continue
    if int(option) == 8:
      rsa()
      continue
    if int(option) == 9:
      rsa_signature()
      continue
    if int(option) == 10:
      snow3g_aes_mult()
      continue
    if int(option) == 11:
      vigenere()
      continue
    
  return

if __name__ == '__main__':
  main()
