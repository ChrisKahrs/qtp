model basic_adder
  Modelica.Blocks.Continuous.Integrator integrator(y(start = realOutput), y_start = 0)  annotation(
    Placement(visible = true, transformation(origin = {54, 4}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.IntegerConstant integerConstant(k = 3)  annotation(
    Placement(visible = true, transformation(origin = {-42, -24}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.MathInteger.Sum sum(nu = 2) annotation(
    Placement(visible = true, transformation(origin = {4, 4}, extent = {{-6, -6}, {6, 6}}, rotation = 0)));
  Modelica.Blocks.Sources.IntegerTable integerTable(startTime = 0, table = [0, 0; 1, 2; 2, 4; 3, 6; 4, 4; 6, 2])  annotation(
    Placement(visible = true, transformation(origin = {-64, 46}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Interfaces.RealOutput realOutput annotation(
    Placement(visible = true, transformation(origin = {88, 46}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {88, 46}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(integerConstant.y, sum.u[1]) annotation(
    Line(points = {{-30, -24}, {-2, -24}, {-2, 4}}, color = {255, 127, 0}));
  connect(sum.y, integrator.u) annotation(
    Line(points = {{10, 4}, {42, 4}}, color = {255, 127, 0}));
  connect(integerTable.y, sum.u[2]) annotation(
    Line(points = {{-52, 46}, {-2, 46}, {-2, 4}}, color = {255, 127, 0}));
  connect(integrator.y, integrator.u) annotation(
    Line(points = {{66, 4}, {82, 4}, {82, -30}, {28, -30}, {28, 4}, {42, 4}}, color = {0, 0, 127}));
  connect(integrator.y, realOutput) annotation(
    Line(points = {{66, 4}, {88, 4}, {88, 46}}, color = {0, 0, 127}));
  annotation(
    uses(Modelica(version = "4.0.0")));
end basic_adder;
