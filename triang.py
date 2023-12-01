def is_triang():
  strn = input()
  sides = strn.strip().split()

  a = int(sides[0])
  b = int(sides[1])
  c = int(sides[2])
  if (a + b > c) and (b + c > a) and (c + a > b):
    return True
  else:
    return False

print(is_triang())