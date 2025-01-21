# Carla Utility: Vehicle Physics Control in JSON format

This repository has the vehicle physics control for [all the vehicles in the latest Carla release](https://carla.readthedocs.io/en/latest/catalogue_vehicles/) in json format, which can be useful for research, developing custom models...

## How to use?

### Use Pre-Generated data files

You can simply access the data that corresponds to the vehicle you are using in `./data`.

### Re-Generate the data files

It is possible to regenerate the vehicle physics control for all the vehicles that are currently available in you Carla server by running `python generate_all.py`. Or for a single vehicle vehicle by following `example.py`.

## About Carla Vehicle Physics Control

More details can be found in [this page](https://carla.readthedocs.io/en/latest/python_api/#carlavehiclephysicscontrol).

### Vehicle Physics Control

| **Property**                                   | **Units** | **Type**                          | **Description**                                                                                                                                                                                                                                                                |
| ---------------------------------------------- | --------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `torque_curve`                                 | N·m       | `list(carla.Vector2D)`            | Curve that indicates the torque measured in Nm for a specific RPM of the vehicle's engine.                                                                                                                                                                                     |
| `max_rpm`                                      | RPM       | `float`                           | The maximum RPM of the vehicle's engine.                                                                                                                                                                                                                                       |
| `moi`                                          | kg·m²     | `float`                           | The moment of inertia of the vehicle's engine.                                                                                                                                                                                                                                 |
| `damping_rate_full_throttle`                   | -         | `float`                           | Damping ratio when the throttle is maximum.                                                                                                                                                                                                                                    |
| `damping_rate_zero_throttle_clutch_engaged`    | -         | `float`                           | Damping ratio when the throttle is zero with clutch engaged.                                                                                                                                                                                                                   |
| `damping_rate_zero_throttle_clutch_disengaged` | -         | `float`                           | Damping ratio when the throttle is zero with clutch disengaged.                                                                                                                                                                                                                |
| `use_gear_autobox`                             | -         | `bool`                            | If True, the vehicle will have an automatic transmission.                                                                                                                                                                                                                      |
| `gear_switch_time`                             | s         | `float`                           | Switching time between gears.                                                                                                                                                                                                                                                  |
| `clutch_strength`                              | kg·m²/s   | `float`                           | Clutch strength of the vehicle.                                                                                                                                                                                                                                                |
| `final_ratio`                                  | -         | `float`                           | Fixed ratio from transmission to wheels.                                                                                                                                                                                                                                       |
| `forward_gears`                                | -         | `list(carla.GearPhysicsControl)`  | List of objects defining the vehicle's gears.                                                                                                                                                                                                                                  |
| `mass`                                         | kg        | `float`                           | Mass of the vehicle.                                                                                                                                                                                                                                                           |
| `drag_coefficient`                             | -         | `float`                           | Drag coefficient of the vehicle's chassis.                                                                                                                                                                                                                                     |
| `center_of_mass`                               | m         | `carla.Vector3D`                  | Center of mass of the vehicle.                                                                                                                                                                                                                                                 |
| `steering_curve`                               | -         | `list(carla.Vector2D)`            | Curve that indicates the maximum steering for a specific forward speed.                                                                                                                                                                                                        |
| `use_sweep_wheel_collision`                    | -         | `bool`                            | Enable the use of sweep for wheel collision. By default, it is disabled and it uses a simple raycast from the axis to the floor for each wheel. Provides a better collision model.                                                                                             |
| `wheels`                                       | -         | `list(carla.WheelPhysicsControl)` | List of wheel physics objects. This list should have 4 elements, where index 0 corresponds to the front left wheel, index 1 to the front right wheel, 2 to the back left, and 3 to the back right. For 2-wheeled vehicles, set the same values for both front and back wheels. |

### Vector 2D

| **Property** | **Units** | **Type** | **Description** |
| ------------ | --------- | -------- | --------------- |
| `x`          | -         | `float`  | X-axis value.   |
| `y`          | -         | `float`  | Y-axis value.   |

### Vector 3D

| **Property** | **Units** | **Type** | **Description** |
| ------------ | --------- | -------- | --------------- |
| `x`          | -         | `float`  | X-axis value.   |
| `y`          | -         | `float`  | Y-axis value.   |
| `z`          | -         | `float`  | Z-axis value.   |

### Gear Physics Control

| **Property** | **Units** | **Type** | **Description**                                                                          |
| ------------ | --------- | -------- | ---------------------------------------------------------------------------------------- |
| `ratio`      | -         | `float`  | The transmission ratio of the gear.                                                      |
| `down_ratio` | -         | `float`  | Quotient between current RPM and MaxRPM where the autonomous gear box should shift down. |
| `up_ratio`   | -         | `float`  | Quotient between current RPM and MaxRPM where the autonomous gear box should shift up.   |

### Wheel Physics Control

| **Property**           | **Units**     | **Type**         | **Description**                                                                                                                |
| ---------------------- | ------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `tire_friction`        | -             | `float`          | A scalar value that indicates the friction of the wheel.                                                                       |
| `damping_rate`         | -             | `float`          | Damping rate of the wheel.                                                                                                     |
| `max_steer_angle`      | degrees       | `float`          | Maximum angle that the wheel can steer.                                                                                        |
| `radius`               | cm            | `float`          | Radius of the wheel.                                                                                                           |
| `max_brake_torque`     | N·m           | `float`          | Maximum brake torque.                                                                                                          |
| `max_handbrake_torque` | N·m           | `float`          | Maximum handbrake torque.                                                                                                      |
| `position`             | m             | `carla.Vector3D` | World position of the wheel. This is a read-only parameter.                                                                    |
| `long_stiff_value`     | kg per radian | `float`          | Tire longitudinal stiffness per unit gravitational acceleration. Each vehicle has a custom value.                              |
| `lat_stiff_max_load`   | -             | `float`          | Maximum normalized tire load at which the tire can deliver no more lateral stiffness no matter how much extra load is applied. |
| `lat_stiff_value`      | -             | `float`          | Maximum stiffness per unit of lateral slip. Each vehicle has a custom value.                                                   |
