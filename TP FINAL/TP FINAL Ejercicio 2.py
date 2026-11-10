
# ==========================================
# EcoTech Solutions
# ==========================================


class StockInvalidoError(Exception):
    """Error cuando se intenta asignar un stock negativo."""
    pass


class DispositivoEcológico:

    def __init__(self, modelo: str, precio: float, stock: int):

        self.modelo = modelo
        self.precio = precio
      
        self.set_stock(stock)

    
    def get_stock(self) -> int:
        return self.__stock

    
    def set_stock(self, nuevo_stock: int):

        if nuevo_stock < 0:
            raise StockInvalidoError(
                "El stock no puede tomar valores negativos."
            )

        self.__stock = nuevo_stock

    
    def obtener_ficha_tecnica(self) -> str:

        return (
            f"Modelo: {self.modelo} | "
            f"Precio: ${self.precio} | "
            f"Stock: {self.get_stock()} unidades"
        )

    
    def a_diccionario(self) -> dict:

        return {
            "tipo": "DispositivoEcológico",
            "modelo": self.modelo,
            "precio": self.precio,
            "stock": self.get_stock()
        }



class PanelSolar(DispositivoEcológico):

    def __init__(
        self,
        modelo: str,
        precio: float,
        stock: int,
        eficiencia_watts: int
    ):

        
        super().__init__(modelo, precio, stock)

        
        self.eficiencia_watts = eficiencia_watts

    
    def obtener_ficha_tecnica(self) -> str:

        ficha_base = super().obtener_ficha_tecnica()

        return (
            f"{ficha_base} | "
            f"Potencia: {self.eficiencia_watts} W | "
            f"Producto de energía renovable"
        )

    
    def a_diccionario(self) -> dict:

        datos = super().a_diccionario()

        datos["tipo"] = "PanelSolar"
        datos["eficiencia_watts"] = self.eficiencia_watts

        return datos



# ==========================================
# PUNTO B: PERSISTENCIA Y GESTIÓN DEL CATÁLOGO
# ==========================================

import json



class GestorInventario:

    @staticmethod
    def guardar_catalogo_json(
        lista_dispositivos: list,
        ruta_archivo: str
    ):

        
        catalogo = []

        for dispositivo in lista_dispositivos:
            catalogo.append(dispositivo.a_diccionario())

        
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:

            json.dump(
                catalogo,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print(f"Catálogo guardado correctamente en: {ruta_archivo}")




if __name__ == "__main__":

    

    dispositivo1 = DispositivoEcológico(
        "Termostato-Eco",
        350.0,
        8
    )

    dispositivo2 = PanelSolar(
        "SolarMax-500",
        1200.0,
        10,
        500
    )

    dispositivo3 = PanelSolar(
        "SolarPro-800",
        1800.0,
        5,
        800
    )

    
    lista_dispositivos = [
        dispositivo1,
        dispositivo2,
        dispositivo3
    ]

    

    print("\n--- PRUEBA DE VALIDACIÓN DE STOCK ---")

    try:

        dispositivo1.set_stock(-5)

    except StockInvalidoError as error:

        print(f"[ERROR CONTROLADO]: {error}")

    

    print("\n--- FICHAS TÉCNICAS DEL CATÁLOGO ---")

    for dispositivo in lista_dispositivos:

        print(dispositivo.obtener_ficha_tecnica())

    

    print("\n--- EXPORTACIÓN DEL CATÁLOGO ---")

    GestorInventario.guardar_catalogo_json(
        lista_dispositivos,
        "catalogo_ecotech.json"
    )
