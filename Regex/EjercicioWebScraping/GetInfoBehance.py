# requests for fetching html of website
import requests
# re biblioteca de regular expressions
import re

# OPCIÓN 1: OBTENINENDO EL HTML CON UNA PETICIÓN

# Obtener HTML (web no dinámica)
# https://www.behance.net/okhergo
r = requests.get('https://www.behance.net/okhergo')

# Extraer el cotenido como texto
data = r.text

# Descomentar esta linea para ver el contenido obtenido y llevarlo a https://regex101.com/
# O utilizar el inspector de elementos de Google Chrome para obtener el código fuente de la página web
#print(data)

# TIP: En regex101 tenéis una opción para generar el código para lenguaje de programación que necesitéis


# OPCIÓN 2: Obtener el codigo HTML del inspector de elementos de Google Chrome para obtener el código fuente de la página web
#data = """  CODIGO HTML COPIADO   """


# COMPLETA ESTO
# Las expresiones regulares en Python tienen una r detras que significa raw string, 
# lo que significa que cualquier carácter especial dentro de la cadena de texto se
# interpreta literalmente en lugar de como un carácter de escape.
regex = r"/<td class="UserInfo-statColumn-NsR UserInfo-statValue-d3q"><a href="\/okhergo\/insights" class="UserInfo-statValue-d3q UserInfo-disabledLink-gtI">([0-9]*)"/gm

# Cuidado con los flags
# Prueba a utilizar caputuring groups
# Comprueba que ocurre con findall, match, search etc.

"""

findall documentación
https://docs.python.org/3/library/re.html#re.findall
The result depends on the number of capturing groups in the pattern. 
If there are no groups, return a list of strings matching the whole pattern. 
If there is exactly one group, return a list of strings matching that group. 
If multiple groups are present, return a list of tuples of strings matching the groups. 
Non-capturing groups do not affect the form of the result.

"""
vistas_proyecto = re.findall(regex, data, re.MULTILINE)
print(vistas_proyecto)


if len(vistas_proyecto) > 0:
	print(f"El numero de vistas de proyecto es: {vistas_proyecto[0]}")

