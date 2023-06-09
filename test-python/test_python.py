# Para tener en cuenta: la información necesaría para la solución de esta 
# prueba, la encuentran en el archivo data.py, 
# 
# Para el tema de terceros (thirds)
#
# !importante: para la identificación a mostrar, se debe tener en cuenta lo siguiente:
#
#  third: {
#    "identificationDv": "5",
#    "identificationNumber": "8046924",
#  }
#
# la identificación a mostrar es: 8.046.924-5 o 8,046,924-5
# 
# Se debe tener en cuenta que la identificación se muestra con separador de miles
# 
# NOTA: Solo para la identificación que se muestra, para las validaciones y demás debe 
# ser sin ajuste de miles ==> 8046924

""" 
  1) 
  cree un objeto que contenga las empresas y dentro 
  las sucursales que corresponden para cada empresa
"""

"""
  2) 
  teniendo en cuenta el punto 1, cree una función que permita
  consultar las sucursales, debe hacerse el mismo procedimiento
  que se realizó en el punto 1, pero, utilizando la función creada
"""

"""
  3) 
  ordenar los terceros por nombre, para obtener el nombre correcto se debe tener en 
  cuenta la siguiente validación:
  
  si el tercero tiene un (tradename != '') entonces se muestra el tradename, 
  en caso contrario se debe obtener el nombre concatenando los siguientes 
  campos: (firstname, lastname, maidenname) en el orden dado
"""

"""
  4) 
  Mostrar de los terceros los cuales no poseen ni email o no tengan cellPhone.
"""

"""
  5) 
  ordenar los terceros por nombre y agregar dentro de cada tercero una 
  propiedad que muestre la compañia a la que pertenece
"""

"""
  6) 
  ordernar las compañias por nombre y dentro de cada compañia, crear un objecto 
  llamado thirds el cual va a tener todos los terceros que pertenezcan a esa compañia,
  se debe tener en cuenta que tengan un estado ACTIVO
"""

"""
  7) 
  muestre los items que tienen colores y ordenelos por precio de manera ascendente
"""

"""
  8) 
  muestre los items donde su codigo sea un número PAR,
  ordenelos por el precio de manera descendente y dentro de cada item 
  agregue el color correspondiente, si lo tiene.
"""

"""
  9) 
  muestre todos los items, ordenelos por nombre y dentro de cada item agregue 
  el color correspondiente, en caso de que esté lo tenga. 
  
  El resultado del ordenando debe ser así, en la parte inicial los items que no tienen 
  color y en la parte final los que si tienen color, todo dentro de un mismo objeto
"""

"""
  10) 
  muestre todos los terceros, reduzca la información y solo muestre el nombre, la ciudad, 
  la identificacion y el estado, ordenelos por su identificación.

"""