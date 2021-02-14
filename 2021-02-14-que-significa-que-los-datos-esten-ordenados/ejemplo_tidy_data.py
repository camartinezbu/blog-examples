# Este script contiene las funciones que usé para crear las tablas de
# homicidios en las ciudades incluidas en la entrada de blog
# https://camartinezbu.github.io/posts/que-significa-que-los-datos-esten-ordenados/
#
# La tabla para importar ya cumple con los principios del tidy data

import pandas as pd
import re

datos = pd.read_csv("ejemplo_tidy_data.csv")

# 1. Los nombres de las columnas son valores y no variables

datos_1 = datos.drop(["POBLACIÓN", "TASA"], axis = 1) \
  .pivot(index = ["CODIGO DANE", "MPIO"], columns = "AÑO")["HOMICIDIOS"] \
  .reset_index().rename(columns = {2018:"HOMICIDIOS_2018", 2019:"HOMICIDIOS_2019", 2020:"HOMICIDIOS_2020"})

## Volver a la estructura original

datos_1_original = datos_1.melt(id_vars = ["CODIGO DANE", "MPIO"], \
  var_name = "AÑO", value_name = "HOMICIDIOS")

datos_1_original["AÑO"] = datos_1_original["AÑO"].str.extract(pat = "(\d+)")

# 2. Varias variables están almacenadas en una columna

datos_2 = datos[datos["AÑO"] == 2020].melt(id_vars = ["CODIGO DANE", "MPIO", "AÑO"], \
  var_name = "VARIABLE", value_name = "VALOR")

## Volver a la estructura original

datos_2_original = datos_2.pivot(index = ["CODIGO DANE", "MPIO", "AÑO"], \
  columns = "VARIABLE")["VALOR"].reset_index()

# 3. Las variables están almacenadas tanto en columnas como filas

datos_3 = datos.melt(id_vars = ["CODIGO DANE", "MPIO", "AÑO"], var_name = "VARIABLE", value_name = "VALOR") \
  .pivot(index = ["CODIGO DANE", "MPIO", "VARIABLE"], columns = "AÑO")["VALOR"].reset_index()

## Volver a la estructura original

datos_3_orginal = datos_3.melt(id_vars = ["CODIGO DANE", "MPIO", "VARIABLE"], var_name = "AÑO", value_name = "VALOR") \
  .pivot(index = ["CODIGO DANE", "MPIO", "AÑO"], columns = "VARIABLE")["VALOR"].reset_index()

