salario = float(input('Qual o seu salário? '))
anoAdmissao = int(input('Em que ano foi admitido? '))
anoAtual = int(input('Digite o ano em que estamos: '))
tempoTrabalhado = anoAtual - anoAdmissao

if (tempoTrabalhado >= 5):
  salarioAtual = salario + (salario * 0.20)
  print('O seu salário terá uma bonificação de 20% e aumentará para R${}' .format(salarioAtual))
else:
  salarioAtual = salario + (salario * 0.10)
  print('O seu salário terá uma bonificação de 10% e aumentará para R${}' .format(salarioAtual))
