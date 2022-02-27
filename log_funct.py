"""Выяснить, какие функция тормозят - запрещено устанавливать непроверенные модули и пакеты"""

"""Вариант №1: засечь время выполнения каждой функции с помощью встроенной библиотеки
datetime"""
import time
from datetime import datetime
def calc_1():

    start_time=datetime.now()
    time.sleep(2)
    print(datetime.now()-start_time)

"""Вариант №2: посчитать среднее значение выполнения каждой функции, за количество раз N"""
import timeit
N=4
def calc_2():

    time.sleep(2)

"""Вариант №3: прологировать каждую функцию - тогда мы сможем отслеживать не только 
производительность, но и отлавливать ошибки"""
import logging
logging.basicConfig(filename="logs/logs.log", level=logging.INFO)
wait_time=2
def calc_3(wait_time):
    logging.info(f'Function started on {datetime.now()}')
    time.sleep(wait_time)
    logging.info(f'Function ended on {datetime.now()}')

if __name__ == '__main__':
    calc_1() #Вариант №1
    print(timeit.timeit(calc_2,number=N)) #Вариант №2
    calc_3(wait_time) #Вариант №2 - создастся текстовый файл logs в папке logs со временем