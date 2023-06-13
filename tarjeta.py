import pygame
from constantes import *


def crear_tarjeta(nombre_imagen: str, identificador: int, nombre_imagen_escondida: str, x: int, y: int) -> dict:
    '''
    Crea una nueva tarjeta
    Recibe como parametro el path donde estan los recursos, el nombre de la imagen y el tamaño que esta debera tener
    Retorna la tarjeta creada
    '''
    superficie = pygame.image.load(CARPETA_RECURSOS + nombre_imagen)
    superficie_escalar = pygame.transform.scale(superficie,(ANCHO_TARJETA,ALTO_TARJETA))
    superficie_escondida = pygame.image.load(CARPETA_RECURSOS + nombre_imagen_escondida)
    superficie_escondida_escalar = pygame.transform.scale(superficie_escondida,(ANCHO_TARJETA,ALTO_TARJETA))
    superficie_rect = superficie_escalar.get_rect()
    superficie_rect.x = x
    superficie_rect.y = y
    tarjeta = {
        "superficie": superficie_escalar,
        "superficie_escondida": superficie_escondida_escalar,
        "identificador": identificador,
        "visible": False,
        "descubierto": False,
        "rectangulo": superficie_rect
    }
    return tarjeta


def obtener_cantidad_tarjetas_por_estado(lista_tarjetas: list[dict], estado: bool) -> int:
    '''
        Obtiene la cantidad de tarjetas que esten visibles y que esten o no cubiertas
        Recibe la lista de tarjetas y un estado (True o False) si es True me devuelve las cartas descubieras sino me devuelve las cubiertas.
        Retorna dicha cantidad
    '''
    cantidad = 0
    for tarjeta in lista_tarjetas:
        if (tarjeta["descubierto"] == estado and tarjeta["visible"]):
            cantidad += 1
    return cantidad


def descubrir_tarjetas(lista_tarjetas, identificador):
    '''
        Función que se encarga de cambiarme la bandera a las tarjetas a las que el usuario haya acertado en el memotest
        recibe la lista de tarjetas y el identificador a la que le va a reemplazar la bandera descubierto
        Uso una variable contador para evitar que el bucle se ejecute completo y ahorrar recursos si ya reemplazo a dos tarjetas no tiene sentido seguir iterando
    '''
    contador = 0
    for tarjeta in lista_tarjetas:
        if tarjeta["identificador"] == identificador and tarjeta["descubierto"] == False:
            tarjeta["descubierto"] = True
            contador += 1
        elif contador == 2:
            break
            