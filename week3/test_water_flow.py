from pytest import approx
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe

def test_water_column_height():
    assert water_column_height(0, 0) == approx(0)
    assert water_column_height(0, 10) == approx(7.5)
    assert water_column_height(25, 0) == approx(25)
    assert water_column_height(48.3, 12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0)
    assert pressure_gain_from_water_height(10) == approx(98.82)
    assert pressure_gain_from_water_height(25) == approx(245.55)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.1, 100, 0.02, 2) == approx(-2.495)
    assert pressure_loss_from_pipe(0.2, 50, 0.01, 1) == approx(-0.249)
    assert pressure_loss_from_pipe(0.3, 200, 0.03, 3) == approx(-13.365)
    assert pressure_loss_from_pipe(0.4, 150, 0.02, 2.5) == approx(-22.372)
    assert pressure_loss_from_pipe(0.5, 100, 0.02, 1.5) == approx(-3.328)
    assert pressure_loss_from_pipe(0.6, 50, 0.01, 1.2) == approx(-0.065)
    assert pressure_loss_from_pipe(0.7, 200, 0.03, 2.8) == approx(-22.620)
