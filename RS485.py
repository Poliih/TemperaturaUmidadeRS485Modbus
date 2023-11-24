import minimalmodbus
import time
import serial

# Configuração da porta serial para o dispositivo
instrument = minimalmodbus.Instrument('COM3', 1)  # Substitua '/dev/ttyUSB0' e 1 pelos valores corretos
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.mode = minimalmodbus.MODE_RTU
instrument.serial.timeout = 0.2


if instrument.serial.isOpen():  # Não há mais verificação da porta do sensor
    print("Conexão serial do dispositivo mestre aberta.")

    try:
        while True:
            # Ler temperatura e umidade do sensor via dispositivo Modbus
            temperature = instrument.read_register(1, 1, 4)
            humidity = instrument.read_register(2, 1, 4)
            print("Temperatura:", temperature, "°C")
            print("Umidade:", humidity, "%")

            # Dados do sensor não são lidos diretamente via porta serial aqui

            time.sleep(1)

    except KeyboardInterrupt:  # Interrompe o loop com Ctrl+C
        pass

    instrument.serial.close()  # Apenas fecha a conexão do dispositivo mestre
else:
    print("Erro ao abrir a conexão serial do dispositivo mestre.")
