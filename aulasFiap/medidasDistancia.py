#Usain Bolt é o recordista mundial dos 100 metros rasos com o tempo de 9,58 segundos.
#Escreva um algoritmo que calcula a velocidade média em m/s e em km/h de um corredor,
#seu algoritmo recebe como dados de entrada a distância em metros e o tempo em segundos.
distancia = float(input("Distância em metros: "))
tempo = float(input("Rempo em segundos: "))

velocidadeMetrosSegundo = distancia / tempo

print("Velocidade m/s: ", velocidadeMetrosSegundo)

distancia_km = distancia / 1000
tempo_hs = tempo / 3600

velocidade_kmhora = distancia_km / tempo_hs
print("Velocidade Km/h: ", velocidade_kmhora)