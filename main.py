import schedule
import xlrd
import time
import speedtest
from datetime import datetime

from threading import Timer
def internet():
    s = speedtest.Speedtest()
    data_atual = str(datetime.now().strftime('%d/%m/%Y'))
    hora_atual = str(datetime.now().strftime('%H:%M'))
    velocidade = str(s.download(threads=None)*(10**-6))
    arquivo = open("dados.txt", "a")
    linhas = list()
    linhas.append(data_atual + " - " + hora_atual + " -- " + velocidade + "\n")
    arquivo.writelines(linhas)
    print(data_atual, " - ", hora_atual, " -- ", velocidade)
    Timer(1, internet).start()


internet()