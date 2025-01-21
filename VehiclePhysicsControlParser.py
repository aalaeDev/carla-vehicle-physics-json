import json


def parse_vector2d(vector):
    return {"x": vector.x, "y": vector.y}


def parse_vector3d(vector):
    return {"x": vector.x, "y": vector.y, "z": vector.z}


def parse_gear_physics_control(gear):
    return {
        "ratio": gear.ratio,
        "down_ratio": gear.down_ratio,
        "up_ratio": gear.up_ratio,
    }


def parse_wheel_physics_control(wheel):
    return {
        "tire_friction": wheel.tire_friction,
        "damping_rate": wheel.damping_rate,
        "max_steer_angle": wheel.max_steer_angle,
        "radius": wheel.radius,
        "max_brake_torque": wheel.max_brake_torque,
        "max_handbrake_torque": wheel.max_handbrake_torque,
        "lat_stiff_max_load": wheel.lat_stiff_max_load,
        "lat_stiff_value": wheel.lat_stiff_value,
        "long_stiff_value": wheel.long_stiff_value,
        "position": parse_vector3d(wheel.position),
    }


def parse_vehicle_physics_control(vehicle):
    # Extracting attributes from the object
    vehicle_data = {
        "torque_curve": [parse_vector2d(v) for v in vehicle.torque_curve],
        "max_rpm": vehicle.max_rpm,
        "moi": vehicle.moi,
        "damping_rate_full_throttle": vehicle.damping_rate_full_throttle,
        "damping_rate_zero_throttle_clutch_engaged": vehicle.damping_rate_zero_throttle_clutch_engaged,
        "damping_rate_zero_throttle_clutch_disengaged": vehicle.damping_rate_zero_throttle_clutch_disengaged,
        "use_gear_autobox": vehicle.use_gear_autobox,
        "gear_switch_time": vehicle.gear_switch_time,
        "clutch_strength": vehicle.clutch_strength,
        "final_ratio": vehicle.final_ratio,
        "forward_gears": [parse_gear_physics_control(g) for g in vehicle.forward_gears],
        "mass": vehicle.mass,
        "drag_coefficient": vehicle.drag_coefficient,
        "center_of_mass": parse_vector3d(vehicle.center_of_mass),
        "steering_curve": [parse_vector2d(v) for v in vehicle.steering_curve],
        "wheels": [parse_wheel_physics_control(w) for w in vehicle.wheels],
        "use_sweep_wheel_collision": vehicle.use_sweep_wheel_collision,
    }

    return json.dumps(vehicle_data, indent=4)
