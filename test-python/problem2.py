from data import *
"""
  2) 
  teniendo en cuenta el punto 1, cree una función que permita
  consultar las sucursales, debe hacerse el mismo procedimiento
  que se realizó en el punto 1, pero, utilizando la función creada
"""

class empresas:

    def sucursales(self):
        companies = get_companies()
        branches = get_branches()

        for i in range(len(companies)):
            for j in range(0,len(companies[i]['branches'])):
                for k in range(0,len(branches)):
                    if companies[i]['branches'][j] == branches[k]['id']:
                        companies[i]['branches'][j] = branches[k]['name']
        for i in range(0,len(companies)):
            print(companies[i])

empresa = empresas()
empresa.sucursales()