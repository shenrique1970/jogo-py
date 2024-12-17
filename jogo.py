import random as rd  # Importa o módulo random e o renomeia como rd

# O jogador deverá escolher um número inteiro qualquer entre 0 e 50.
ns = rd.randint(0, 50)  # Gera um número secreto aleatório entre 0 e 50

# Nomeando as jogadas na forma de tupla
jogadas = ("Primeira", "Segunda", "Terceira", "Quarta", "Quinta", "Sexta",
           "Setima", "Oitava", "Nona", "Decima")  # Tupla com os nomes das jogadas

# Você terá 10 tentativas para acertar qual foi o número oculto gerado
# pelo computador no intervalo (0 a 50).
# Contador de tentativas (inicia em 1)
c = 1
# Contador de chances restantes (inicia em 9, total de 10 tentativas)  
f = 9  

print(ns)  # Exibe o número secreto (para fins de depuração)

# Loop percorrendo a tupla jogadas
for y in jogadas:
    # Loop para capturar um palpite válido
    while True:  
        # Solicita ao usuário um palpite
        num = input("Descubra um número entre 0 a 50: ")  
        # Verifica se a entrada não é um número
        if not num.isdigit(): 
            # Mensagem de erro
            print('Valor INVÁLIDO! Deve ser um número.') 
            # Volta para o início do loop para solicitar um novo palpite
            continue 

        # Converte a entrada para um número inteiro
        n = int(num)  

        # Verifica se o número está fora do intervalo permitido
        if n < 0 or n > 50:  
            # Mensagem de erro
            print('Valor INVÁLIDO! O número deve estar entre 0 e 50.')  
            # Volta para o início do loop para solicitar um novo palpite
            continue  
        
        # Se o número for válido
        # Exibe o número válido digitado pelo usuário
        print(f'Você digitou um número válido: {n}')  
        # Sai do loop de captura de palpite
        break  

    
    # Verifica se o palpite é maior que o número secreto
    if int(num) > ns and c <= 10:
        # Dica para o jogador
        print(f"Perdeu a {y} chance, o número sorteado é menor que {num}")  
    # Verifica se o palpite é menor que o número secreto
    elif int(num) < ns and c <= 10:
        print(f"Perdeu a {y} chance, o número sorteado é maior que {num}") 
    # Verifica se o palpite é igual ao número secreto
    elif int(num) == ns:
        # Mensagem de sucesso
        print(f"Acertou na {y} chance! faltando {f} de 10")  
        # Sai do loop de jogadas se o jogador acertar
        break  

    # Verifica se ainda há chances restantes
    if f != 0:
        # Informa quantas chances ainda restam
        print(f"faltam {f} chances!")  
    else:
        # Mensagem de fim de jogo se não houver chances restantes
        print('Suas chances de 10 terminaram.')  

    f -= 1  # Decrementa o contador de chances restantes
    c += 1  # Incrementa o contador de tentativas