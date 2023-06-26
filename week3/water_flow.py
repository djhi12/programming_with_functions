GRAVITY = 9.80665  # Earth's acceleration of gravity in m/s^2
WATER_DENSITY = 998.2  # Density of water in kg/m^3
WATER_VISCOSITY = 0.0010016  # Dynamic viscosity of water in Pascal seconds

def water_column_height(tower_height, tank_height):
    h = tower_height + 3 * tank_height / 4
    return h

def pressure_gain_from_water_height(height):
    P = WATER_DENSITY * GRAVITY * height / 1000
    return P

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    P = -friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2 / (2000 * pipe_diameter)
    return P

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    P = -0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings / 2000
    return P

def reynolds_number(hydraulic_diameter, fluid_velocity):
    R = WATER_DENSITY * hydraulic_diameter * fluid_velocity / WATER_VISCOSITY
    return R

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    P = -k * WATER_DENSITY * fluid_velocity**2 / 2000
    return P
