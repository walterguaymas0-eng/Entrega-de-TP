def calcular_emisiones_carbono(
    consumo_kwh: float,
    factor_emision: float = 0.4
) -> float:

    # Validamos que el consumo no sea negativo
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")

    # Calculamos las emisiones de carbono
    emisiones = consumo_kwh * factor_emision

    return emisiones



import unittest


class TestCalculoEmisiones(unittest.TestCase):

    # Prueba 1: Verificar el cálculo con valores nominales
    def test_calculo_correcto(self):

        resultado = calcular_emisiones_carbono(100.0, 0.4)

        self.assertEqual(resultado, 40.0)


    # Prueba 2: Verificar el cálculo utilizando el factor por defecto
    def test_factor_emision_por_defecto(self):

        resultado = calcular_emisiones_carbono(200.0)

        self.assertEqual(resultado, 80.0)


    # Prueba 3: Verificar que un consumo de cero genere cero emisiones
    def test_consumo_cero(self):

        resultado = calcular_emisiones_carbono(0.0)

        self.assertEqual(resultado, 0.0)


    # Prueba 4: Verificar que un consumo negativo genere ValueError
    def test_consumo_negativo_lanza_excepcion(self):

        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50.0)


# Ejecutamos las pruebas
if __name__ == "__main__":
    unittest.main()



registros_consumo = [

    {"planta": "Norte", "consumo_kwh": 1200},

    {"planta": "Sur", "consumo_kwh": 850},

    {"planta": "Norte", "consumo_kwh": 1400},

    {"planta": "Este", "consumo_kwh": 950},

    {"planta": "Sur", "consumo_kwh": 1100}

]


def obtener_metricas_consumo(registros):

    # Variable para acumular las emisiones globales
    total_emisiones = 0.0

    # Diccionario para acumular el consumo de cada planta
    consumos_por_planta = {}

    # Recorremos todos los registros
    for registro in registros:

        planta = registro["planta"]
        consumo = registro["consumo_kwh"]

        # Calculamos las emisiones utilizando la función anterior
        emisiones = calcular_emisiones_carbono(consumo)

        # Acumulamos las emisiones globales
        total_emisiones += emisiones

        # Acumulamos el consumo correspondiente a cada planta
        consumos_por_planta[planta] = (
            consumos_por_planta.get(planta, 0) + consumo
        )

    # Determinamos cuál es la planta con mayor consumo
    if consumos_por_planta:

        planta_top = max(
            consumos_por_planta,
            key=consumos_por_planta.get
        )

    else:
        planta_top = "Sin datos"

    # Retornamos las métricas obtenidas
    return {
        "total_emisiones": total_emisiones,
        "planta_top": planta_top
    }




from django.shortcuts import render


def vista_panel_sustentabilidad(request):

    # Obtenemos las métricas procesadas
    metricas = obtener_metricas_consumo(registros_consumo)

    # Creamos el diccionario de contexto
    contexto = {

        "total_emisiones": metricas["total_emisiones"],

        "planta_top": metricas["planta_top"]

    }

    # Renderizamos la plantilla HTML
    return render(
        request,
        "sustentabilidad/panel.html",
        contexto
    )

