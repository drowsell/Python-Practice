import os
import time

def make(amount):

  dot = 0

  for j in range(50): 
    for k in range(50):
      if dot == k:
        print(".", end = '')
      else:
        print(" ", end = '')
    dot = dot + 1
    print("\033[H\033[J")
        

                
          
make(2)
