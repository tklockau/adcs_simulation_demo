from simulation.satellite.satellite import move_2b, SatelliteState, ReactionWheel
from simulation.utils.quantities import Vector, Time, AngularVelocity
from simulation.simulate import simulate
from simulation.plot.plot import plot, Graph

# Set satellite parameters to a preset
satellite = move_2b

# Construct time variable values
time = Vector[Time].linear(0, 60)
reaction_wheel_rotation: Vector[AngularVelocity] = - 1/120 * (time ** 2)

# Execute the simulation
simulated_satellite = simulate(satellite, reaction_wheel_rotation, time)

# Construct the graphs
satellite_graph = Graph.from_satellites(
    "Satellite",
    satellites=simulated_satellite,
    plot_method=SatelliteState.angular_velocity
)
reaction_wheel_graph = Graph.from_satellites(
    "Reaction Wheel",
    satellites=simulated_satellite,
    plot_method=ReactionWheel.angular_velocity
)

# Plot the graphs
plot(
    x_values=time,
    graphs=[satellite_graph, reaction_wheel_graph],
    x_label="time in s",
    y_label="angular velocity in rad/s",
    title="Comparison between satellite and reaction wheel angular velocity"
)