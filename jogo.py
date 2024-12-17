import random as np
#import numpy as np

# O jogador deverá escolher um número inteiro qualquer entre 0 e 50.
ns = np.randint(0,50)

# nomeando as jogadas
jogadas = ("Primeira","Segunda","Terceira","Quarta","Quinta","Sexta",
    "Setima","Oitava","Nona","Decima")

#### Voce terá 10 tentativas para acertar qual foi o número oculto gerado
#### pelo computador no intervalo (0 a 50).
c = 1
f = 9
print(ns)
for y in jogadas:
    while True:
        num = input("Descubra um número entre 0 a 50: ")
        
        if not num.isdigit():
            print('Valor INVÁLIDO! Deve ser um número.')
            continue
        
        n = int(num)
        
        if n < 0 or n > 50:
            print('Valor INVÁLIDO! O número deve estar entre 0 e 50.')
            continue
        
        # Se o número for válido, saia do loop
        break

    print(f'Você digitou um número válido: {n}')
       

    if int(num) > ns and c <= 10:
        print(f"Perdeu a {y} chance, o numero sorteado é menor que {num}")
    elif int(num) < ns and c <= 10:
        print(f"Perdeu a {y} chance, o numero sorteado é maior que {num}")
    elif int(num) == ns:
        print(f"Acertou na {y} chance! faltando {f} de 10")
        break
    if f != 0:
        print(f"faltam {f} chances!")
    else:
        print('Suas chances de 10 terminaram.') 
        
    
    f -= 1
    c += 1  
