def promedio_facultades(dict:info, contando_externos:bool = True) -> tuple:

    set_correos = set() # Conjunto para no repetir correos
    facultades = set() # Conjunto para no repetir facultades

    # Accedemos a cada estudiante e identificamos a que facultades pertenecen
    for codigo_estudiante in info.values():
        for materia in codigo_estudiante['materias']:
            facultades.add(materia['facultad'])
    
    suma_facultades = {} # Almacena la suma de la nota * creditos por facultad
    creditos_facultades = {} # Almacena los creditos de la facultad

    # Inicializamos los valores en 0
    for facultad in facultades:
        suma_facultades[facultad] = 0
        creditos_facultades[facultad] = 0

    for codigo_estudiante, info_estudiante in info.items():
        utilizado = False
        for materia in info_estudiante['materias']:
            if materia['retirada'] == 'No' and materia['creditos'] != 0:
                if contando_externos == True or ( materia['codigo'][:4] == info_estudiante['programa'] and str (codigo_estudiante)[4:6] != '05' ) :
                    utilizado == True
                    try: 
                        suma_facultades[materia['facultad']] += materia['nota'] * materia['creditos']
                        creditos_facultades[materia['facultad']] += materia['creditos']
                    except:
                        return 'Error numérico'
        if utilizado == True:
            nombres = info_estudiante['nombres'].split(' ') 
            apellidos = info_estudiante['apellidos'].split(',') 

            if len(nombres) == 1:
                set_correos.add(nombres[0][0] + apellidos[1][0] + '.' + apellidos[0] + str(info_estudiante['documento'])[])
            else:
                set_correos.add(nombres[0][0] + nombres[1][0] + '.' + apellidos[1] + str(info_estudiante['documento'])[])

    # El metodo .maketrans retorna una tabla de mapeo (diccionario) para el reemplazo a travez del metodo translate
    a,b = 'áéíóúñÁÉÍÓÚÑ', 'aeiounaeioun'
    trans = str.maketrans(a,b) 

    lista_correos = list(sorted(set_correos))
    # Adicionar un indice con la funcion enumerate y reemplazar caracteres no permitidos
    for indice, correo in enumerate(lista_correos):
        lista_correos[indice] = correo.translate(trans).lower()
        # lista_correos[indice] = (unicodedata.normalize('NFKD', correo.lower()).encode('ASIIC', 'ignore').decode(''UTF)

    diccionario_respuesta = {}
    for fac in sorted(creditos_facultades.keys()):
        diccionario_respuesta[fac] = round( suma_facultades[fac] / creditos_facultades[fac] , 2)
    
    return (diccionario_respuesta , lista_correos)

