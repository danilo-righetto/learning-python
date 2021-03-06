print("*********************************")
print("*********Usando o FOR************")
print("*********************************")

for item in range(1, 10):
    print(item)


total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas):
    print("Tentativa", rodada, "de", total_de_tentativas)
    print("Tentativa {} de {}", format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100!")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")