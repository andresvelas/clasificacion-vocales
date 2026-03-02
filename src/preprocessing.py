import numpy as np





def quitar_silencio(y, frame_size=1024, hop_size=512, threshold=0.01):
    frames = []
    max_energy = np.max(y**2)
    for i in range(0, len(y) - frame_size, hop_size):
        frame = y[i:i+frame_size]
        energia = np.mean(frame**2)
        if energia > threshold * max_energy:
            frames.append(frame)
    if len(frames) == 0:
        return np.array([])
    return np.concatenate(frames)

def remove_iqr_outliers(df, column):
    """
    Elimina outliers de un DataFrame usando el método IQR (1.5 * IQR).
    
    Parámetros:
    - df: pandas DataFrame
    - column: nombre de la columna numérica a analizar
    
    Retorna:
    - DataFrame sin outliers y con índice reseteado
    """
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    filtered_df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

    return filtered_df.reset_index(drop=True)