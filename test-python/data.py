
def get_companies():
    
    companies = [
        {
            'id': 1,
            'name': 'SOFTPYMES SAS',
            'nit': '123456789',
            'dv': '1',
            'branches': [1, 3, 5]
        },
        {
            'id': 2,
            'name': 'COMPANY SERVICES LTDA',
            'nit': '987654321',
            'dv': '2',
            'branches': [2]
        },
        {
            'id': 3,
            'name': 'LA INDUSTRIA INC',
            'nit': '987654333',
            'dv': '3',
            'branches': [4]
        },
        {
            'id': 4,
            'name': 'FEISBUT SA',
            'nit': '900500630',
            'dv': '4',
            'branches': [6]
        },
        {
            'id': 5,
            'name': 'DESARROLLADORES DEV',
            'nit': '900802602',
            'dv': '5',
            'branches': [7]
        }
    ] 
    return companies
    
    
def get_branches():
    
    branches = [
        {
            'id': 1,
            'name': 'PRINCIPAL',
            'address': 'Cll 123',
            'isMain': True,
            'cityName':'Pereira'
        },
        {
            'id': 2,
            'name': 'LA ISLA',
            'address': 'Cll 12 # 1-23',
            'isMain': True,
            'cityName':'Cali'
        },
        {
            'id': 3,
            'name': 'ZONA NORTE',
            'address': 'Cll 1 # 11-23',
            'isMain': False,
            'cityName':'Pereira'
        },
        {
            'id': 4,
            'name': 'CENTRO',
            'address': 'Cll 4 # 4-32',
            'isMain': True,
            'cityName':'Medellin'
        },
        {
            'id': 5,
            'name': 'ZONA PACIFICO',
            'address': 'Cll 5 # 5-43',
            'isMain': False,
            'cityName':'Bogota'
        },
        {
            'id': 6,
            'name': 'OESTE',
            'address': 'Cll 6 # 6-45',
            'isMain': False,
            'cityName':'Pereira'
        },
        {
            'id': 7,
            'name': 'CC SUR',
            'address': 'Cll 7 # 7-56',
            'isMain': True,
            'cityName':'Pasto'
        }
        
    ]     
    return branches
    
    
def get_thirds():
    thirds = [
        {
            "billAddress1": "CRA 8 69 76",
            "cellPhone": None,
            "cityName": "Ibague",
            "companyid": 1,
            "email": "prueba@test.com.co",
            "firstname": "GERMAN ALBERTO",
            "identificationDv": "8",
            "identificationNumber": "1111123",
            "lastname": "CHAVARRO",
            "maidenname": "RAMIREZ",
            "phone": "2136368",
            "state": "ACTIVO",
            "tradename": ""
        },
        {
            "billAddress1": "CARRERA 59 NO 26 21",
            "cellPhone": None,
            "cityName": "Pasto",
            "companyid": 3,
            "email": "siifn@otra.co",
            "firstname": "",
            "identificationDv": "5",
            "identificationNumber": "8046924",
            "lastname": "",
            "maidenname": "",
            "phone": "3158000",
            "state": "ACTIVO",
            "tradename": "POLICIA NACIONAL DE COLOMBIA"
        },
        {
            "billAddress1": "CRA 8 NO 6 C 38",
            "cellPhone": "321687526",
            "cityName": "Cucuta",
            "companyid": 2,
            "email": "",
            "firstname": "",
            "identificationDv": "4",
            "identificationNumber": "800168",
            "lastname": "",
            "maidenname": "",
            "phone": "542200",
            "state": "ACTIVO",
            "tradename": "DIAN"
        },
        {
            "billAddress1": "CRA 15 NO. 134 A 25 APTO 406 CONTADOR",
            "cellPhone": None,
            "cityName": "Sucre",
            "companyid": 1,
            "email": "",
            "firstname": "JORGE",
            "identificationDv": "6",
            "identificationNumber": "122693",
            "lastname": "RAMIREZ",
            "maidenname": "GASCA",
            "phone": "",
            "state": "ACTIVO",
            "tradename": ""
        },
        {
            "billAddress1": "CRA 8 N 69-76",
            "cellPhone": None,
            "cityName": "BOGOTA",
            "companyid": 1,
            "email": "asrfs@no.com",
            "firstname": "MARIA ELCY",
            "identificationDv": "2",
            "identificationNumber": "26520933",
            "lastname": "RAMIREZ",
            "maidenname": "GASCA",
            "phone": "",
            "state": "ACTIVO",
            "tradename": ""
        },
        {
            "billAddress1": "CRA 9 N 72-35",
            "cellPhone": "32164782",
            "cityName": "Suarez",
            "companyid": 1,
            "email": "contabilidad@test.com.co",
            "firstname": "",
            "identificationDv": "1",
            "identificationNumber": "86250302",
            "lastname": "",
            "maidenname": "",
            "phone": "",
            "state": "ACTIVO",
            "tradename": "BANCO BBVA"
        },
        {
            "billAddress1": "CR 66 A N 43 18",
            "cellPhone": None,
            "cityName": "Cali",
            "companyid": 1,
            "email": "forpo@test.co",
            "firstname": "",
            "identificationDv": "0",
            "identificationNumber": "860020227",
            "lastname": "",
            "maidenname": "",
            "phone": "2209960",
            "state": "ACTIVO",
            "tradename": "FONDO ROTATORIO DE CASA"
        },
        {
            "billAddress1": "AV CLL 26 N 51 50 PISO 5",
            "cellPhone": None,
            "cityName": "Manizales",
            "companyid": 1,
            "email": "",
            "firstname": "",
            "identificationDv": "4",
            "identificationNumber": "898969900",
            "lastname": "",
            "maidenname": "",
            "phone": "2236580",
            "state": "ACTIVO",
            "tradename": "MARISCOS DEL PACIFICO"
        },
        {
            "billAddress1": "CARRERA 8 NO. 8 - 55",
            "cellPhone": None,
            "cityName": "Tolima",
            "companyid": 1,
            "email": "",
            "firstname": "",
            "identificationDv": "5",
            "identificationNumber": "83085348",
            "lastname": "",
            "maidenname": "",
            "phone": "343100",
            "state": "INACTIVO",
            "tradename": "MINISTERIO DE CULTURA"
        },
        {
            "billAddress1": "CRA 8 NO 69 76",
            "cellPhone": "32565851",
            "cityName": "Jamundí",
            "companyid": 1,
            "email": "",
            "firstname": "",
            "identificationDv": "3",
            "identificationNumber": "80365816",
            "lastname": "",
            "maidenname": "",
            "phone": "566980",
            "state": "ACTIVO",
            "tradename": "CONSEJO ESPACIAL"
        },
        {
            "billAddress1": "CARRERA 50 # 18-06",
            "cellPhone": None,
            "cityName": "Calarca",
            "companyid": 1,
            "email": "",
            "firstname": "",
            "identificationDv": "4",
            "identificationNumber": "809888632",
            "lastname": "",
            "maidenname": "",
            "phone": "3325611",
            "state": "INACTIVO",
            "tradename": "LA CASA DEL PAN DE YUCA"
        },
        {
            "billAddress1": "CRA 8 NO 69 76",
            "cellPhone": "32105648521",
            "cityName": "Armenia",
            "companyid": 5,
            "email": "",
            "firstname": "",
            "identificationDv": "2",
            "identificationNumber": "86965100",
            "lastname": "",
            "maidenname": "",
            "phone": "34332560",
            "state": "ACTIVO",
            "tradename": "LA CASERONA"
        }
    ]
    return thirds
    
    
