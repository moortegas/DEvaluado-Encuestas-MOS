from encuesta import Encuesta

class Usuario:
    def __init__(self, correo, edad, region):
        self.correo = correo
        self.edad = edad
        self.region = region

    def leer_datos(self):
        """Lee los datos del usuario."""
        print(f"Correo: {self.correo}")
        print(f"Edad: {self.edad}")
        print(f"Región: {self.region}")

    def modificar_datos(self, nuevo_correo=None, nueva_edad=None, nueva_region=None):
        """Modifica los datos del usuario."""
        if nuevo_correo:
            self.correo = nuevo_correo
        if nueva_edad:
            self.edad = nueva_edad
        if nueva_region:
            self.region = nueva_region


class Encuesta:
    def __init__(self):
        self.respuestas = []

    def agregar_respuesta(self, respuesta):
        """Agrega una respuesta a la lista de respuestas."""
        self.respuestas.append(respuesta)

    def mostrar_respuestas(self):
        """Muestra todas las respuestas recopiladas."""
        for i, respuesta in enumerate(self.respuestas, start=1):
            print(f"Respuesta {i}: {respuesta}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un usuario
    usuario1 = Usuario(correo="usuario@example.com", edad=30, region=1)

    # Leer datos del usuario
    usuario1.leer_datos()

    # Modificar datos del usuario
    usuario1.modificar_datos(nuevo_correo="nuevo_correo@example.com", nueva_edad=35)

    # Crear una encuesta
    encuesta1 = Encuesta()

    # Agregar respuestas a la encuesta
    encuesta1.agregar_respuesta("Sí")
    encuesta1.agregar_respuesta("No")
    encuesta1.agregar_respuesta("Neutral")

    # Mostrar respuestas de la encuesta
    encuesta1.mostrar_respuestas()
