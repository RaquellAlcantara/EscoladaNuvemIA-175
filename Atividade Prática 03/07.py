n1 = input("Digite a primeira Nota: ")
n2 = input("Digite a segunda Nota: ")
n3 = input("Digite a terceira Nota: ")
n4 = input("Digite a quarta Nota: ")

media = ((n1 * 2) + (n1 * 3) + (n1 *4) + (n1 * 1)) / 10

print (f"A média é: {media:.1f}")

if media  >= 7.0:
    print("Aluno aprovado")

if media  <= 5.0:
    print("Aluno aprovado")

else:
    print("Aluno em exame")

    exame  = float(input("Digite aa noota o exame: "))
    print(f"A nota do exame: ")

    media_final = (media + exame) / 2
    if media_final >= 5.0:
        print("Alunoo aprovado")
    else:
        print("Aluno reprovado")

    print(f"A média final é: {media_final:.1f}")


