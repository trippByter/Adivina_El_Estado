#==========Manejo de mapa con "Turtle"======#
import turtle
screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Prompt que solicita texto al usuario (nombre del estado)
answer_state = screen.textinput(
    title = "Guess the State",
    prompt = "What's another state's name?"
    )


#______Fin Manejo de mapa con "Turtle"________#

# R E G I S T R A N D O    C L I C K S
# ==========> get_mouse_click_coor <============
# muestra en consola coordenadas del click en el mapa
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
# ==========> Fin get_mouse_click_coor <==========