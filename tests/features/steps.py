# -*- coding: utf-8 -*-
from lettuce import step, world


@step(u'Dado el número (\d+)')
def dado_el_numero(step, numero):
    world.numero = int(numero)


@step(u'Cuando computamos el factorial')
def computamos_el_factorial(step):
    world.numero = factorial(world.numero)


@step(u'Debo ver el número (\d+)')
def debo_ver_numero(step, esperado):
    esperado = int(esperado)
    assert world.numero == esperado, \
        "Obtuve %d" % world.numero


def factorial(n):
    return 1