# Prueba 1:
print(promedio_facultades({					
					20110274333:{
								"nombres" : "Carolina Paula",
								"apellidos" : "Ochoa, López",
								"documento" : 82364435,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7972",
												"nota" : 3.15,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
                    20190264705:{
								"nombres" : "Julio Nicolas",
								"apellidos" : "Fernández, Ramírez",
								"documento" : 42697671,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-7888",
												"nota" : 4.68,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
                    20170136837:{
								"nombres" : "Jorge Juan",
								"apellidos" : "Moreno, López",
								"documento" : 88481595,
								"programa" : "ARQU",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-8218",
												"nota" : 4.49,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-2113",
												"nota" : 2.97,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-5048",
												"nota" : 4.26,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20130225137:{
								"nombres" : "Sara Carolina",
								"apellidos" : "Gómez, Fernández",
								"documento" : 58770043,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-7738",
												"nota" : 3.36,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-9115",
												"nota" : 2.62,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-7698",
												"nota" : 1.59,
												"creditos" : 4,
												"retirada" : "Si",
												},
											]
								},
					20200116062:{
								"nombres" : "Sara Camila",
								"apellidos" : "Martínez, Gómez",
								"documento" : 40079000,
								"programa" : "DIGR",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-9331",
												"nota" : 4.0,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-3530",
												"nota" : 3.4,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-8548",
												"nota" : 3.1,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-9771",
												"nota" : 3.91,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20100379147:{
								"nombres" : "Jorge Juan",
								"apellidos" : "Romero, López",
								"documento" : 39344921,
								"programa" : "DIGR",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-9511",
												"nota" : 2.38,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-6043",
												"nota" : 3.71,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1720",
												"nota" : 2.5,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20200126220:{
								"nombres" : "Sofia",
								"apellidos" : "Cordoba, Romero",
								"documento" : 90333325,
								"programa" : "IQUI",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-4982",
												"nota" : 4.57,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-4982",
												"nota" : 2.8,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-6947",
												"nota" : 2.47,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-2248",
												"nota" : 3.43,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20130271126:{
								"nombres" : "Gabriela",
								"apellidos" : "Alvarez, García",
								"documento" : 72857337,
								"programa" : "ARQU",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-4963",
												"nota" : 3.15,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-2113",
												"nota" : 3.9,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-1221",
												"nota" : 4.37,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20160219974:{
								"nombres" : "Daniela Sara",
								"apellidos" : "Cuellar, Guitiérrez",
								"documento" : 80398132,
								"programa" : "IIND",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-3557",
												"nota" : 3.91,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-5158",
												"nota" : 3.83,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-7543",
												"nota" : 3.41,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},					
					20150222512:{
								"nombres" : "Mateo Gabriel",
								"apellidos" : "Niño, Romero",
								"documento" : 12964051,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-3683",
												"nota" : 3.6,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-4014",
												"nota" : 3.15,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-1670",
												"nota" : 4.75,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					}))
# Expected return:
# ({'Arquitectura': 3.81, 'Diseño': 3.58, 'Ingenieria': 3.63, 'Medicina': 3.08}, ['cp.lopez35', 'ds.guitierrez32', 'gg.alvarez37', 'jj.lopez21', 'jj.lopez95', 'jn.ramirez71', 'mg.romero51', 'sc.fernandez43', 'sc.gomez00', 'sr.cordoba25'])

# Prueba 2:
print(promedio_facultades({
					20170116008:{
								"nombres" : "Sofia Natalia",
								"apellidos" : "Martinez, Alvarez",
								"documento" : 86056697,
								"programa" : "HAMO",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-3145",
												"nota" : 3.79,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-1882",
												"nota" : 3.02,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-4916",
												"nota" : 3.99,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-9576",
												"nota" : 3.2,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-7401",
												"nota" : 4.08,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20180181912:{
								"nombres" : "Julian Andres",
								"apellidos" : "Fernández, Gómez",
								"documento" : 38203099,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-4822",
												"nota" : 3.99,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-6559",
												"nota" : 3.09,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20170131506:{
								"nombres" : "Laura Camila",
								"apellidos" : "Cuellar, Pérez",
								"documento" : 15755411,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-7857",
												"nota" : 3.19,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1857",
												"nota" : 2.62,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1415",
												"nota" : 2.83,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1720",
												"nota" : 2.58,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20100240601:{
								"nombres" : "Andres Julian",
								"apellidos" : "Ochoa, Romero",
								"documento" : 81959788,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-7472",
												"nota" : 3.6,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-5465",
												"nota" : 2.58,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-8357",
												"nota" : 4.69,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-9511",
												"nota" : 2.51,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-3379",
												"nota" : 4.31,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20160386484:{
								"nombres" : "Julio",
								"apellidos" : "Sánchez, Fernández",
								"documento" : 95423746,
								"programa" : "HART",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-3008",
												"nota" : 2.83,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-3008",
												"nota" : 2.53,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-2620",
												"nota" : 4.06,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20190365550:{
								"nombres" : "Catalina Valentina",
								"apellidos" : "García, López",
								"documento" : 88933669,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-5278",
												"nota" : 3.45,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1857",
												"nota" : 4.56,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9835",
												"nota" : 3.93,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9442",
												"nota" : 4.46,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20150173830:{
								"nombres" : "Catalina Valentina",
								"apellidos" : "Fernández, Guitiérrez",
								"documento" : 36216549,
								"programa" : "DISE",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-3520",
												"nota" : 2.71,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-5596",
												"nota" : 4.7,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-6981",
												"nota" : 2.79,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-5596",
												"nota" : 2.51,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-5161",
												"nota" : 2.36,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20100383099:{
								"nombres" : "Juan Pablo",
								"apellidos" : "Moreno, Cordoba",
								"documento" : 17911136,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-9115",
												"nota" : 4.18,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-6074",
												"nota" : 3.73,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20090198116:{
								"nombres" : "Sofia Gabriela",
								"apellidos" : "Diaz, Moreno",
								"documento" : 62587112,
								"programa" : "ICIV",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-1157",
												"nota" : 2.45,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-7915",
												"nota" : 4.17,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-5962",
												"nota" : 4.49,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20190262931:{
								"nombres" : "Paula Natalia",
								"apellidos" : "Torres, Jiménez",
								"documento" : 18534577,
								"programa" : "HART",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-2081",
												"nota" : 4.43,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-8458",
												"nota" : 4.77,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-1258",
												"nota" : 3.15,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20190299456:{
								"nombres" : "Natalia Paula",
								"apellidos" : "Moreno, Alvarez",
								"documento" : 89771722,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7322",
												"nota" : 4.27,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-5808",
												"nota" : 3.19,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-4470",
												"nota" : 2.26,
												"creditos" : 4,
												"retirada" : "Si",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7972",
												"nota" : 3.66,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20150172603:{
								"nombres" : "Catalina Paula",
								"apellidos" : "Pérez, Diaz",
								"documento" : 59641117,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-8636",
												"nota" : 4.65,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-1999",
												"nota" : 2.52,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-3063",
												"nota" : 2.95,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20160197253:{
								"nombres" : "Julian Mateo",
								"apellidos" : "Jiménez, Fernández",
								"documento" : 41016120,
								"programa" : "MEDI",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-9348",
												"nota" : 4.55,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9306",
												"nota" : 2.77,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-1836",
												"nota" : 3.66,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20160174103:{
								"nombres" : "Mateo Julio",
								"apellidos" : "Diaz, López",
								"documento" : 88132707,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-2104",
												"nota" : 4.55,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-3425",
												"nota" : 3.98,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-4686",
												"nota" : 4.97,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-9455",
												"nota" : 2.43,
												"creditos" : 0,
												"retirada" : "Si",
												},
											]
								},
					20150384070:{
								"nombres" : "Carolina Natalia",
								"apellidos" : "López, Gómez",
								"documento" : 33424549,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7322",
												"nota" : 2.49,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-4101",
												"nota" : 3.14,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-8021",
												"nota" : 2.97,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7470",
												"nota" : 4.77,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					}, False ))
# Expected return: No 88
# ({'Arquitectura': 3.84, 'Diseño': 3.37, 'Historia del Arte': 3.66, 'Ingenieria': 3.88, 'Medicina': 3.45}, ['aj.romero88', 'cn.gomez49', 'cp.diaz17', 'cv.guitierrez49', 'cv.lopez69', 'jf.sanchez46', 'jm.fernandez20', 'jp.cordoba36', 'lc.perez11', 'mj.lopez07', 'np.alvarez22', 'pn.jimenez77', 'sg.moreno12', 'sn.alvarez97'])

# Prueba 3 
print(promedio_facultades({
     20200389418:{
        "nombres" : "Carolina Camila",
        "apellidos" : "Martínez, Jiménez",
        "documento" : 28762912,
        "programa" : "ARQU",
        "materias" : [
            
           ]
        },
     20180218013:{
        "nombres" : "Julio Nicolas",
        "apellidos" : "Pardo, Ramírez",
        "documento" : 28762921,
        "programa" : "ISIS",
        "materias" : [
            {
            "facultad" : "Ingenieria",
            "codigo" : "ISIS-2485",
            "nota" : 4.49,
            "creditos" : 2,
            "retirada" : "No",
            },
            {
            "facultad" : "Ingenieria",
            "codigo" : "ISIS-6565",
            "nota" : 2.44,
            "creditos" : 3,
            "retirada" : "No",
            },
            {
            "facultad" : "Ingenieria",
            "codigo" : "ISIS-2485",
            "nota" : 4.17,
            "creditos" : 2,
            "retirada" : "No",
            },
            {
            "facultad" : "Ingenieria",
            "codigo" : "ISIS-6565",
            "nota" : 1.93,
            "creditos" : 3,
            "retirada" : "Si",
            },
            {
            "facultad" : "Ingenieria",
            "codigo" : "ISIS-6565",
            "nota" : 3.29,
            "creditos" : 3,
            "retirada" : "No",
            },
           ]
        },
     20120153166:{
        "nombres" : "Maria Camila",
        "apellidos" : "Gómez, Suárez",
        "documento" : 13060098,
        "programa" : "MEDI",
        "materias" : [
            {
            "facultad" : "Medicina",
            "codigo" : "MEDI-6474",
            "nota" : 4,
            "creditos" : 3,
            "retirada" : "No",
            },
            {
            "facultad" : "Medicina",
            "codigo" : "MEDI-1652",
            "nota" : 3.63,
            "creditos" : 2,
            "retirada" : "No",
            },
            {
            "facultad" : "Medicina",
            "codigo" : "MEDI-9490",
            "nota" : 3.61,
            "creditos" : 3,
            "retirada" : "No",
            },
            {
            "facultad" : "Historia del Arte",
            "codigo" : "HART-8458",
            "nota" : 3.0,
            "creditos" : 3,
            "retirada" : "No",
            },
           ]
        },
     20180294370:{
        "nombres" : "Andres Oscar",
        "apellidos" : "Martínez, Guitiérrez",
        "documento" : 38221530,
        "programa" : "DISE",
        "materias" : [
            {
            "facultad" : "Diseño",
            "codigo" : "DISE-5161",
            "nota" : 3.18,
            "creditos" : 3,
            "retirada" : "No",
            },
            {
            "facultad" : "Diseño",
            "codigo" : "DISE-4199", 
            "nota" : 3.31,
            "creditos ...snip... t     nota" : 3.93,
            "creditos" : 2,
            "retirada" : "No",
            },
           ]
        },
     20140227848:{
        "nombres" : "Jose Nicolas",
        "apellidos" : "Díaz, Romero",
        "documento" : 21403906,
        "programa" : "IQUI",
        "materias" : [
            {
            "facultad" : "Ingenieria",
            "codigo" : "IQUI-3859",
            "nota" : 3.94,
            "creditos" : 3,
            "retirada" : "No",
            },
            {
            "facultad" : "Ingenieria",
            "codigo" : "IQUI-9815",
            "nota" : 3.68,
            "creditos" : 1,
            "retirada" : "No",
            },
            {
            "facultad" : "Ingenieria",
            "codigo" : "IQUI-9702",
            "nota" : 2.7,
            "creditos" : 4,
            "retirada" : "No",
            },
            {
            "facultad" : "Ingenieria",
            "codigo" : "IQUI-2859",
            "nota" : 4.05,
            "creditos" : 2,
            "retirada" : "No",
            },
           ]
        },
     20170115295:{
        "nombres" : "Maria Paula",
        "apellidos" : "Córdoba, Ramírez",
        "documento" : 43182695,
        "programa" : "ICIV",
        "materias" : [
            {
            "facultad" : "Ingenieria",
            "codigo" : "ICIV-8615",
            "nota" : 4.43,
            "creditos" : 3,
            "retirada" : "No",
            },
            {
            "facultad" : "Ingenieria",
            "codigo" : "ICIV-1020",
            "nota" : 3.12,
            "creditos" : 4,
            "retirada" : "No",
            },
            {
            "facultad" : "Ingenieria",
            "codigo" : "ICIV-1020",
            "nota" : 3.18,
            "creditos" : 4,
            "retirada" : "No",
            },
           ]
        },
     20140186272:{
        "nombres" : "Gabriel Nicolas",
        "apellidos" : "Cuellar, López",
        "documento" : 55100972,
        "programa" : "DIMD",
        "materias" : [
            {
            "facultad" : "Diseño",
            "codigo" : "DIIN-5413",
            "nota" : 3.69,
            "creditos" : 0,
            "retirada" : "Si",
            },
            {
            "facultad" : "Diseño",
            "codigo" : "DIMD-8304",
            "nota" : 4.98,
            "creditos" : 4,
            "retirada" : "No",
            },
            {
            "facultad" : "Diseño",
            "codigo" : "DIMD-7666",
            "nota" : 3.23,
            "creditos" : 2,
            "retirada" : "No",
            },
            {
            "facultad" : "Diseño",
            "codigo" : "DIMD-3018",
            "nota" : 3.67,
            "creditos" : 3,
            "retirada" : "No",
            },
           ]
        },
     } ))
# Expected return: evitar 'cc.jimenez12' 'dl.ramirez99' 'nm.cordoba54' 'pn.alvarez60' 'po.cuellar46' 'vn.hernandez50'
# ({'Arquitectura': 3.77, 'Diseño': 3.81, 'Historia del Arte': 3.54, 'Ingenieria': 3.58, 'Medicina': 3.71}, ['ao.guitierrez30', 'ap.pardo45', 'cd.alvarez54', 'cg.ochoa82', 'cg.torres35', 'co.ochoa69', 'cs.suarez51', 'dc.ochoa90', 'dg.perez52', 'dl.alvarez18', 'ds.sanchez79', 'gn.lopez72', 'ja.cuellar06', 'jg.lopez00', 'jn.garcia75', 'jn.ramirez07', 'jn.romero06', 'jp.martinez62', 'ld.cordoba15', 'lg.martinez88', 'mc.suarez98', 'mp.ramirez95', 'na.alvarez52', 'nc.sanchez05', 'no.sanchez57', 'oj.garcia59', 'oj.gomez77', 'on.perez17', 'pm.suarez99', 'sc.guitierrez83', 'sc.torres93', 'sd.hernandez00', 'sn.nino29', 'sp.nino74'])

# Prueba 4
print(promedio_facultades({
     20180234491:{
        "nombres" : "Julio Juan",
        "apellidos" : "López, Cuellar",
        "documento" : 89783030,
        "programa" : "ICIV",
        "materias" : [
            {
            "facultad" : "Ingenieria",
            "codigo" : "ICIV-2983",
            "nota" : 3.65,
            "creditos" : 0,
            "retirada" : "No",
            },
            {
            "facultad" : "Ingenieria",
            "codigo" : "ICIV-4627",
            "nota" : 3.34,
            "creditos" : 3,
            "retirada" : "No",
            },
            {
            "facultad" : "Ingenieria",
            "codigo" : "ICIV-6267",
            "nota" : 3.29,
            "creditos" : 4,
            "retirada" : "No",
            },
            {
            "facultad" : "Ingenieria",
            "codigo" : "ICIV-7182",
            "nota" : 2.83,
            "creditos" : 2,
            "retirada" : "Si",
            },
           ]
        },
     20180111599:{
        "nombres" : "Camilo Julián",
        "apellidos" : "Cuellar, Sánchez",
        "documento" : 25501871,
        "programa" : "HART",
        "materias" : [
            {
            "facultad" : "Historia del Arte",
            "codigo" : "HART-1258",
            "nota" : 3.77,
            "creditos" : 3,
            "retirada" : "Si",
            },
            {
            "facultad" : "Historia del Arte",
            "codigo" : "HART-4066",
            "nota" : 2.76,
            "creditos" : 0,
            "retirada" : "No",
            },
            {
            "facultad" : "Historia del Arte",
            "codigo" : "HART-5285",
            "nota" : 3.74,
            "creditos" : 0,
            "retirada" : "Si",
            },
           ]
        },
     20130111233:{
        "nombres" : "Camilo Jorge",
        "apellidos" : "Pérez, Díaz",
        "documento" : 68407479,
        "programa" : "MEDI",
        "materias" : [
            {
            "facultad" : "Medicina",
            "codigo" : "MEDI-7278",
            "nota" : 2.48,
            "creditos" : 1,
            "retirada" : "Si",
            },
            {
            "facultad" : "Medicina",
            "codigo" : "MEDI-2625",
            "nota" : 3.52,
            "creditos" : 4,
            "retirada" : "Si",
            },
            {
            "facultad" : "Medicina",
            "codigo" : "MENF-2553",
            "nota" : 2.24,
            "creditos" : 3,
            "retirada" : "Si",
            },
            {
            "facultad" : "Medicina",
            "codigo" : "MEDI-9490",
            "nota" : 4.64,
            "creditos" : 3,
            "retirada" : "No",
            },
           ]
        },
     20180270894:{
        "nombres" : "Camila",
        "apellidos" : "Guitiérrez, Pardo",
        "documento": "...snip... omero, Ramírez",
        "documento" : 61689275,
        "programa" : "MENF",
        "materias" : [
            {
            "facultad" : "Medicina",
            "codigo" : "MENF-2072",
            "nota" : 2.43,
            "creditos" : 2,
            "retirada" : "No",
            },
            {
            "facultad" : "Medicina",
            "codigo" : "MENF-2593",
            "nota" : 3.22,
            "creditos" : 4,
            "retirada" : "No",
            },
            {
            "facultad" : "Medicina",
            "codigo" : "MENF-6067",
            "nota" : 4.58,
            "creditos" : 1,
            "retirada" : "No",
            },
            {
            "facultad" : "Medicina",
            "codigo" : "MENF-5889",
            "nota" : 2.59,
            "creditos" : 0,
            "retirada" : "No",
            },
           ]
        },
     20190287188:{
        "nombres" : "Daniela Sofia",
        "apellidos" : "García, Córdoba",
        "documento" : 75179813,
        "programa" : "ARQD",
        "materias" : [
            {
            "facultad" : "Arquitectura",
            "codigo" : "ARQD-1564",
            "nota" : 2.72,
            "creditos" : 3,
            "retirada" : "No",
            },
            {
            "facultad" : "Arquitectura",
            "codigo" : "ARQD-3420",
            "nota" : 2.46,
            "creditos" : 4,
            "retirada" : "No",
            },
            {
            "facultad" : "Arquitectura",
            "codigo" : "ARQD-1864",
            "nota" : 3.94,
            "creditos" : 4,
            "retirada" : "No",
            },
            {
            "facultad" : "Arquitectura",
            "codigo" : "ARQD-1564",
            "nota" : 3.14,
            "creditos" : 3,
            "retirada" : "Si",
            },
           ]
        },
     20170294793:{
        "nombres" : "Jorge Nicolas",
        "apellidos" : "Cuellar, Jiménez",
        "documento" : 49162279,
        "programa" : "DIIN",
        "materias" : [
            {
            "facultad" : "Diseño",
            "codigo" : "DIIN-2355",
            "nota" : 3.31,
            "creditos" : 3,
            "retirada" : "No",
            },
            {
            "facultad" : "Diseño",
            "codigo" : "DIMD-4014",
            "nota" : 3.88,
            "creditos" : 3,
            "retirada" : "No",
            },
            {
            "facultad" : "Diseño",
            "codigo" : "DIIN-3467",
            "nota" : 2.69,
            "creditos" : 4,
            "retirada" : "No",
            },
            {
            "facultad" : "Diseño",
            "codigo" : "DIIN-3467",
            "nota" : 2.54,
            "creditos" : 4,
            "retirada" : "No",
            },
           ]
        },
     } ))
# Expected return: evitar 'cj.sanchez71'  'cs.garcia72' 'jc.gomez64'
# ({'Arquitectura': 3.5, 'Diseño': 3.51, 'Historia del Arte': 3.32, 'Ingenieria': 3.57, 'Medicina': 3.84}, ['ao.moreno72', 'as.moreno65', 'cc.moreno79', 'cd.diaz95', 'cd.ramirez17', 'cj.diaz79', 'cj.nino13', 'cl.sanchez46', 'cp.guitierrez74', 'dn.alvarez66', 'dp.moreno22', 'ds.cordoba13', 'ga.jimenez70', 'gc.pardo14', 'gc.sanchez97', 'gj.alvarez97', 'gj.ochoa71', 'gm.garcia13', 'gn.martinez48', 'go.fernandez88', 'gs.torres68', 'ja.lopez56', 'jc.guitierrez73', 'jc.hernandez92', 'jc.sanchez60', 'jc.sanchez71', 'jd.ramirez75', 'jg.cuellar03', 'jj.cuellar30', 'jj.ochoa30', 'jn.jimenez79', 'jp.hernandez60', 'ld.hernandez98', 'md.diaz36', 'mg.jimenez54', 'mn.diaz52', 'mn.martinez68', 'mo.gomez89', 'ng.martinez32', 'no.ramirez99', 'oj.cordoba71', 'pg.gomez25', 'pj.diaz67', 'sc.martinez33', 'sc.suarez26', 'sn.alvarez95', 'ss.ochoa48'])    