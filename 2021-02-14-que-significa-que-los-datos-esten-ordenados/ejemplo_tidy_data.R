# Este script contiene las funciones que usé para crear las tablas de
# homicidios en las ciudades incluidas en la entrada de blog
# https://camartinezbu.github.io/posts/que-significa-que-los-datos-esten-ordenados/
#
# La tabla para importar ya cumple con los principios del tidy data

library(dplyr)
library(tidyr)
library(readr)

datos <- read_csv("ejemplo_tidy_data.csv")

# 1. Los nombres de las columnas son valores y no variables

datos_1 <- datos %>%
  select(-c(POBLACIÓN, TASA)) %>%
  pivot_wider(names_from = AÑO, values_from = HOMICIDIOS, names_prefix = "HOMICIDIOS_")

## Volver a la estructura original

datos_1_original <- datos_1 %>%
  pivot_longer(cols = c(`HOMICIDIOS_2018`:`HOMICIDIOS_2020`), names_to = "AÑO", values_to = "HOMICIDIOS", names_pattern = "(\\d+)")
  
# 2. Varias variables están almacenadas en una columna

datos_2 <- datos %>%
  filter(AÑO == 2020) %>%
  pivot_longer(cols = c(POBLACIÓN, HOMICIDIOS, TASA), values_to = "VALOR", names_to = "VARIABLE")

## Volver a la estructura original

datos_2_original <- datos_2 %>%
  pivot_wider(names_from = VARIABLE, values_from = VALOR)

# 3. Las variables están almacenadas tanto en columnas como filas

datos_3 <- datos %>%
  pivot_longer(cols = c(POBLACIÓN, HOMICIDIOS, TASA), names_to = "VARIABLE", values_to = "VALOR") %>%
  pivot_wider(names_from = AÑO, values_from = VALOR)

## Volver a la estructura original
  
datos_3_original <- datos_3 %>%
  pivot_longer(cols = c(`2018`:`2020`), names_to = "AÑO", values_to = "VALOR") %>%
  pivot_wider(names_from = VARIABLE, values_from = VALOR)




