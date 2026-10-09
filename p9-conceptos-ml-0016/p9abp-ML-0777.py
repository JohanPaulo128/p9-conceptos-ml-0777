print("Johan Paulo Aros Reveles NC 0016")


import pandas as pd

datos = {
    'id_paciente': [101, 102, 103, 104],
    'edad': [25, 50, 35, 60],
    'nivel_glucosa': [90, 160, 110, 180],
    'presion_arterial': [115, 140, 120, 150],
    'indice_masa_corporal': [22.5, 31.0, 26.0, 33.5],
    'diagnostico_diabetes': [0, 1, 0, 1]
}

df = pd.DataFrame(datos)

df = df.drop(columns=['id_paciente'])

X = df[['edad', 'nivel_glucosa',
        'presion_arterial', 'indice_masa_corporal']]

y = df['diagnostico_diabetes']

print("--- DATOS DE ENTRADA (X) ---")
print(X)

print("\n--- VARIABLE OBJETIVO (y) ---")
print(y)

print("Johan Paulo Aros Reveles NC 0016")