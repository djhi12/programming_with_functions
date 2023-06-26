import pytest
from water_flow import (
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction
)

def test_water_column_height():
    tower_height = 10.0
    tank_height = 5.0
    expected_height = 15.75
    assert water_column_height(tower_height, tank_height) == pytest.approx(expected_height, 0.01)

    tower_height = 15.0
    tank_height = 8.0
    expected_height = 19.0
    assert water_column_height(tower_height, tank_height) == pytest.approx(expected_height, 0.01)

def test_pressure_gain_from_water_height():
    height = 20.0
    expected_pressure = 196.08  # kilopascals
    assert pressure_gain_from_water_height(height) == pytest.approx(expected_pressure, 0.01)

    height = 25.0
    expected_pressure = 245.10  # kilopascals
    assert pressure_gain_from_water_height(height) == pytest.approx(expected_pressure, 0.01)

def test_pressure_loss_from_pipe():
    pipe_diameter = 0.2
    pipe_length = 50.0
    friction_factor = 0.02
    fluid_velocity = 1.5
    expected_pressure_loss = -0.3075  # kilopascals
    assert pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity) == pytest.approx(expected_pressure_loss, 0.001)

    pipe_diameter = 0.3
    pipe_length = 40.0
    friction_factor = 0.015
    fluid_velocity = 2.0
    expected_pressure_loss = -0.432  # kilopascals
    assert pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity) == pytest.approx(expected_pressure_loss, 0.001)

def test_pressure_loss_from_fittings():
    fluid_velocity = 1.5
    quantity_fittings = 3
    expected_pressure_loss = -0.045  # kilopascals
    assert pressure_loss_from_fittings(fluid_velocity, quantity_fittings) == pytest.approx(expected_pressure_loss, 0.001)

    fluid_velocity = 2.0
    quantity_fittings = 4
    expected_pressure_loss = -0.1067  # kilopascals
    assert pressure_loss_from_fittings(fluid_velocity, quantity_fittings) == pytest.approx(expected_pressure_loss, 0.001)

def test_reynolds_number():
    hydraulic_diameter = 0.2
    fluid_velocity = 1.5
    expected_reynolds_number = 249833.33
    assert reynolds_number(hydraulic_diameter, fluid_velocity) == pytest.approx(expected_reynolds_number, 0.01)

    hydraulic_diameter = 0.3
    fluid_velocity = 2.0
    expected_reynolds_number = 499666.67
    assert reynolds_number(hydraulic_diameter, fluid_velocity) == pytest.approx(expected_reynolds_number, 0.01)

def test_pressure_loss_from_pipe_reduction():
    larger_diameter = 0.2
    fluid_velocity = 1.5
    reynolds_number = 100000
    smaller_diameter = 0.1
    expected_pressure_loss = -3.744  # kilopascals
    assert pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter) == pytest.approx(expected_pressure_loss, 0.001)

    larger_diameter = 0.3
    fluid_velocity = 2.0
    reynolds_number = 200000
    smaller_diameter = 0.2
    expected_pressure_loss = -4.85  # kilopascals
    assert pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter) == pytest.approx(expected_pressure_loss, 0.001)
