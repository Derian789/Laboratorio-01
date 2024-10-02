from random import choice

# Función para pedir y guardar el nombre
def inicio(): 
    nombre = input("Ingresa tu nombre: ")
    print(f"Hola, {nombre}. ¡Bienvenido a nuestro servidor!")
    print("___________________________________________________")     
    return nombre

# Función para mostrar opciones
def mostrar_opciones(pregunta):
    for texto in pregunta["opciones"]:
        print(texto)

# Función para obtener una pregunta aleatoria de una categoría
def obtener_pregunta(categoria, preguntas):
    if preguntas[categoria]:
        return choice(preguntas[categoria])
    return None

# Función para verificar la respuesta del usuario
def verificar_respuesta(respuesta_usuario, respuesta_correcta):
    return respuesta_usuario == respuesta_correcta

# Función principal del juego
def jugar(preguntas, nombre_usuario):
    puntuacion = 0
    while preguntas["programacion"] or preguntas["musica"]: 
        categoria = choice(["programacion", "musica"])     # Elegimos una categoría aleatoria
        pregunta = obtener_pregunta(categoria, preguntas)

        if pregunta:
            print(f"{nombre_usuario}, aquí tienes tu pregunta:")
            print(pregunta["pregunta"])  # Mostramos la pregunta
            mostrar_opciones(pregunta)

            respuesta = input("Selecciona una opción (A, B, C, D) o escribir 'salir' para salir del juego: ").upper() 

            if respuesta == 'SALIR':  # Verifica si el usuario quiere salir
                print(f"Gracias {nombre_usuario}, por jugar nuestro servidor")
                break  
            elif verificar_respuesta(respuesta, pregunta["respuesta"]):  # Comprueba la respuesta correcta
                print(f"¡Es correcto {nombre_usuario}!")
                puntuacion += 1      
            else:
                print(f"La respuesta es incorrecta {nombre_usuario}. ")
                puntuacion -= 1 

            print(f"Puntuación actual: {puntuacion}")
            print("_____________________________________________")     
            
            # Elimina la pregunta de la categoría
            preguntas[categoria].remove(pregunta)
        else:
            continue
    
    return puntuacion

# Función para mostrar el resultado final
def mostrar_resultado(puntuacion, nombre_usuario):
    print("__________________________________________")
    print("_______________RESULTADOS_________________")
    print("__________________________________________")
    print(f"\nFelicidades {nombre_usuario}, Tu puntuación final es: {puntuacion}")

# Ejecución del programa


 # Almacena el nombre del usuario

# Creación de diccionarios con dos categorías de preguntas, opciones y respuestas
preguntas = {
    "programacion": [
        {
            "pregunta": "¿Qué función de Python se usa para obtener la longitud de una lista?",
            "opciones": ["A. count()", "B. length()", "C. len()", "D. size()"],
            "respuesta": "C",
        },
        {
            "pregunta": "¿Qué palabra clave se utiliza para manejar excepciones en Python?",
            "opciones": ["A. throw", "B. except", "C. try", "D. catch"],
            "respuesta": "B",
        },
        {
            "pregunta": "¿Cómo se define una función en Python?",
            "opciones": ["A. def mi_funcion[]:", "B. function mi_funcion():", "C. def mi_funcion():", "D. mi_funcion[]:"],
            "respuesta": "C",
        },
        {
            "pregunta": "¿Qué función se utiliza para obtener datos del usuario en Python?",
            "opciones": ["A. get()", "B. input()", "C. read()", "D. ask()"],
            "respuesta": "B",
        },
        {
            "pregunta": "¿Qué método se utiliza para agregar un elemento al final de una lista?",
            "opciones": ["A. add()", "B. insert()", "C. append()", "D. extend()"],
            "respuesta": "C",
        },
        {
            "pregunta": "¿Que palabra se usa para devolver un valor desde una funcion en python?",
            "opciones": ["A. return","B. output","C. class","D. pass"],
            "respuesta": "A",
        },                                         
        {
            "pregunta": "¿Que funcion de random, sirve para dar valores aleatorios sin repeticiones?",
            "opciones": ["A. random.sample", "B. random.choice", "C. random.gauss", "D. random.choices"],
            "respuesta": "A",
        },                     
        {
            "pregunta": "¿Que funcion se usa para terminar el programa en cualquier parte de un codigo?",
            "opciones": ["A. continue", "B. True", "C. none", "D. break"],
            "respuesta": "D",
        },                                      
        {
            "pregunta": "¿Que funcion convierte una cadena de texto que se encuentra en minusculas a mayuscula?",
            "opciones": ["A. print().upper()", "B. print().lower", "C. print().min", "D. print().title"],
            "respuesta": "A",
        },                                      
        {
            "pregunta": "¿¿Qué función permite sumar todos los elementos de una lista en Python??",
            "opciones": ["A. add()", "B. total ()", "C. reduce()", "D. sum()"],
            "respuesta": "D"
        }                                      
    ],
    "musica": [
        {
            "pregunta": "¿Quien es conocido como el rey del pop?",
            "opciones": ["A. Elvis Presley", "B. Prince", "C. Freddie Mercury", "D. Michael Jackson"],
            "respuesta": "D",
        },
        {
            "pregunta": "¿Qué banda lanzó el álbum Abbey Road en 1969?",
            "opciones": ["A. The Rolling Stones", "B. The Beatles", "C. Led Zeppelin", "D. Pink Floyd"],
            "respuesta": "B",
        },
        {
            "pregunta": "¿Cuál de estos instrumentos pertenece a la familia de los instrumentos de viento?",
            "opciones": ["A. Violín", "B. Trompeta", "C. Guitarra", "D. Batería"],
            "respuesta": "B",
        },
        {
            "pregunta": "¿Qué artista ganó el premio Grammy al mejor álbum del año en 2021?",
            "opciones": ["A. Beyoncé", "B. Taylor Swift", "C. Billie Eilish", "D. Dua Lipa"],
            "respuesta": "C",
        },
        {
            "pregunta": "¿Quién es el guitarrista principal de la banda Queen?",
            "opciones": ["A. Roger Taylor", "B. Brian May", "C. John Deacon", "D. Jimmy Page"],
            "respuesta": "B",
        },
        {
            "pregunta": "¿Qué cantante tiene el álbum 21 como uno de los más vendidos?",
            "opciones": ["A. Adele", "B. Lady Gaga", "C. Katy Perry", "D. Rihanna"],
            "respuesta": "A",
        },
        {
            "pregunta": "¿Qué banda lideró Kurt Cobain?",
            "opciones": ["A. Pearl Jam", "B. Nirvana", "C. Soundgarden", "D. Alice in Chains"],
            "respuesta": "B",
        },
        {
            "pregunta": "¿Cuál de estos géneros musicales es originario de Jamaica?",
            "opciones": ["A. Blues", "B. Reggae", "C. Jazz", "D. Flamenco"],
            "respuesta": "B",
        },
        {
            "pregunta": "¿Qué álbum de Pink Floyd es uno de los más vendidos de la historia?",
            "opciones": ["A. The Wall", "B. Wish You Were Here", "C. Dark Side of the Moon", "D. Animals"],
            "respuesta": "C",
        },
        {
            "pregunta": "¿Qué cantante tiene el récord de más premios Grammy ganados en una sola noche?",
            "opciones": ["A. Michael Jackson", "B. Beyoncé", "C. Stevie Wonder", "D. Paul McCartney"],
            "respuesta": "A"
        }
    ]
}

nombre_usuario = inicio()
puntuacion_final = jugar(preguntas, nombre_usuario)
mostrar_resultado(puntuacion_final, nombre_usuario)
