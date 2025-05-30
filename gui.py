import funciones
import FreeSimpleGUI as sg

label = sg.Text("Ingresa una tarea")
input_box = sg.InputText(tooltip="Ingresa la tarea")
add_button = sg.Button('Agregar')

window = sg.Window('Mi aplicacion de tareas pendientes',layout=[[label],[input_box,add_button]])
window.read()
window.close()
