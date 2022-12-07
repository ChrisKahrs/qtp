model ExampleFMUA
  Modelica.Blocks.Interfaces.RealInput u annotation(
    Placement(visible = true, transformation(origin = {-102, 4}, extent = {{-20, -20}, {20, 20}}, rotation = 0), iconTransformation(origin = {-102, 4}, extent = {{-20, -20}, {20, 20}}, rotation = 0)));
  Modelica.Blocks.Interfaces.RealOutput y annotation(
    Placement(visible = true, transformation(origin = {102, -2}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {102, -2}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Continuous.Integrator integrator annotation(
    Placement(visible = true, transformation(origin = {-56, 72}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
y = u^3;
annotation(
    uses(Modelica(version = "4.0.0")));
end ExampleFMUA;
