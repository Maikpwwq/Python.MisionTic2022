# La funcion calcula sobre un promedio de notas ingresadas de 0 a 100
def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int)-> str:
    notasEstudiate=(nota1, nota2, nota3, nota4, nota5)
    notaMin= min(notasEstudiate) # Elegir la menor nota para descartar
    promedioAcordado= (nota1+ nota2+ nota3+ nota4+ nota5 - notaMin)/4 # Calculo Promedio
    promedioAjustado= promedioAcordado*5/100 # Transformar Nota a escala 0 a 5
    promedioRedondeado= round(promedioAjustado,2) # Promedio redondeado a 2 decimales
    promedio= str(promedioRedondeado) # Salida convertida a cadena 
    return "El promedio ajustado del estudiante {} es: {}".format(codigo, promedio)

print(nota_quices("AA0010276", 19,90,38,55,68))
print(nota_quices("IS00201620", 37,10,50,19,79))
print(nota_quices("BIO2201810", 45,46,33,74,22))
print(nota_quices("IQ102201810", 57,100,87,93,21))
print(nota_quices("MA00201520", 5,14,76,91,5))