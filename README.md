# Clasificación automática de vocales españolas

Sistema de reconocimiento automático de las cinco vocales del español  
(/a/, /e/, /i/, /o/, /u/) a partir de grabaciones de audio propias.

---

## Pipeline del sistema

![Pipeline](reports/figures/pipeline.png)

El proyecto implementa el flujo clásico de reconocimiento de patrones:

1. Preprocesamiento de señal  
2. Extracción de características (MFCC)  
3. Construcción del vector de características (429 dimensiones)  
4. Clasificación mediante SVM y ANN  
5. Evaluación y análisis comparativo  

---

## Resultados principales

| Modelo | Accuracy |
|--------|----------|
| ANN (regularizada) | **88.89%** |
| SVM (RBF, C=10) | **88.89%** |
| Solución IA generativa | 55.56% |

En un escenario de *small data*, el modelo SVM mostró un rendimiento equivalente al Deep Learning con menor complejidad y mayor estabilidad.

---

## Estructura del repositorio



project-root/
├── data/ # Datos (no incluidos por privacidad)
├── notebooks/ # Desarrollo experimental y análisis detallado
├── src/ # Código modular del proyecto
├── models/ # Modelos entrenados
├── reports/ # Memoria y figuras
├── setup.py # Configuración del paquete
└── README.md # Este archivo



---

## Dataset

- 118 muestras tras limpieza
- 5 clases balanceadas (~22–25 por vocal)
- Grabaciones propias
- Los audios originales no se incluyen por motivos de privacidad

Para reproducir el experimento, coloque sus audios en:

---

## Instalación

Clonar el repositorio:

```bash
git clone <url-del-repo>
cd clasificacion-vocales