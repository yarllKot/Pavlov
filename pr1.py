#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #импортируем библиотечку
import numpy #Еще одну
import matplotlib.pyplot as mpp #Последнюю

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': #условие ифа
    arguments = numpy.arange(-20, 20, 0.1) #Выбираем область определения кортежем
    mpp.plot( #Начало функции
        arguments, #аргументы и строчкой ниже тоже аргументы
        [math.sin(a)*math.pow(math.e,a) for a in arguments]
    )
    mpp.show()#выводим график