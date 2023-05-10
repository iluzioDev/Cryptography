#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 2023

@author: iluzioDev

This script implements functions, tests, algorithms, etc. used in some ciphers.
"""
import random

def fast_exponentiation(base, exponent, modulus):
  """Fast exponentiation algorithm.

  Args:
      base (int): Base number.
      exponent (int): Exponent number.
      modulus (int): Modulus number.
  """
  base = int(base)
  exponent = int(exponent)
  modulus = int(modulus)

  result = 1
  base = base % modulus
  while exponent > 0 and base > 1:
    if exponent % 2 == 1:
      result = (result * base) % modulus
      exponent = exponent - 1
    else:
      base = (base * base) % modulus
      exponent = exponent / 2
  return result

def lehman_peralta(x, n = 10):
  """
  Function that implements Lehman-Peralta primality test.

  Args:
    x (int): Number to be tested.
    n (int): Number of iterations. Defaults to 10.
    
  Returns:
    bool: True if x is prime, False otherwise.
  """
  # Step 1: Check special cases.
  if x <= 1:
    return False
  elif x <= 3:
    return True
  
  maybe_prime = False
  for i in range(n):
    # Step 2: Choose a random number a in the range [2, x - 1], both inclusive.
    d = round((x - 1) / 2)
    a = random.randint(2, d)
  
    # Step 3: Compute a^(x - 1)/2 mod x.
    result = pow(a, d, x)
  
    # If result is x - 1, then x is **probably** prime.
    if result == x - 1:
      maybe_prime = True
  
    # Step 4: If result is 1 or -1, then x is **probably** prime.
    if result == 1 or result == x - 1:
      continue
    # If result of a^(x - 1)/2 is not 1 or -1, then x is composite.
    else:
      return False
  # If all iterations resulted in 1, then x is composite.
  return maybe_prime

def euclid_extended(a, b):
  """
  Euclid's extended algorithm.

  Args:
    a (int): First number.
    b (int): Second number.

  Returns:
    tuple: Tuple containing the GCD, the x coefficient and the y coefficient.
  """
  if a == 0:
    return (b, 0, 1)
  else:
    g, y, x = euclid_extended(b % a, a)
    return (g, x - ((b // a) * y), y)
