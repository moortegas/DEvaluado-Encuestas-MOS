class ListadoRespuestas:
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
    # Crear un listado de respuestas
    listado1 = ListadoRespuestas()

    # Agregar respuestas al listado
    listado1.agregar_respuesta("Sí")
    listado1.agregar_respuesta("No")
    listado1.agregar_respuesta("Neutral")

    # Mostrar respuestas del listado
    listado1.mostrar_respuestas()