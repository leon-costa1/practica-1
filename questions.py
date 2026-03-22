import random

words = {
    "General": ["python", "programa"],
    "Tipos de datos": ["cadena", "entero", "lista"],
    "Varios": ["variable", "funcion", "bucle"]
}

play = True
score = 0

print("¡Bienvenido al Ahorcado!")
print()

while play:
    # Mostrar categorias de palabras
    print("Categorias:")
    number = 1
    for clave in words:
        print(f"{number}) {clave}")
        number += 1
    print()

    # Elegir categoria
    category = int(input("Elija el numero de categoria que desea: "))
    while (category > (number-1)) or (category < 1):
        print("Numero no valido")
        print()
        category = int(input("Elija el numero de categoria que desea: "))

    # Armado random de la categoria
    match category:
        case 1:
            category_list = random.sample(words["General"], len(words["General"]))
        case 2:
            category_list = random.sample(words["Tipos de datos"], len(words["Tipos de datos"]))
        case 3:
            category_list = random.sample(words["Varios"], len(words["Varios"]))

    index = 0

    while (index+1) <= len(category_list) and play:
        guessed = []
        attempts = 6
        
        word = category_list[index]
        index += 1
        
        while attempts > 0:
            # Mostrar progreso: letras adivinadas y guiones para las que faltan
            progress = ""
            for letter in word:
                if letter in guessed:
                    progress += letter + " "
                else:
                    progress += "_ "
            print(progress)

            # Verificar si el jugador ya adivinó la palabra completa
            if "_" not in progress:
                print("¡Ganaste!")
                score += 6
                break
            
            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")

            letter = input("Ingresá una letra: ")

            if len(letter) == 1 and letter.isalpha():
                if letter in guessed:
                    print("Ya usaste esa letra.")
                elif letter in word:
                    guessed.append(letter)
                    print("¡Bien! Esa letra está en la palabra.")
                else:
                    guessed.append(letter)
                    attempts -= 1
                    score -= 1
                    print("Esa letra no está en la palabra.")
            else:
                print("Entrada no valida")

            print()

        else:
            print(f"¡Perdiste! La palabra era: {word}")
            score = 0
        
        print()
        print("1) Terminar juego.")
        print("2) Seguir jugando (en la misma categoria hasta el final de la misma).")
        
        after_round = int(input("Que quieres hacer? (si elije cualquier otro numero se le asignara la opcion 2): "))
        if after_round == 1:
            play = False
    
    print()
    
    if play:
        print("Termino con las palabras de la categoria elegida, vuelva a elegir.")
        print()

print(f"Puntaje final: {score}")