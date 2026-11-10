# ==========================================
# PUNTO A: LIMPIEZA DE REGISTROS DE SENSORES
# ==========================================

def limpiar_registro_sensor(registro_raw: dict[str, str]):

    
    sensor_id = registro_raw["sensor_id"].strip()

    
    temperatura_texto = registro_raw["temperatura"].strip()
    temperatura_texto = temperatura_texto.replace("ºC", "").replace("C", "").strip()

    
    temperatura = float(temperatura_texto)

    
    ubicacion = registro_raw.get("ubicacion", "Ubicación desconocida")

    
    registro_limpio = {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion.strip()
    }

    return registro_limpio


# ==========================================
# DATOS ORIGINALES DE LOS SENSORES
# ==========================================

sensores_raw = [
    {
        "sensor_id": "TEMP.020",
        "temperatura": "24.6",
        "ubicacion": "Zona Norte"
    },
    {
        "sensor_id": "TEMP.021",
        "temperatura": "33.5 C",
        "ubicacion": "Zona Sur"
    },
    {
        "sensor_id": "TEMP.022",
        "temperatura": "26.8 C",
        "ubicacion": "Zona Este"
    },
    {
        "sensor_id": "TEMP.023",
        "temperatura": "32.6 ºC",
        "ubicacion": "Zona Oeste"
    },
    {
        "sensor_id": "TEMP.024",
        "temperatura": "30.1 C",
        
    }
]


# ==========================================
# EJECUCIÓN DEL PUNTO A
# ==========================================

sensores_limpios = []

for sensor in sensores_raw:

    registro = limpiar_registro_sensor(sensor)

    sensores_limpios.append(registro)




# ==========================================
# PUNTO B: ANÁLISIS ESTADÍSTICO DE SENSORES
# ==========================================

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):

    
    sensores_alerta = list(filter(
        lambda sensor: sensor["temperatura"] > umbral_temperatura,
        lista_sensores_limpios
    ))

    
    lista_sensores_alerta = list(map(
        lambda sensor: sensor["sensor_id"],
        sensores_alerta
    ))

    
    temperaturas = list(map(
        lambda sensor: sensor["temperatura"],
        lista_sensores_limpios
    ))

    
    if len(temperaturas) > 0:
        promedio_temperatura = sum(temperaturas) / len(temperaturas)
    else:
        promedio_temperatura = 0.0

    
    return lista_sensores_alerta, promedio_temperatura


# ==========================================
# EJECUCIÓN DEL PUNTO B
# ==========================================


umbral = 30.0


resultado = generar_resumen_sensores(sensores_limpios, umbral)


lista_sensores_alerta, promedio_temperatura = resultado

print("===== REGISTROS DE SENSORES LIMPIOS =====")

for sensor in sensores_limpios:
    print(f"sensor: {sensor["sensor_id"]} . temperatura:{sensor["temperatura"]} . ubicación: {sensor["ubicacion"]}")


print("\n===== RESULTADOS DEL ANÁLISIS =====")

print("Umbral de temperatura:", umbral, "°C")

print("Sensores en alerta:", lista_sensores_alerta)

print("Promedio general:", round(promedio_temperatura, 2), "°C")