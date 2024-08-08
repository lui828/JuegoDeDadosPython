import random

def lanzar_dado():
    """Lanza el dado y devuelve un número entre 1 y 6."""
    return random.randint(1, 6)

def mostrar_instrucciones():
    """Muestra las instrucciones del juego."""
    print("¡Bienvenido al juego de los Dados Pig!")
    print("En cada turno, puedes lanzar los dados tantas veces como desees.")
    print("Si sacas un 1, pierdes todos los puntos de ese turno.")
    print("Si decides detenerte, acumulas los puntos de ese turno.")
    print("El primer jugador en alcanzar 70 puntos gana.")
    print()


def turno_jugador(nombre):
    print(nombre)
    """Maneja el turno de un jugador."""
    puntos_turno = 0
    while True:
        dado = lanzar_dado()
        print(f"{nombre} lanza el dado... salió un {dado}.")
        if dado == 1:
            print(f"¡{nombre} sacó un 1! Pierde todos los puntos de este turno.")
            return 0
        else:
            puntos_turno += dado
            print(f"Puntos de este turno: {puntos_turno}.")
            decision = input("¿Quieres lanzar de nuevo o detenerte? (lanza/detente): ").strip().lower()
            if decision == 'detente':
                return puntos_turno

def jugar_pig_dice():
    """Función principal para jugar a Pig Dice."""
    
    mostrar_instrucciones()
    puntos_jugador1= 0
    puntos_jugador2 = 0
    meta_puntos = 70
    
    while puntos_jugador1 < meta_puntos and puntos_jugador2 < meta_puntos:
        print("\nTurno del Jugador 1")
        puntos_turno1 = turno_jugador("Jugador 1")
        puntos_jugador1 += puntos_turno1
        print(f"Total de puntos de Jugador 1: {puntos_jugador1}")
        if puntos_jugador1 >= meta_puntos:
            break

        print("\nTurno del Jugador 2")
        puntos_turno2 = turno_jugador("Jugador 2")
        puntos_jugador2 += puntos_turno2
        print(f"Total de puntos de Jugador 2: {puntos_jugador2}")
    
    if puntos_jugador1 >= meta_puntos:
        print("Jugador 1 gana!")
    else:
        print("Jugador 2 gana!")
        

# Ejecuta el juego
if __name__ == "__main__":
    jugar_pig_dice()