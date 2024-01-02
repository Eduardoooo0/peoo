num = 1
m1 = m2 = m3 = m4 = 0
while not num == 0:
  num = int(input('Digite um número:'))
  if num >= 1 and num <= 25:
    m1 += 1
  elif num >= 26 and num <= 50:
    m2 += 1
  elif num >= 51 and num <= 75:
    m3 += 1
  elif num >= 76 and num <=100:
    m4 += 1
print(f'Intervalos\n[1 - 25]: {m1} número(s)\n[26 - 50]: {m2} número(s)\n[51 - 75]: {m3} número(s)\n[76 - 100]: {m4} número(s)')
    