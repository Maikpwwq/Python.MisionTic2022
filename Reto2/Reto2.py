def prestamo (informacion:dict)-> dict:

    # Uso Variables
    p_id = informacion['id_prestamo'] #id_prestamo
    p_c= informacion['casado'] == 'Si' #Si/No
    p_d= informacion['dependientes'] #manejar 4 casos 0,1,2,3+    
    p_e= informacion['educacion'] == 'Graduado' # Graduado/No Graduado
    p_i= informacion['independiente'] == 'Si' # Si/No
    i_d= informacion['ingreso_deudor'] # numero
    i_c= informacion['ingreso_codeudor'] # numero
    c_p= informacion['cantidad_prestamo'] # numero
    # p_p= informacion['plazo_credito']
    h_c= informacion['historia_credito'] == 1 # 1-0
    t_p= informacion['tipo_propiedad'] # Rural Urbana Semiurbano

    def caso_personas (dependientes):
        if (dependientes == 0 or dependientes == 1):                    
            return False
        elif (dependientes == 2 or dependientes == '3+'):
            return True

    # Uso condicionales
    p= i_c > 0
    q= (i_d / 9) > c_p
    r= caso_personas(p_d)
    s= p_i
    t= (i_c / 12) > c_p
    u= c_p < 200
    v= not (p_c and r)
    w= (i_d / 10) > c_p 
    x= (i_c / 10) > c_p 
    y= c_p < 180
    z= not (t_p == 'Semiurbano')
    pp= p_e
    pq= (i_d / 11) > c_p 
    pr= (i_c / 11) > c_p     

    # Arbol de decisiones
    if h_c :
        if p and q:
            aprobar= True            
        else:
            if r and s :
                if t:
                    aprobar= True
                else:
                    aprobar= False
            else:
                if u:
                    aprobar= True
                else:
                    aprobar= False            
    else:
        if s:
            if v:
                if w or x:
                    if y:
                        aprobar= True
                    else:
                        aprobar= False
                else:
                    aprobar= False
            else:
                aprobar= False             
        else:
            if not(r) and z:
                if pp :
                    if pq and pr:
                        aprobar= True
                    else:
                        aprobar= False
                else:
                    aprobar= False
            else:
                aprobar= False                        
    
    diccionario_respuesta = {
        'id_prestamo': p_id,
        'aprobado': aprobar
    }

    return diccionario_respuesta

informacion = {
    'id_prestamo': 'RETOS2_001',
    'casado': 'No',
    'dependientes': 1,
    'educacion': 'Graduado',
    'independiente': 'Si',
    'ingreso_deudor': 4692,
    'ingreso_codeudor': 0,
    'cantidad_prestamo': 106,
    'plazo_prestamo': 360,
    'historia_credito': 1,
    'tipo_propiedad': 'Rural'
}

print(prestamo(informacion))

informacion = {
    'id_prestamo': 'RETOS2_002',
    'casado': 'No',
    'dependientes': '3+',
    'educacion': 'No Graduado',
    'independiente': 'No',
    'ingreso_deudor': 1830,
    'ingreso_codeudor': 0,
    'cantidad_prestamo': 100,
    'plazo_prestamo': 360,
    'historia_credito': 0,
    'tipo_propiedad': 'Urbano'
}

print(prestamo(informacion))

informacion = {
    'id_prestamo': 'RETOS2_003',
    'casado': 'No',
    'dependientes': 0,
    'educacion': 'No Graduado',
    'independiente': 'No',
    'ingreso_deudor': 3748,
    'ingreso_codeudor': 1668,
    'cantidad_prestamo': 110,
    'plazo_prestamo': 360,
    'historia_credito': 1,
    'tipo_propiedad': 'Semiurbano'
}

print(prestamo(informacion))

informacion = {
    'id_prestamo': 'RETOS2_011',
    'casado': 'No',
    'dependientes': '3+',
    'educacion': 'Graduado',
    'independiente': 'No',
    'ingreso_deudor': 3080,
    'ingreso_codeudor': 0,
    'cantidad_prestamo': 255,
    'plazo_prestamo': 360,
    'historia_credito': 1,
    'tipo_propiedad': 'Rural'
}

print(prestamo(informacion))

informacion = {
    'id_prestamo': 'RETOS2_012',
    'casado': 'Si',
    'dependientes': 1,
    'educacion': 'Graduado',
    'independiente': 'Si',
    'ingreso_deudor': 11500,
    'ingreso_codeudor': 0,
    'cantidad_prestamo': 286,
    'plazo_prestamo': 360,
    'historia_credito': 0,
    'tipo_propiedad': 'Urbano'
}

print(prestamo(informacion))