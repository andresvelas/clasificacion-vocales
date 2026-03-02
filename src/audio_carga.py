import os
import librosa
import pandas as pd

vocales_validas = {"a", "e", "i", "o", "u"}
generos_validos = {"hombre", "mujer"}

FORMATOS_AUDIO = {".ogg", ".opus"}


def carga_path_audios(path):
    """
    Carga audios desde un directorio, soportando .ogg, .opus y otros formatos.
    Nomenclatura esperada: vocal_genero_*.extension (ej: a_hombre_01.opus)
    """
    datos = []

    for archivo in os.listdir(path):
        # Verificar si el archivo tiene una extensión de audio válida
        extension = os.path.splitext(archivo)[1].lower()
        if extension not in FORMATOS_AUDIO:
            continue

        # Quitar la extensión para parsear el nombre
        nombre_sin_ext = os.path.splitext(archivo)[0]
        partes = nombre_sin_ext.split("_")

        if len(partes) < 2:
            print(f"Archivo ignorado (formato de nombre incorrecto): {archivo}")
            continue

        vocal, genero = partes[0], partes[1]

        if vocal not in vocales_validas or genero not in generos_validos:
            print(f"Archivo ignorado (vocal o género inválido): {archivo}")
            continue

        path_audio = os.path.join(path, archivo)

        try:

            y, sr = librosa.load(path_audio, sr=22050)

            datos.append({
                "archivo": archivo,
                "y": y,
                "sr": sr,
                "vocal": vocal,
                "genero": genero,
                "duracion": len(y) / sr,
            })

        except Exception as e:
            print(f"Error cargando {archivo}: {e}")

    if not datos:
        print("No se cargaron audios. Verifica el path y los nombres de archivo.")
    else:
        print(f"Se cargaron {len(datos)} audios exitosamente")

    df = pd.DataFrame(datos)
    return df


def guardar_df(df, nombre, path_destino):
    """
    Guarda el DataFrame en formato Parquet con compresión.
    """
    os.makedirs(path_destino, exist_ok=True)

    numero_audios = len(df)

    ruta_final = os.path.join(
        path_destino,
        f"dataset_{nombre}_{numero_audios}.parquet"
    )

    df.to_parquet(ruta_final, compression="zstd")

    print(f"Dataset guardado en:\n{ruta_final}")
    
    return ruta_final


def verificar_audios(path):
    """
    Analiza el directorio y muestra un resumen de los archivos encontrados.
    """
    formatos = {}
    validos = 0
    invalidos = 0
    
    for archivo in os.listdir(path):
        extension = os.path.splitext(archivo)[1].lower()
        if extension in FORMATOS_AUDIO:
            formatos[extension] = formatos.get(extension, 0) + 1
            
            nombre_sin_ext = os.path.splitext(archivo)[0]
            partes = nombre_sin_ext.split("_")
            
            if len(partes) >= 2 and partes[0] in vocales_validas and partes[1] in generos_validos:
                validos += 1
            else:
                invalidos += 1
    
    print("\nResumen del directorio:")
    print(f"  Archivos válidos: {validos}")
    print(f"  Archivos inválidos: {invalidos}")
    print(f"  Formatos encontrados: {formatos}")
    
    return formatos