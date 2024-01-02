class ContaCorrente:
  def __init__(self):
    self.saldo = 0
    self.nome = ''
  def VerSaldo(self):
    print(f'Seu saldo atual é R$ {self.saldo}')
  def Depositar(self):
    self.valor = float(input('Digite o valor que deseja depositar:'))
    self.saldo += self.valor
    print(f'Foram depositados R$ {self.valor} em sua conta')
  def Sacar(self):
    self.valor = float(input('Digite o valor que deseja sacar:'))
    if self.valor > self.saldo:
      raise Exception(f'Saldo insuficiente')
    self.saldo -= self.valor
    print(f'Foram sacados R$ {self.valor} da sua conta')
app = ContaCorrente()
app.nome = input('Digite seu nome:')
while True:
try:
  print('Menu:\n1 - Saldo\n2 - Depositar\n3 - Sacar\n4 - Sair')
  opcao = input('Digite a opção desejada:')
  if opcao == '1':
    app.VerSaldo()
  elif opcao == '2':
    app.Depositar()
  elif opcao == '3':
    app.Sacar()
  elif opcao == '4':
    break
except Exception as erro:
  print(f'Erro: {erro}')