import glob
import os
import pathlib
import sys

from VehiclePhysicsControlParser import parse_vehicle_physics_control

CARLA_LIB_PATH = "../../carla/dist/carla-*%d.%d-%s.egg"
HOST = "127.0.0.1"
PORT = 2000
OUTPUT_DIR = "./data"

try:
    sys.path.append(
        glob.glob(
            CARLA_LIB_PATH
            % (
                sys.version_info.major,
                sys.version_info.minor,
                "win-amd64" if os.name == "nt" else "linux-x86_64",
            )
        )[0]
    )
except IndexError:
    pass

import carla

client = carla.Client(HOST, PORT)
client.set_timeout(2.0)

world = client.get_world()
map = world.get_map()
spawn_points = world.get_map().get_spawn_points()


vehicle_bps = world.get_blueprint_library().filter("vehicle")

pathlib.Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

for i in range(len(vehicle_bps)):
    vehicle = world.try_spawn_actor(vehicle_bps[i], spawn_points[0])

    physics = vehicle.get_physics_control()
    json_physics = parse_vehicle_physics_control(physics)
    vehicle_model = vehicle.type_id.replace("vehicle.", "").replace(".", "_")

    vehicle.destroy()

    with open(
        f"{os.path.join(OUTPUT_DIR, vehicle_model)}_physics_control.json", "w"
    ) as f:
        f.write(json_physics)
