# Borja Villena Pardo
# Fuentes consultadas: //docs.python.org ; //chat.openai.com ;
# //adictosaltrabajo.com ; //micro.recursospython.com ; //aula.uoc.edu ;
# //github.com ; //google.com
# Importamos librerías necesarias
import random as ra

# Creamos diccionario global
myDict = {}


# Desactivamos guía de estilo porque nos está reportando un fallo interno
%pycodestyle_off


# Creamos la función que nos piden
def diccionario():
    """
    Esta función recibe como entrada un string con la ruta a una carpeta
    y devuelve un diccionario con el siguiente formato:

    Las claves del diccionario serán enteros representando el orden en el que
    se ha encontrado cada una de las líneas de cada uno de los archivos.

    El valor asociado a cada clave será, en sí mismo, un diccionario con una
    clave para cada uno de los siguientes conceptos:
    summary, city, state, date_time, shape, duration, text,c ity_latitude,
    city_longitude y el valor asociado a cada clave según consta en el archivo
    que se está leyendo.

    """
    # Definimos la ruta base
    ruta_base = os.getcwd()
    # Solicitamos la ruta relativa
    ruta = input(f'Partiendo de la ruta base:\n\n {ruta_base}\n\n'
                 'escribe la ruta relativa del repositorio que quieres '
                 'analizar para construir el diccionario:'
                 '\n\n\t-Si quieres usar '
                 'el repositorio de carpetas surgido tras descomprimir'
                 ' el archivo original.zip, escribe: '
                 ' /content/size_decompressed/original \n\n')
    # ruta : /content/size_decompressed/original'

    # Utilizamos diccionario global creado previamente
    global myDict
    ord_linea = 0
    # Usamos loops for anidados con funciones lógicas para obtener la
    # información requerida del repositorio e ir formando el diccionario
    for state in os.listdir(ruta):
        ruta_state = os.path.join(ruta, state)

        if os.path.isdir(ruta_state):
            for city in os.listdir(ruta_state):
                ruta_city = os.path.join(ruta_state, city)

                if os.path.isdir(ruta_city):
                    for archivo in os.listdir(ruta_city):
                        ruta_archivo = os.path.join(ruta_city, archivo)

                        with open(ruta_archivo, 'r') as archivo_txt:
                            lineas = archivo_txt.readlines()

                            for i in lineas:
                                datos = i.strip().split(';')

                                # Construimos el diccionario "valor" de nuestro
                                # diccionario global myDict

                                myDict_valor = {}

                                # Agregamos toda la información y le
                                # damos orden
                                myDict_valor = {
                                    'summary': datos[0],
                                    'city' : city,
                                    'state' : state,
                                    'date_time': datos[1],
                                    'shape' : archivo.split('.')[0],
                                    'duration': datos[2],
                                    'text': datos[3],
                                    'city_latitude': datos[4],
                                    'city_longitude': datos[5]
                                }


                                # Agregamos llave myDict_Valor para completar
                                # myDict
                                myDict[ord_linea] = myDict_valor
                                ord_linea += 1

    return myDict


myDict = diccionario()


# Test Cell, Public
dict_size = len(myDict)

rand_val_s1 = ra.randint(0, dict_size-1)
rand_val_s2 = ra.randint(0, dict_size-1)

assert dict_size == 101207, " Incorrect number of entries."
assert len(myDict[0]) == len(myDict[dict_size-1]) == 9, \
  " Incorrect number of entries."