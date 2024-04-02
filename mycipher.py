import sys

def main():
  shift = check(sys.argv)
  new_message = ""
  alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  for char in sys.stdin:
    char = char.lower()
    if char in alpha:
      index = alpha.index(char)
      if (index + shift) <= 26:
        index += shift
        new_message += alpha[index].upper()
      else:
        index = index + shift - 26
        new_message += alpha[index].upper()
  for i in range(len(new_message)):
    if (i+1) % 50 == 0 and i != 0:
      print(new_message[i], end="\n")
    elif (i+1) % 5 == 0 and i != 0:
      print(new_message[i], end=" ")
    else:
      print(new_message[i], end="")
