from gym_pybullet_drones.envs import CtrlAviary
from gym_pybullet_drones.utils.enums import DroneModel, Physics
import pybullet as p
import numpy as np
import time

if __name__ == "__main__":
    # Crear entorno con varios drones
    env = CtrlAviary(
        drone_model=DroneModel.CF2X,
        num_drones=9,                         # número de drones
        neighbourhood_radius=10,
        physics=Physics.PYB,
        gui=True,                             # Muestra la ventana 3D
        record=False
    )

    print("🚁 Simulación iniciada con múltiples drones... (Ctrl + C para salir)")
    time.sleep(1)

    obs = env.reset()                         # Reinicia el entorno
    action = np.zeros((env.NUM_DRONES, 4))    # Inicializa acción en 0 (sin control activo)

    # Simulación de 10 segundos
    for i in range(10 * env.PYB_FREQ):
        env.step(action)
        if i % env.PYB_FREQ == 0:
            print(f"⏱️ Tiempo simulado: {i/env.PYB_FREQ:.1f} s")
        time.sleep(1/env.PYB_FREQ)            # Mantiene ritmo de simulación real

    env.close()
    print("✅ Simulación finalizada")
