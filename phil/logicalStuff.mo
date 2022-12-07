model logicalStuff
  Modelica.Blocks.Sources.Sine sine(amplitude = 3, f = .1, offset = 0, phase = 0, startTime = 0)  annotation(
    Placement(visible = true, transformation(origin = {-70, 54}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.RealToInteger realToInteger annotation(
    Placement(visible = true, transformation(origin = {-26, 52}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.IntegerStep integerStep(height = 4, offset = 1, startTime = 2)  annotation(
    Placement(visible = true, transformation(origin = {-42, 20}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.MathInteger.Sum sum(nu = 2)  annotation(
    Placement(visible = true, transformation(origin = {36, 42}, extent = {{-6, -6}, {6, 6}}, rotation = 0)));
equation
  connect(sine.y, realToInteger.u) annotation(
    Line(points = {{-58, 54}, {-38, 54}, {-38, 52}}, color = {0, 0, 127}));
  connect(realToInteger.y, sum.u[1]) annotation(
    Line(points = {{-14, 52}, {30, 52}, {30, 42}}, color = {255, 127, 0}));
  connect(integerStep.y, sum.u[2]) annotation(
    Line(points = {{-30, 20}, {30, 20}, {30, 42}}, color = {255, 127, 0}));
  annotation(
    uses(Modelica(version = "4.0.0")));
end logicalStuff;
