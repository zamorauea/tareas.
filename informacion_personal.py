# Crear el diccionario con información personal 
informacion_personal = {
    "nombre": "Viviana",
    "edad": 33,
    "ciudad": " Esmeraldas A",
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Esmeralda B"

# Agregar la clave "profesion" al diccionario
informacion_personal["profesion"] = "Ingeniera"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["celular"] = "0996173679"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad")

# Imprimir el diccionario resultante
print("Información personal actualizada:")
print(informacion_personal)
