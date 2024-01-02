def main():
  while True:
    n = int(input('Digite um número ou [0] para sair :'))
    if n == 0:
      break
    else:
      print(codificar(n))
def codificar(a):
  string = str(a)
  s = string.replace('0','O').replace('1','I').replace('2','Z').replace('3','E').replace('4','A').replace('5','S').replace('6','R').replace('7','T').replace('8','B').replace('9','P')
  return s
if __name__ == '__main__':
    main() 