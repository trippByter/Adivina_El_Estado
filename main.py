#==========Manejo de mapa con "Turtle"======#
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Leemos archivo csv
data = pandas.read_csv("50_states.csv")
# Obtenemos lista con todos los "states" - estados
all_states = data.state.to_list()

# Para evitar salir del programa cada vez que se
# adivine o no, creamos un bucle while
# La condición es que el usuario adivine los 
# 50 estados. Para eso, nos ayudamos de una lista
guessed_states = []
while len(guessed_states) < 50:
    # Prompt que solicita texto al usuario (nombre del estado)
    answer_state = screen.textinput(
        title = f"{len(guessed_states)}/50 States Correct",
        prompt = "What's another state's name?"
        ).title() # Primera en mayúscula

    print(answer_state)

    # Creamos la salida del juego.
    # Creamos una lista con los "states"
    # que ni fueron adivinados
    if answer_state == "Exit":
        unguessed = []
        for ung in all_states:
            if ung not in guessed_states:
                unguessed.append(ung)
        
        # Pasar lista a CSV: 
        # 1.- Pasar lista ("unguessed"), a DataFrame 
        # 2.- Pasar DataFrame a CSV ".to_csv"
        # 3.- Nombre del CSV entre paréntesis
        unguessed_data = pandas.DataFrame(unguessed)
        unguessed_data.to_csv("Faltantes.csv")
        break

    if answer_state in all_states:
        # Agregamos a guessed_states
        guessed_states.append(answer_state)
        # Instanciamos "Turtle"
        t = turtle.Turtle()
        # Ocultamos la forma real de la tortuga
        t.hideturtle()
        # Hacemos que se encierre para evitar dibujos
        t.penup()
        # Guardamos la fila completa correspondiente
        # al state si este es igual al answer_state
        state_data = data[data.state == answer_state]
        # Obtenemos coordenadas de ubicación X & Y
        # para ubicar la tortuga
        t.goto(int(state_data.x), int(state_data.y))
        # Hacemos que la tortuga imprima el nombre adivinado
        t.write(answer_state)

# Se quita esta línea para funcionalidad de "Exit"
# screen.exitonclick()
#______Fin Manejo de mapa con "Turtle"________#

# R E G I S T R A N D O    C L I C K S
# ==========> get_mouse_click_coor <============
# muestra en consola coordenadas del click en el mapa
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
# ==========> Fin get_mouse_click_coor <==========