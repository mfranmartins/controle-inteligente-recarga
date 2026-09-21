from machine import Pin, ADC
import time

# CONFIGURACAO DOS COMPONENTES
pot_geracao = ADC(26)
pot_consumo = ADC(27)
led_verde = Pin(16, Pin.OUT)
led_amarelo = Pin(17, Pin.OUT)
led_vermelho = Pin(18, Pin.OUT)
# FUNCAO PARA CONVERTER ADC EM WATTS
def converter_para_watts(valor_adc):
    return int((valor_adc / 65535) * 5000)

# FUNCAO PARA CONVERTER DECIMAL EM HEX
def decimal_para_hexadecimal(numero):
    caracteres = "0123456789ABCDEF"

    if numero == 0:
        return "0000"

    resultado = ""

    while numero > 0:
        resto = numero % 16
        resultado = caracteres[resto] + resultado
        numero = numero // 16

    while len(resultado) < 4:
        resultado = "0" + resultado

    return resultado

# FUNCAO PARA CONTROLAR OS LEDS
def desligar_leds():
    led_verde.value(0)
    led_amarelo.value(0)
    led_vermelho.value(0)

# VARIAVEIS DE CONTROLE
ultima_geracao = -1
ultimo_consumo = -1

# LOOP PRINCIPAL
while True:
    # LEITURA DOS POTENCIOMETROS
    leitura_geracao = pot_geracao.read_u16()
    leitura_consumo = pot_consumo.read_u16()

    # CONVERSAO PARA WATTS
    geracao = converter_para_watts(leitura_geracao)
    consumo = converter_para_watts(leitura_consumo)

    # VERIFICA SE OS VALORES MUDARAM
    if geracao != ultima_geracao or consumo != ultimo_consumo:

        # Guarda os novos valores
        ultima_geracao = geracao
        ultimo_consumo = consumo

        # CALCULO DA ENERGIA DISPONIVEL
        energia_disponivel = geracao - consumo

        # DESLIGA TODOS OS LEDS
        desligar_leds()

        # DEFINICAO DO STATUS
        if energia_disponivel >= 1000:
            status = "RECARGA AUTORIZADA"
            led_verde.value(1)
        elif energia_disponivel > 0:
            status = "RECARGA REDUZIDA"
            led_amarelo.value(1)
        else:
            status = "RECARGA BLOQUEADA"
            led_vermelho.value(1)

        # REPRESENTACAO DOS DADOS
        geracao_binario = bin(geracao)[2:]
        geracao_hexadecimal = decimal_para_hexadecimal(geracao)
        consumo_binario = bin(consumo)[2:]
        consumo_hexadecimal = decimal_para_hexadecimal(consumo)

        # TERMINAL
        print("\033[2J\033[H")
        print("     CONTROLE INTELIGENTE DE RECARGA")
        print("Geracao em decimal:          ", geracao,"W")
        print("Geracao em binario:          ", geracao_binario)
        print("Geracao em hexadecimal:      ", geracao_hexadecimal)
        print("Consumo em decimal:          ", consumo,"W")
        print("Consumo em binario:          ", consumo_binario)
        print("Consumo em hexadecimal:      ", consumo_hexadecimal)
        print()
        print("Energia disponivel:          ", energia_disponivel,"W")
        print("Status:",status)

    time.sleep(0.1)
