import random as rd

print("Bem-vindo ao Jogo de Adivinhação!")
pontuacao = []  # Inicializa a lista de pontuações
print("Escolha o nível de dificuldade:")
print("1. Fácil (10 tentativas)")
print("2. Médio (7 tentativas)")
print("3. Difícil (5 tentativas)")

while True:
    dificuldade = input("Digite o número da dificuldade desejada: ")
    if dificuldade == "1":
        tentativas_totais = 10
        break
    elif dificuldade == "2":
        tentativas_totais = 7
        break
    elif dificuldade == "3":
        tentativas_totais = 5
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

while True:
    numero_secreto = rd.randint(1, 100)
    tentativas_restantes = tentativas_totais
    tentativas = 0
    palpites_feitos = []
    print("\nEu pensei em um número entre 1 e 100.")
    print(f"Você tem {tentativas_totais} tentativas para adivinhar.")

    # Loop de Tentativas
    while tentativas_restantes > 0:
        palpite = input("\nDigite o seu palpite: ")
        # Verificando se o input é um número válido
        if not palpite.isdigit():
            print("Por favor, digite um número válido.")
            continue
        palpite = int(palpite)
        if palpite in palpites_feitos:
            print("Você já tentou esse número. Tente outro.")
            continue
        else:
            palpites_feitos.append(palpite)
            tentativas += 1
            tentativas_restantes -= 1
            print(f"Palpites já feitos: {palpites_feitos}")

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            pontuacao_partida = tentativas_restantes * 10 * (int(dificuldade))  # Cálculo da pontuação
            pontuacao.append(pontuacao_partida)  # Adiciona a pontuação à lista
            print(f"Sua pontuação nesta partida: {pontuacao_partida} pontos.")
            break
        elif palpite < numero_secreto:
            print("O número é maior que esse.")
        else:
            print("O número é menor que esse.")
        print(f"Tentativas restantes: {tentativas_restantes}")
    else:
        print(f"\nQue pena! Você não conseguiu adivinhar. O número era {numero_secreto}.")
        pontuacao.append(0)  # Adiciona 0 à lista de pontuações se o jogador não acertar

    # Exibindo o Placar
    print("\nPlacar:")
    for idx, pontos in enumerate(pontuacao, start=1):
        print(f"Partida {idx}: {pontos} pontos")
    
    # Perguntar se o jogador quer jogar novamente
    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar! Até a próxima.")
        break