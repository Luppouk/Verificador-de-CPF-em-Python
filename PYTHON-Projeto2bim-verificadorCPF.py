cpfs = list()
qntdCpf = 0
qntdV = 0
qntdIv = 0
print("=" * 40)
print("{:^40}" .format("VERIFICADOR DE CPF"))
print("=" * 40)
r = input("Deseja iniciar o programa? s/n\n").lower().strip()
while r != 's' and r != 'n':
    r = input("Resposta inválida, tente novamente: ").lower().strip()
while r == "s":
    #pegar o CPF do usuário
    print("-" * 40)
    print("{:^40}" .format("INSIRA SEU CPF"))
    print("{:^40}" .format("apenas números, sem '.' ou '-'"))
    cpf = []
    num = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
    for c in range(11):
        aux = input(f"{c+1}° dígito: ").strip()
        while aux not in num:
            aux = input("Dígito inválido, tente novamente: ").strip()
        cpf.append(int(aux))
    print("-" * 40)

    #validação do primeiro dígito
    cpf1 = list(cpf[0:9])
    num1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    s1 = 0
    for c in range(len(cpf1)):
        s1 += num1[c] * cpf1[c]
    rest1 = s1 % 11
    if rest1 < 2:
        dig1 = 0
    else:
        dig1 = 11 - rest1

    #validação do segundo dígito
    cpf2 = list(cpf[0:9])
    cpf2.append(dig1)
    num2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    s2 = 0
    for c in range(len(cpf2)):
        s2 += num2[c] * cpf2[c]
    rest2 = s2 % 11
    if rest2 < 2:
        dig2 = 0
    else:
        dig2 = 11 - rest2
    cpf2.append(dig2)

    if cpf != cpf2 or cpf2[9] == cpf2[10]:
        cpfV = "Inválido"
        qntdIv += 1
    else:
        cpfV = "Válido"
        qntdV += 1
    print("CPF verificado: {}{}{}.{}{}{}.{}{}{}-{}{}" 
    .format(cpf[0],cpf[1],cpf[2],cpf[3],cpf[4],cpf[5],
    cpf[6],cpf[7],cpf[8],cpf[9],cpf[10]))
    print(f"Resultado: {cpfV}")
    print("-" * 40)
    dictAux = {"cpf" : cpf2, "validacao" : cpfV}
    cpfs.append(dictAux)
    qntdCpf += 1
    r = input("Gostaria de inserir mais um CPF? s/n\n").lower().strip()
    while r != 's' and r != 'n':
        r = input("Resposta inválida, tente novamente: ").lower().strip()

#cálculo da porcentagem e impressão do resultado
print("=" * 40)
if qntdCpf != 0:
    pV = (qntdV / qntdCpf) * 100
    pIv = (qntdIv / qntdCpf) * 100
    print(f"CPF's testados: {qntdCpf}\nCPF's válidos: {qntdV}\nCPF's inválidos: {qntdIv}")
    print("Porcentagem de CPF's válidos: {:.2f}%\nPorcentagem de CPF's inválidos: {:.2f}%" .format(pV, pIv))
else: 
    print(("{:^40}" .format("Não foi digitado nenhum cpf").upper()))
print("=" * 40)