def get_colors():
    colors = [
        {
            "colorCode": "AMA",
            "colorName": "AMARILLO"
        },
        {
            "colorCode": "AZU",
            "colorName": "AZUL"
        },
        {
            "colorCode": "BLA",
            "colorName": "BLANCO"
        },
        {
            "colorCode": "CAR",
            "colorName": "CARMELITA"
        },
        {
            "colorCode": "FUS",
            "colorName": "FUSCIA"
        },
        {
            "colorCode": "NAR",
            "colorName": "NARANJA"
        },
        {
            "colorCode": "NEG",
            "colorName": "NEGRO"
        },
        {
            "colorCode": "PR",
            "colorName": "PUPURAL"
        },
        {
            "colorCode": "ROJ",
            "colorName": "ROJO"
        },
        {
            "colorCode": "ROS",
            "colorName": "ROSADO"
        },
        {
            "colorCode": "VER",
            "colorName": "VERDE"
        },
        {
            "colorCode": "VIO",
            "colorName": "VIOLETA"
        }
    ]
    return colors
    
    
def get_items():
    items = [
        {
            'code': '001',
            'name': 'Celular',
            'color': 'BLA',
            'price': 1150000
        },
        {
            'code': '002',
            'name': 'Camiseta',
            'color': 'NEG',
            'price': 50000
        },
        {
            'code': '003',
            'name': 'Lapíz',
            'color': 'NAR',
            'price': 1000
        },
        {
            'code': '004',
            'name': 'Lentes',
            'color': None,
            'price': 500000
        },
        {
            'code': '005',
            'name': 'Zapatos',
            'color': 'ROS',
            'price': 170000
        },
        {
            'code': '006',
            'name': 'Vaso de cristal',
            'color': None,
            'price': 5500
        },
        {
            'code': '007',
            'name': 'Portail HP',
            'color': 'ROJ',
            'price': 2500000
        },
        {
            'code': '008',
            'name': 'Cuaderno',
            'color': None,
            'price': 5000
        },
        {
            'code': '009',
            'name': 'Gorra',
            'color': 'VER',
            'price': 50000
        },
        {
            'code': '010',
            'name': 'Balón',
            'color': None,
            'price': 0
        }
    ]
    return items
    
    
