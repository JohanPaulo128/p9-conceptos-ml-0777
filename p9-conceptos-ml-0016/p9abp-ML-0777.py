
import pandas as pd

datos4 = {
    'distancia_km': [4.8, 1.0, 3.3, 6.5, 2.2],
    'trafico_nivel': [3, 1, 2, 3, 1],
    'edad_repartidor': [29, 24, 36, 41, 21],
    'tiempo_entrega_min': [45, 8, 28, 60, 15]
}

df = pd.DataFrame(datos4)

X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']]
y = df['tiempo_entrega_min']

print("--- DATOS DE ENTRADA (X) ---")
print(X)

print("\n--- VARIABLE OBJETIVO (y) ---")
print(y)

print("\nJohan Paulo Aros Reveles NC 0016")