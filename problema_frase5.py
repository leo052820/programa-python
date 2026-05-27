# Nombre: jose leonardo lopez rangel
# progama de ingenieria en sistemas
# autoria propia

#PROBLEMA 4 - Videoteca Digital

# Matriz con información de películas/series
# Formato:
# [Título, Año de Lanzamiento, Calificación, Género]

videoteca = [
    ["Inception", 2010, 9, "Ciencia Ficción"],
    ["Avatar", 2009, 8, "Acción"],
    ["Interstellar", 2014, 10, "Ciencia Ficción"],
    ["Titanic", 1997, 7, "Drama"],
    ["Joker", 2019, 9, "Drama"],
    ["The Batman", 2022, 8, "Acción"],
    ["Dune", 2021, 9, "Ciencia Ficción"]
]

# Función para contar títulos que cumplen criterios

def contar_titulos(matriz, calificacion_minima, anio_limite):

    contador = 0

    for titulo in matriz:

        # Datos de cada fila
        nombre = titulo[0]
        anio = titulo[1]
        calificacion = titulo[2]
        genero = titulo[3]

        # Verificar condiciones
        if calificacion >= calificacion_minima and anio >= anio_limite:
            contador += 1

            print("Título:", nombre)
            print("Año:", anio)
            print("Calificación:", calificacion)
            print("Género:", genero)
            print("---------------------------")

    return contador

# Programa principal

# Solicitar datos al usuario
calificacion_usuario = int(input("Ingrese la calificación mínima: "))
anio_usuario = int(input("Ingrese el año límite: "))

# Llamar función
resultado = contar_titulos(
    videoteca,
    calificacion_usuario,
    anio_usuario
)

# Mostrar resultado final
print("Total de títulos que cumplen los criterios:", resultado)