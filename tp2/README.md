# TP2 - Problema del Empaquetamiento

## Ejecución

```
/tdatp2 <E>|<A>|<A2> <datos.txt> <-v|--verbose>
```

Donde 
 - E: Solución exacta
 - A: Aproximación Cátedra
 - A2: Aproximación Alumnos

La opción `-v, --verbose` además de dar el resultado (la cantidad de envases)
mostrará como se componen dichos envases.

### Datos de Prueba

En el directorio `src/samples` se encuentran provistos algunos conjuntos de datos

### Generación Datos de Prueba

Si se desea hacer pruebas alternativas, existe un script para generar datos aleatorios

```
python data.py -n <N>
```

Donde **N** es la cantidad de elementos que deseemos generar. La salida del script se puede
_pipear_ directamente a un file ya que contiene el formato esperado por el programa principal

```
python data.py -n 8 | tee /tmp/aux.txt && ./tdatp2 A2 /tmp/aux.txt
```
