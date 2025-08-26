# Sua solução aqui

# Enunciado do Exercicio:
# Um determinado material radioativo perde metade 
# de sua massa a cada 50 segundos. Dada a massa inicial, 
# em gramas, fazer um algoritmo que determine o tempo 
# necessário para que essa massa se torne menor do 
# que 0,5 grama. Escreva a massa inicial a massa 
# final e o tempo calculado em horas, minutos e segundos.


# Valor de entrada:
massa = float(input())

# Inicialmente o tempo vale 0
tempo_passado_segundos = 0
tempo_passado_minutos = 0
tempo_passado_horas = 0


# Enquanto a massa for maior que 0.5g,
# o programa ira continuar fazendo a 
# contagem do tempo(em segundos) 
# e dividindo a massa pela metade.
while massa >= 0.5:
    tempo_passado_segundos += 50
    massa /= 2


# Transformacao do tempo em segundos para
# minutos dividindo por 60
if tempo_passado_segundos >= 60:
    tempo_passado_minutos = tempo_passado_segundos // 60
    tempo_passado_segundos %= 60

# Transformacao para horas
if tempo_passado_minutos >= 60:
    tempo_passado_horas = tempo_passado_minutos // 60
    tempo_passado_minutos %= 60

# Saida dos dados
print(f"{tempo_passado_horas}h "
      f"{tempo_passado_minutos}m "
      f"{tempo_passado_segundos}s"
    )