# Calculadora de Divisas para Viajeros

Este proyecto es una calculadora sencilla en Python que permite convertir una cantidad de dinero desde una moneda base (por ejemplo USD) a otra moneda extranjera usando una tasa de cambio.

El objetivo es ayudar a viajeros frecuentes a calcular rápidamente cuánto dinero obtendrán en la moneda local del país que visiten.

El programa utiliza una función llamada `exchange_money` que recibe:

`budget`: cantidad de dinero que deseas cambiar.
`exchange_rate`: tasa de cambio del país destino.

La función devuelve el equivalente en la moneda extranjera.

## Fórmula utilizada

moneda_extranjera = budget / exchange_rate

## Ejemplo

```python
def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

print(exchange_money(300, 0.0075))
```

Resultado esperado:

```
40000.0
```

## Cómo ejecutar el programa

1. Instalar Python.
2. Guardar el archivo como `exchange_money.py`.
3. Ejecutar en la terminal:

```
python exchange_money.py
```


Python

Diego
