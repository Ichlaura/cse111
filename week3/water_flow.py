
#1. Using VS Code, create a new file and save it as water_flow.py
#2. Create another new file, save it as test_water_flow.py
#3. In your water_flow.py program, write a function named water_column_height
def water_column_height(tower_height, tank_height):
 
    return tower_height + (3 * tank_height) / 4

#5. In your water_flow.py program, write a function named pressure_gain_from_water_height
def pressure_gain_from_water_height(height):
   
    density = 998.2  # kg/m³
    gravity = 9.80665  # m/s²
    return (density * gravity * height) / 1000

#7. In your water_flow.py program, write a function named pressure_loss_from_pipe
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    
    density = 998.2  # kg/m³
    numerator = -friction_factor * pipe_length * density * fluid_velocity**2
    denominator = 2000 * pipe_diameter
    return numerator / denominator
       
