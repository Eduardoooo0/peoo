num1 = float(input('digite o primeiro número:'))
num2 = float(input('digite o segundo número:'))
num3 = float(input('digite o terceiro número:'))
p = num1
if num2 > p :
  p = num2
  if num3 > p :
    #3,2,1
    p = num3
    s = num2
    t = num1
  elif num1 > num3 :
    #2,1,3
    p = num2
    s = num1
    t = num3
  else:
    #2,3,1
    p = num2
    s = num3
    t = num1
elif num3 > p :
  if num1 > num2 :
    #3,1,2
    p = num3
    s = num1
    t = num2
else:
  if num2 > num3 :
    #1,2,3
    p = num1
    s = num2
    t = num3
  else:
    #1,3,2
    p = num1
    s = num3
    t = num2
print(t,s,p)
