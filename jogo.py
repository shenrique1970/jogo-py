import random
import numpy as np

# O jogador deverá escolher um número inteiro qualquer entre 0 e 50.
np = random.randint(0,50)


r = {1:'Primeira', 2:'Segunda', 3:'Terceira', 4:'Quarta', 5:'Quinta', 6:'Sexta', 7:'Satima', 8:'Oitava', 9:'Nona', 10:'Decima'}


#### Voce terá 10 tentativas para acertar qual foi o número oculto gerado
#### pelo computador no intervalo (0 a 50).
c = 1
f = 9
for y in r.values():
    while not (num := input("Descubra numero entre 0 a 50: ")).isdigit() or (n := int(num)) < 0 or int(num) > 50:
        print('Valor INVÁLIDO!')
        

    if int(num) > np and c <= 10:
        print(f"Perdeu a {y} chance, o numero sorteado é menor que {num}")
    elif int(num) < np and c <= 10:
        print(f"Perdeu a {y} chance, o numero sorteado é maior que {num}")
    elif f != 0 and int(num) != np:
        print(f"faltam {f} chances!")
    elif c == 10:
        print('Suas chances de 10, acabaram')
    elif int(num) == np:
        print(f"Acertou na {y} chance! faltando {f} de 10")
        break

    f -= 1
    c += 1  