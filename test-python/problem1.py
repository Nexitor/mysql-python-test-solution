from data import *

""" 
  1) 
  cree un objeto que contenga las empresas y dentro 
  las sucursales que corresponden para cada empresa
"""

class empresas:

    companies = get_companies()
    branches = get_branches()

    for i in range(len(companies)):
        for j in range(0,len(companies[i]['branches'])):
            for k in range(0,len(branches)):
                if companies[i]['branches'][j] == branches[k]['id']:
                    companies[i]['branches'][j] = branches[k]['name']


empresa = empresas()
for i in range(0,len(empresa.companies)):
    print(empresa.companies[i])


