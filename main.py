# Author: Yan Lu yfl5541@psu.edu
# Collaborator: Spoorthi Dhulappanavar sxd5682@psu.edu
# Collaborator: Nicole Giron nqg5259@psu.edu
# Collaborator: Xiaolong Lin xxl5453@psu.edu
# Section: 4
# Breakout: 11
def sum_n(n):
  if n<=0 :
    return 0
  else :
    sum = n + sum_n(n-1)
    return sum

def print_n(s, n):
  if n == 0:
    return
  else: 
   print(s)
   print_n(s,n-1)

def run():
  num = int(input("Enter an int: "))
  print(f"sum is {sum_n(num)}.")
  stri = input("Enter a string: ")
  print_n(stri,num)

if __name__ == "__main__":
  run()