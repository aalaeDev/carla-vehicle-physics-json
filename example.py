import glob
import os
import sys

from VehiclePhysicsControlParser import parse_vehicle_physics_control

CARLA_LIB_PATH = "../../carla/dist/carla-*%d.%d-%s.egg"

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

HOST = "127.0.0.1"
PORT = 2000

client = carla.Client(HOST, PORT)
client.set_timeout(2.0)

world = client.get_world()
map = world.get_map()
spawn_points = world.get_map().get_spawn_points()

vehicle_bps = world.get_blueprint_library().filter("coupe_2020")
vehicle = world.try_spawn_actor(vehicle_bps[0], spawn_points[0])

physics = vehicle.get_physics_control()
json_physics = parse_vehicle_physics_control(physics)
vehicle_model = vehicle.type_id.replace("vehicle.", "").replace(".", "_")

vehicle.destroy()

with open(f"{vehicle_model}_physics_control.json", "w") as f:
    f.write(json_physics)
