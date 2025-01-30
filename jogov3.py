# foram feitas melhorias no código, como a validação de entrada e a possibilidade de jogar novamente

import random as rd

def jogar():
    print('Bem-vindo ao jogo!')

    while True:
        # Gerar um número aleatório entre 1 e 50
        numero_secreto = rd.randint(1, 50)
        tentativas = 10  # Número total de tentativas
        palpites_lancados = []
        print(f'Você tem {tentativas} tentativas para acertar o número entre 1 e 50.')

        for tentativa in range(1, tentativas + 1):
            palpite = input(f'Tentativa {tentativa}: Digite um número: ')

            if palpite in palpites_lancados:
                print('Esse numero já foi lançado. tente outro.')
                continue
            else:
                palpites_lancados.append(palpite)

            # Validação da entrada
            if not palpite.isdigit():
                print('Entrada inválida! Digite apenas números.')
                continue

            palpite = int(palpite)

            # Verifica se o palpite está dentro do intervalo
            if palpite < 1 or palpite > 50:
                print('O número deve ser entre 1 e 50. Você perdeu uma tentativa.')
                continue

            # Verifica se o palpite está correto
            if palpite == numero_secreto:
                print(f'Acertou! O número era {numero_secreto}. Você acertou na tentativa {tentativa}.')
                break
            elif palpite < numero_secreto:
                print(f'Tentativa {tentativa}: O número é maior que {palpite}.')
            else:
                print(f'Tentativa {tentativa}: O número é menor que {palpite}.')

            # Exibir tentativas restantes
            if tentativa < tentativas:
                print(f'Tentativas restantes: {tentativas - tentativa}')
                print(f"Palpites já feitos: {palpites_lancados}")

        else:
            print(f'Você perdeu todas as chances. O número era {numero_secreto}.')
            
        # Perguntar se o jogador deseja jogar novamente
        novo_jogo = input('Deseja jogar novamente? (s/n) ').lower()
        if novo_jogo != 's':
            print('Obrigado! Até a próxima.')
            break

# Iniciar o jogo
jogar()