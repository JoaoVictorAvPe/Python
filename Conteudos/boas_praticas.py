velocidade =  34
local_carro = 100

RADAR_1 = 60 #Variáveis constantes se escreve com letra maiúscula 
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_do_carro_acima_do_radar = velocidade > RADAR_1 
carro_esta_no_radar = (LOCAL_1 - RADAR_RANGE) <= local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = velocidade_do_carro_acima_do_radar and carro_esta_no_radar

if carro_multado:
   print('Acima da velocidade permitida no range do radar')
   print(f'Limite do radar: {RADAR_1}\nVelocidade do carro: {velocidade}')
