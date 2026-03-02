import numpy as np



def unificar_mfccs(
    mfccs_series,
    longitud_objetivo: int = None
    ):
    if longitud_objetivo is None:
        longitudes = [mfcc.shape[1] for mfcc in mfccs_series]
        longitud_objetivo = int(np.median(longitudes))
        print(f"Longitud objetivo calculada: {longitud_objetivo} frames")

    mfccs_unificados = []

    for mfcc in mfccs_series:
        n_mfcc, n_frames = mfcc.shape

        # Añadimos padding para tener el mismo tamaño de serie
        if n_frames < longitud_objetivo:
            padding = longitud_objetivo - n_frames
            mfcc_procesado = np.pad(mfcc, ((0, 0), (0, padding)), mode='edge')
        else:
            mfcc_procesado = mfcc[:, :longitud_objetivo]

        mfccs_unificados.append(mfcc_procesado)

    return np.array(mfccs_unificados), longitud_objetivo