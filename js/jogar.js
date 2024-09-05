let chances = 10;

function myFunction() {
    const numero = document.getElementById('numero').value;
    const resultado = document.getElementById('resultado');
    const jogadas = document.getElementById('jogadas');

    if (chances > 0) {
        if (numero == randomNumber) {
            resultado.textContent = 'Parabéns! Você acertou!';
            jogadas.textContent = '';
        } else if (numero > randomNumber) {
            resultado.textContent = 'Tente um número menor.';
        } else {
            resultado.textContent = 'Tente um número maior.';
        }
        chances--;
        jogadas.textContent = 'Tentativas restantes: ' + chances;
    } else {
        resultado.textContent = 'Você não tem mais tentativas. O número era ' + randomNumber;
        jogadas.textContent = '';
    }
}