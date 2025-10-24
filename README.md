# 🧠 Taller 2 - Simulaciones con PyBullet y Docker

**Universidad Santo Tomás**  
**Facultad de Ingeniería Electrónica**  
**Asignatura:** Laboratorio de Digitales  
**Integrantes:**  
- Yossed Mauricio Riaño Páez  
- Miguel Montaña  
- Jeferson Hernández  

---

## 📘 Introducción

El presente taller tiene como propósito desarrollar y comprender el funcionamiento de simulaciones físicas mediante **PyBullet**, un motor de física en tiempo real ampliamente utilizado en robótica, inteligencia artificial y control.  
Adicionalmente, se aplicó **Docker** para garantizar la portabilidad de los entornos de simulación, permitiendo replicar cada experimento en cualquier equipo sin conflictos de dependencias.

Las simulaciones abordadas fueron:
- Drones controlados con *Gym-PyBullet-Drones*.  
- Robot **Baxter** de Rethink Robotics.  
- Robot humanoide **ATLAS** desarrollado por Boston Dynamics, ejecutado mediante el paquete *PyBullet Robots*.

---

## 🚀 1. Clonación del Repositorio Principal

Se realizó la clonación del repositorio base para la ejecución de los tres entornos de simulación.  
El proceso se llevó a cabo desde GitHub utilizando el siguiente comando:

```bash
git clone https://github.com/tu_usuario/Taller_2_Digitales.git
cd Taller_2_Digitales
```

📸 **Evidencia: Clonación del Repositorio**

![Clonacion drones](https://github.com/user-attachments/assets/3ca7d900-c220-49f3-b37d-e3f1c8851d78)


---

## ⚙️ 2. Instalación de Dependencias

Para garantizar el correcto funcionamiento de las simulaciones, se instalaron las librerías necesarias en el entorno Python.

```bash
pip install pybullet gym-pybullet-drones pybullet_robots
```

Estas dependencias permiten la carga de modelos URDF, la simulación de articulaciones, la generación de entornos 3D interactivos y la visualización del comportamiento físico en tiempo real.

---

## 🧩 3. Ejecución de las Simulaciones

### 🚁 3.1 Simulación de Drones

El paquete **Gym-PyBullet-Drones** ofrece un entorno físico donde se modelan drones con diferentes configuraciones de propulsión, control y sensores.  
Se ejecutó la simulación principal con el siguiente comando:

```bash
python fly.py
```

📸 **Evidencia: Simulación de Drones**

![Drones](https://github.com/user-attachments/assets/70dc88d8-09d0-4fca-b16e-07850c4da0b6)


**Descripción técnica:**  
El script inicializa un entorno 3D donde se modela el comportamiento aerodinámico de un dron tipo *quadrotor*. Se analiza la estabilidad, el control PID y la respuesta dinámica ante perturbaciones.

---

### 🤖 3.2 Simulación del Robot Baxter

El robot **Baxter** es un manipulador bimanual con visión estereoscópica, diseñado para la interacción segura con humanos.  
Su entorno de simulación se encuentra en el repositorio *pybullet_robots*, desarrollado por Erwin Coumans (creador de PyBullet).

#### 🔍 Clonación del Proyecto Baxter

```bash
git clone https://github.com/erwincoumans/pybullet_robots.git
cd pybullet_robots
```

📸 **Evidencia: Clonación Exitosa**

![Clonacion BAXTER](https://github.com/user-attachments/assets/8e624f40-62ff-4296-8405-e992ebacb5fa)


#### ▶️ Ejecución

```bash
python baxter_demo.py
```

📸 **Evidencia: Ejecución del Robot Baxter**

![BAXTER 2](https://github.com/user-attachments/assets/28aee52c-47f5-4d29-8577-c018f240b1b7)

**Descripción técnica:**  
El modelo simula los 14 grados de libertad de los brazos de Baxter, permitiendo la visualización del control de articulaciones, la planificación de trayectorias y la manipulación de objetos virtuales mediante PyBullet.

---

### 🦾 3.3 Simulación del Robot ATLAS (Docker + PyBullet)

#### 🧱 Descripción

El robot **ATLAS** es un humanoide avanzado desarrollado por **Boston Dynamics**, diseñado para tareas de locomoción, equilibrio dinámico y manipulación en entornos complejos.  
Para esta simulación, se utilizó el entorno de **PyBullet Robots**, que incluye un modelo físico detallado de ATLAS.

#### 🔍 Clonación del Proyecto ATLAS

```bash
git clone https://github.com/erwincoumans/pybullet_robots.git
cd pybullet_robots/robots/atlas
```

📸 **Evidencia: Clonación del Repositorio ATLAS**

![Clonacion atlas](https://github.com/user-attachments/assets/259d9b6e-268e-43e9-ad39-a8d77d7e5c13)

---

#### ▶️ Ejecución de la Simulación

Para ejecutar la simulación:

```bash
python atlas.py
```
o
```bash
python atlas_demo.py
```

📸 **Evidencia: Ejecución del Robot ATLAS**

![Atlas](https://github.com/user-attachments/assets/10421a62-5357-4244-8b46-1eded09f4d79)


**Descripción técnica:**  
El modelo del robot ATLAS implementa un sistema de control basado en torque aplicado a las articulaciones, simulando el movimiento humanoide.  
Se utiliza la cinemática directa e inversa para determinar posiciones y orientaciones de los miembros, y el motor de física de PyBullet resuelve las colisiones y la gravedad en tiempo real.

---

## 📦 4. Integración con Docker

Docker se utilizó para aislar las dependencias de los proyectos y garantizar la reproducibilidad de los experimentos.  
Ejemplo de construcción y ejecución de la imagen:

```bash
docker build -t pybullet-sim .
docker run -it pybullet-sim
```

Esto permite desplegar un entorno limpio con todas las librerías necesarias y ejecutar los scripts sin conflictos de versiones.

---

## 🧾 5. Conclusiones

- Se logró implementar exitosamente las simulaciones de **Drones**, **Baxter** y **Atlas** usando PyBullet.  
- Docker permitió una **mayor portabilidad y escalabilidad**, haciendo posible correr las simulaciones en diferentes equipos sin reconfiguración.  
- PyBullet demostró ser una herramienta poderosa para el **aprendizaje en robótica**, gracias a su precisión física y compatibilidad con modelos URDF y SDF.  
- La experimentación permitió comprender la **interacción entre controladores, articulaciones y sensores**, base esencial en el diseño de robots reales.

---

## 🔗 Referencias

1. Coumans, E. (2024). *PyBullet Robotics Simulation*. [GitHub Repository](https://github.com/erwincoumans/pybullet_robots)  
2. PyBullet Documentation: [https://pybullet.org/](https://pybullet.org/)  
3. DroneSim: *Gym-PyBullet-Drones* (MIT, 2023) – [https://github.com/utiasDSL/gym-pybullet-drones](https://github.com/utiasDSL/gym-pybullet-drones)  
4. Boston Dynamics (2020). *ATLAS Technical Overview*.  
5. Docker Documentation: [https://docs.docker.com/](https://docs.docker.com/)

---

## 👥 Autores

**Yossed Mauricio Riaño Páez**  
**Miguel Montaña**  
**Jeferson Hernández**  

**Universidad Santo Tomás**  
Facultad de Ingeniería Electrónica  
2025

---
