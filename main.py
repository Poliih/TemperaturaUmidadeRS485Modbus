import minimalmodbus
import time

# Configuração do dispositivo MODBUS
DEVICE_ADDRESS = 1
DEVICE_DEBUG = True
PORT_NAME = 'COM3'

# Inicialização do instrumento MODBUS
instrument = minimalmodbus.Instrument(PORT_NAME, DEVICE_ADDRESS, debug=DEVICE_DEBUG)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.mode = minimalmodbus.MODE_RTU
instrument.serial.timeout = 0.2

# Endereços de registradores para temperatura e umidade
REGISTER_ADDRESS_TEMP = 1  # Endereço do registrador para temperatura
REGISTER_NUMBER_DECIMALS_TEMP = 1  # Número de decimais para a temperatura

# Substitua esses valores pelos endereços corretos de leitura da umidade
REGISTER_ADDRESS_HUMIDITY = 2  # Endereço do registrador para umidade
REGISTER_NUMBER_DECIMALS_HUMIDITY = 1  # Número de decimais para a umidade

while True:
    try:
        # Ler temperatura
        temperature = instrument.read_register(REGISTER_ADDRESS_TEMP, REGISTER_NUMBER_DECIMALS_TEMP, 4)
        temp_celsius = temperature  # Não realizando divisão para manter o valor original

        # Ler umidade (substitua esses valores se tiver os endereços corretos)
        humidity = instrument.read_register(REGISTER_ADDRESS_HUMIDITY, REGISTER_NUMBER_DECIMALS_HUMIDITY, 4)
        print("Temperatura:", temp_celsius, "°C")
        print("Umidade:", humidity, "% ")

    except IOError:
        print("Falha ao ler do instrumento")

    time.sleep(1)  # Aguarda 1 segundo antes da próxima leitura
