from pregunta import Pregunta

class Encuesta():
    def __init__(self, nombre: str, preguntas:str):
        self.nombre = nombre
        self.__preguntas = [
            Pregunta(
            p["enunciado"],
            p["ayuda"], 
            p["alternativas"], 
            p["requerido"], 
        ) for p in preguntas
        ]
        # numeros = [x for x in range(10)]
        # numeros = []
        # for x in range(10)
        self.__listados_respuestas = []

        def mostrar_encuesta(self):
            print(self.nombre)

            for p in self.__preguntas:
                p.mostrar_pregunta()

        def agregar_listado_respuesta(self, listado_respuestas):
            self.__listados_respuestas.append(listado_respuestas)

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, preguntas: list, edad_min:int, edad_max:int):
             super().__init__(nombre, preguntas)

             self.__edad_min = edad_min
             self.__edad_max = edad_max

    @property
    def edad_min(self):
        return self.edad_min
        
    @edad_min.setter
    def edad_min(self, nuevo_min):
        self.__edad_min = nuevo_min

    @property
    def edad_max(self):
        return self.edad_max
        
    @edad_max.setter
    def edad_max(self, nuevo_max):
        self.__edad_max = nuevo_max

    def agregar_respuesta(self, respuestas:list):
        if self.__edad_min <= respuestas.usuario.edad <= self.__edad_max:
            super().agregar_listado_respuestas(respuestas)


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, regiones):
        self.regiones = regiones
        self.respuestas = []

    def agregar_respuesta(self, respuesta, region):
        """Agrega una respuesta a la lista de respuestas si la región es válida."""
        if region in self.regiones:
            self.respuestas.append((respuesta, region))
        else:
            print(f"La región {region} no es válida. No se agregó la respuesta.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una encuesta limitada a ciertas regiones
    regiones_validas = [1, 2, 3]
    encuesta_region = EncuestaLimitadaRegion(regiones=regiones_validas)

    # Agregar respuestas a la encuesta
    encuesta_region.agregar_respuesta(respuesta="Sí", region=1)
    encuesta_region.agregar_respuesta(respuesta="No", region=2)
    encuesta_region.agregar_respuesta(respuesta="Neutral", region=4)  # Región no válida
    encuesta_region.agregar_respuesta(respuesta="Otro", region=3)

    # Mostrar respuestas de la encuesta
    for respuesta, region in encuesta_region.respuestas:
        print(f"Respuesta: {respuesta}, Región: {region}")












