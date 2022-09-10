# Reto_Multiagentes

Proyecto desarrollado para la materia "Modelación de sistemas multiagentes con gráficas computacionales" por el equipo:

- [Ruy Guzmán Camacho](https://github.com/Ruy-GC) | A01639912
- [Santiago González de Cosío Romero](https://github.com/sant-gdc) | A01639813
- [Adrián Becerra Meza](https://github.com/AdrianBecerra411) | A01640329

El proyecto contsa de una simulación de una rotonda y el control del tráfic en ella considerando entradas y salidas, choques de vehiculos y funcionamiento de semaforos. Con el fin de demostrar la funcionalidad de los sistemas mutliagentes para la resolución de problemas de aplicación real. El proyecto consta de 3 partes: 
 - [x] Sistema multiagentes
 - [x] Servidor 
 - [x] Simulación en Unreal Engine

## Parte 1: Modelado de sistema multiagentes

Se genera una cantidad parametrizable de agentes de vehiculos que se inicializan en 4 posiciones aleatorias para integrarse a la rotonda. La rotonda se simula mediante agentes que respresentan la ruta a tomar dentro de la misma además se establecen puntos de salida que se le asignan a los vehiculos de manera aleatoria, se manejan los choques y funcionamiento de semaforos.

### Parametros de la simulación
```python
parameters = {
    'Tree density': 1,
    'size': 40,
    'steps': 100,
    'trafico': 5
}
```

### Generación de JSON para enviar al servidor
```python
if carro.inside == 1 or carro.inside == 2 or carro.inside == 3:
    self.carTable[carro.id]["steps"][str(self.curr_step)] = {
        "x":positions[carro][1],
        "y":positions[carro][0],
        "z": 70
    }
else: 
    self.carTable[carro.id]["steps"][str(self.curr_step)] = {
        "x": carro.id * 2,
        "y": carro.id * 2,
        "z": -1400
    }
```
### Generación de circulo de la rotonda
```python
 def makeCircle(self,startX,startY,r):
        map = []
        Epsilon = 2.2
        for y in range(startX-r,startX+r+1):
            for x in range(startY-r,startY+r+1):
                # see if we're close to (x-a)**2 + (y-b)**2 == r**2
                if abs((x-startX)**2 + (y-startY)**2 - r**2) < Epsilon**2:
                    map.append((x,y))
        return map
 ```
## Parte 2: Servidor entre AgentPy y Unreal Engine
Servidor intermediario con conexión a Firebase para el traspaso de información entre Agentpy y la simulación de Unreal Engine.

### Configuración de conexión a firebase
```python
config = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "databaseURL": os.getenv("DATABASE_URL"),
    "storageBucket": os.getenv("STORAGE_BUCKET")
}
```
requiere un archivo **".env"** con los siguentes campos como se muestra en **example.env**

```
API_KEY = "key"
AUTH_DOMAIN = "domain"
DATABASE_URL = "url"
STORAGE_BUCKET = "bucket"
```
### Instalación e iniciar el servidor
``` bash
cd App/Server

#windows
python -m venv venv
venv/Scripts/activate 
pip install -r requirements.txt
flask run

#linux
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
flask run
```

## Parte 3: Simulación en Unreal Engine
Simulación en UE4 que obtiene los datos del servidor para modelar el movimeitno de vehiculos en una rotonda, utiliza el plugin de vaRest y las herramientas de Unreal Engine para el manejo de datos en JSON.

**También Disponible en Drive:**
https://drive.google.com/file/d/1eL-kt_jaXeI1zhRfV3zzLE1s-JzZojA8/view?usp=sharing




