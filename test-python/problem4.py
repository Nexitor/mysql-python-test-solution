from data import *
"""
  4) 
  Mostrar de los terceros los cuales no poseen ni email o no tengan cellPhone.
"""

terceros = get_thirds()

for i in range(0,len(terceros)):
    if terceros[i]["email"] == "" or terceros[i]["email"] == "":
        print(terceros[i])
