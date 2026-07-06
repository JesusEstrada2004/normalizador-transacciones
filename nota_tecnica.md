# Nota técnica

## Decisiones de diseño

Se definió un modelo normalizado común para representar transacciones provenientes de múltiples fuentes. El esquema final contiene los campos id, amount, currency, timestamp, status y source.

La decisión de incluir el campo source permite conservar trazabilidad del origen de cada transacción. Los estados se normalizaron a tres valores principales: SUCCESS, FAILED y PENDING, para facilitar el análisis y la generación de métricas.

Las transacciones inválidas no se descartan silenciosamente. El sistema las separa en una lista específica junto con la razón del error, permitiendo revisar problemas de calidad de datos.

## Reglas de normalización

Los montos se convierten a tipo decimal, eliminando símbolos como € o $. Las monedas se convierten a mayúsculas. Las fechas se transforman a formato ISO-8601. Los estados se traducen usando un archivo de reglas externo.

## Uso de IA

La IA fue utilizada como apoyo para estructurar el código, proponer funciones de validación, modularizar responsabilidades y diseñar la interfaz CLI. Las decisiones finales sobre el esquema normalizado, criterios de validez y reglas de transformación fueron revisadas y ajustadas por el estudiante.

## Separación de responsabilidades

El proyecto se divide en módulos:

- loader.py: carga de archivos JSON y reglas.
- normalizer.py: detección de fuente y normalización.
- validator.py: validación y separación de registros inválidos.
- metrics.py: cálculo de métricas.
- cli.py: interfaz interactiva.