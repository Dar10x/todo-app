from funciones import obtener_tareas,escribir_tareas

while True:
    accion = input('Escriba agregar,editar,mostrar,completado o salir:')
    accion = accion.strip()

    if 'agregar' in accion:
        tarea = accion[8:] + "\n"
        tareas = obtener_tareas()
        tareas.append(tarea)
        escribir_tareas(tareas)

    elif 'mostrar' in accion:
        tareas = obtener_tareas()
        for index, item in enumerate(tareas):
            item = item.strip('\n')
            row = f"{index +1}-{item}"
            print(row)
    elif 'editar' in accion:
        numero = accion[7:]
        numero = int(numero) -1
        tareas = obtener_tareas()
        nueva_tarea = input('Ingrese la nueva tarea:')
        tareas[numero] = nueva_tarea + '\n'
        escribir_tareas(tareas)
    elif 'completado' in accion:
        numero = accion[11:]
        numero = int(numero)
        tareas = obtener_tareas()
        tarea_eliminada = tareas[numero-1]
        tareas.pop(numero-1)
        escribir_tareas(tareas)
        print(f"La tarea {tarea_eliminada.strip('\n')} fue completada y borrada exitosamente")
    elif 'salir' in accion:
        break
    else:
        print('Valor ingresado no valido')
print("Chau uu")