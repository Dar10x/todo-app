def obtener_tareas():
    with open('files/reporte.txt', 'r') as file:
        tareas = file.readlines()
    return tareas

def escribir_tareas(tareas):
    with open('files/reporte.txt', 'w') as file:
        file.writelines(tareas)