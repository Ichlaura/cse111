
#2.Create another new file, save it as test_water_flow.py, and copy and paste the following import statements into the file.
from pytest import approx
import pytest

from water_flow import (water_column_height, 
                       pressure_gain_from_water_height,
                       pressure_loss_from_pipe)

#4. In your test_water_flow.py file, write a test function named test_water_column_height.
def test_water_column_height():
    """Test water_column_height function with various inputs"""
    assert water_column_height(0.0, 0.0) == approx(0.0)
    assert water_column_height(0.0, 10.0) == approx(7.5)
    assert water_column_height(25.0, 0.0) == approx(25.0)
    assert water_column_height(48.3, 12.8) == approx(57.9)
#6. In your test_water_flow.py file, write a test function named test_pressure_gain_from_water_height.
def test_pressure_gain_from_water_height():
    """Test pressure_gain_from_water_height function with various inputs"""
    assert pressure_gain_from_water_height(0.0) == approx(0.0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)
#8. In your test_water_flow.py file, write a test function named test_pressure_loss_from_pipe 
def test_pressure_loss_from_pipe():
    """Test pressure_loss_from_pipe function with various inputs"""
    # Test cases with zero values
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs=0.001)
    
    # Test cases with normal values
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)


#9. Copy and paste the following code at the bottom of your test_water_flow.py file.
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])