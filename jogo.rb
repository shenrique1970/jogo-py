require 'securerandom'

# O jogador deverá escolher um número inteiro qualquer entre 0 e 50.
np = rand(0..50)

r = {1 => 'Primeira', 2 => 'Segunda', 3 => 'Terceira', 4 => 'Quarta', 5 => 'Quinta', 6 => 'Sexta', 7 => 'Sétima', 8 => 'Oitava', 9 => 'Nona', 10 => 'Décima'}

# Você terá 10 tentativas para acertar qual foi o número oculto gerado
# pelo computador no intervalo (0 a 50).
c = 1
f = 9
r.each_value do |y|
  while true
    print "Descubra numero entre 0 a 50: "
    num = gets.chomp
    break if num.match?(/^\d+$/) && (n = num.to_i) >= 0 && n <= 50

    puts 'Valor INVÁLIDO!'
  end

  if num.to_i > np && c <= 10
    puts "Perdeu a #{y} chance, o numero sorteado é menor que #{num}"
  elsif num.to_i < np && c <= 10
    puts "Perdeu a #{y} chance, o numero sorteado é maior que #{num}"
  elsif f != 0 && num.to_i != np
    puts "faltam #{f} chances!"
  elsif c == 10
    puts 'Suas chances de 10, acabaram'
  elsif num.to_i == np
    puts "Acertou na #{y} chance! faltando #{f} de 10"
    break
  end

  f -= 1
  c += 1
end

