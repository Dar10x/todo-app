import funciones
import FreeSimpleGUI as sg

label = sg.Text("Ingresa una tarea")
input_box = sg.InputText(tooltip="Ingresa la tarea",key="tarea")
add_button = sg.Button('Agregar')
edit_button = sg.Button('Editar')
list_box = sg.Listbox(values=funciones.obtener_tareas(),key="tareas",
                      enable_events=True,size=[43,10])

window = sg.Window('Mi aplicacion de tareas pendientes',
                   layout=[[label],[input_box,add_button],[list_box,edit_button]],
                   font=('Helvetica',20))

while True:
    evento,valores = window.read()
    print(evento)
    print(valores)
    match evento:
        case 'Agregar':
            tareas = funciones.obtener_tareas()
            nueva_tarea = valores['tarea'] + '\n'
            tareas.append(nueva_tarea)
            funciones.escribir_tareas(tareas)
            window['tareas'].update(values=tareas)
        case 'Editar':
            tarea_editar = valores['tareas'][0]
            nueva_tarea = valores['tarea'] + '\n'
            tareas = funciones.obtener_tareas()
            index = tareas.index(tarea_editar)
            tareas[index] = nueva_tarea
            funciones.escribir_tareas(tareas)
            window['tareas'].update(values = tareas)
        case 'tareas':
            window['tarea'].update(value = valores['tareas'][0])
        case sg.WIN_CLOSED:
            break

window.close()
