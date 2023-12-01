import re

# Leemos todas las palabras del español
filename = '0_palabras_todas.txt'

with open(filename, encoding="utf8") as file:
    # lines = file.readlines()
    print("Leidas todas la palabras del español correctamente")
    data = file.read()
    # close file
    file.close()

# Nos quedaremos solo con las que cumplen el regex que indique 5 caracteres

# COMPLETA ESTO
regex_cinco_caracteres = ""

# Cuidado con los flags
palabras_cinco_letras = re.findall(regex_cinco_caracteres, data, re.MULTILINE)

# Suponiendo la siguiente situación en Wordle

# https://wordle.danielfrg.com/

# PROBANDO PRIMERA PALABRA DE 5 LETRAS

# COMPLETA ESTO
regex_intento = ""

palabras_restantes = re.findall(regex_intento, data, re.MULTILINE)

print(f"Posibles palabras:{len(palabras_restantes)}")
print(palabras_restantes)

# INTRODUCIMOS REGEX DE ACUERDO A LOS RESULTADOS
regex_intento = ""
palabras_restantes = re.findall(regex_intento, data, re.MULTILINE)

print(f"Posibles palabras:{len(palabras_restantes)}")
print(palabras_restantes)

# INTRODUCIMOS REGEX DE ACUERDO A LOS RESULTADOS

regex_intento = ""
palabras_restantes = re.findall(regex_intento, data, re.MULTILINE)

print(f"Posibles palabras:{len(palabras_restantes)}")
print(palabras_restantes)

# INTRODUCIMOS REGEX DE ACUERDO A LOS RESULTADOS

regex_intento = ""
palabras_restantes = re.findall(regex_intento, data, re.MULTILINE)

print(f"Posibles palabras:{len(palabras_restantes)}")
print(palabras_restantes)