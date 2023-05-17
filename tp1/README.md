# tda_tp1

## Segunda Parte

Para ejecutar los 3 algoritmos (greedy, greedy_alternative, dynamic_programming) se puede ejecutar con:

```python segunda_parte/main.py```

Este comando generará un set de productos y sobornos random, bastados en los parametros que se encuentran dentro del archivo ```segunda_parte/aux.py```

Estos parametros son:

```
MAX_QTY = 20
MAX_PACKAGES = 5
MAX_TYPES = 2
```

```MAX_QTY``` indica la máxima cantidad de unidades que puede tener un paquete, cuando se genera el set de datos, a cada paquete se le asigna una cantidad que es un valor random entre 1 y MAX_QTY.

```MAX_PACKAGES``` indica la cantidad de paquetes que se generaran para un tipo de producto

```MAX_TYPES``` indica la cantidad de tipos de productos que se generaran, cada tipo de producto se diferencia con un id númerico al cual se le asigna a cada paquete.

### Pruebas de Optimalidad

En caso de querer correr casos especificos, se puede usar el script que se encuentra en 

```segunda_parte/optimality_test.py```

este archivo levanta desde un csv ```test_cases.csv``` los escenarios y los ejecuta, este csv tiene el siguiente formato:

```
scenario,type,packages,bribe
```

Donde 
 - scenario: corresponde a un id para identificar el caso de prueba, si se quiere que un escenario ejecute el calculo del óptimo con muchos productos diferentes, estos deben tener el mismo scenario
 - type: tipo de producto, debe ser un id númerico
 - packages: indican cuantos paquetes y sus cantidades, cada paquete debe separarse con ```;```
- bribe: indica la cantidad de debe ser sobornada (solo puede haber un valor)

#### ejemplo:
```
scenario,type,packages,bribe
1,0,10;8;5;2,12
```

### Pruebas de Stress

Si se desean correr pruebas de stress y graficar los resultados, se pueden hacer desde el notebook que se encuentra en ```segunda_parte/mediciones.ipynb```. Estos casos de prueba se desarrollaron para validar como se compartan los algoritmos al variar la cantidad de paquetes y la cantidad de unidades por paquete, por defecto solo acepta un solo tipo de producto.
