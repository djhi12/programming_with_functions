def water_column_height(tower_height, tank_height):
    h = tower_height + 3 * tank_height / 4
    return h

def pressure_gain_from_water_height(height):
    p = 998.2  # density of water in kg/m^3
    g = 9.80665  # acceleration due to gravity in m/s^2
    P = p * g * height / 1000
    return P

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    p = 998.2  # density of water in kg/m^3
    P = -friction_factor * pipe_length * p * fluid_velocity ** 2 / (2000 * pipe_diameter)
    return P
