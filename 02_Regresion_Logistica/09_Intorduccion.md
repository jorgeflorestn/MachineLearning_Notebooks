# Regresion logistica

Es un algoritmo de clasificación

Es un modelo estadístico que se utiliza para determinar la probabilidad de que ocurra un evento. Muestra la relación entre características y luego calcula la probabilidad de un resultado determinado.

Es similar a la regresión lineal, excepto que en lugar de un resultado gráfico, la variable objetivo es discreta.

Un algoritmo de clasificación se puede dividir entre las diversas salidas pero discretas, es decir, los datos no son nubes de puntos continuos, sino para varios y limitados numeros de dígitos.


Simple. para $ y \epsilon \{ 0, 1 \} $

Multiclase para $ y \epsilon \{ 0, 1, 2, 3, 4, ..., n \} $


## Modelo de regresión lineal

En un intento de usar la regresion lineal se puede usar

$$
    h_{\theta} (x) = \theta ^T X
$$3

Pero es muy sensible a las anomalías

Dentro del modelo de regresion logistica se desa cambiar la hipotesis de condicion dada por $ h_{\theta} (x) >= 0.5 $ a 

$$
    0 <= h_{\theta} (x) <= 1
$$


## Modificaciones del algoritmo del descenso de gradiente

$$
    J(\theta) = - \frac{1}{m} \sum (y \ln(h) + (1 - y) \ln (1 - h))
$$

Generalizando

$$
    J(\theta) = - \frac()    
$$