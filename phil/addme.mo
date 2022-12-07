model addme
  Modelica.Blocks.Math.Add add(k1 = +0, k2 = +2)  annotation(
    Placement(visible = true, transformation(origin = {30, 0}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Interfaces.RealInput realInM annotation(
    Placement(visible = true, transformation(origin = {-80, 52}, extent = {{-20, -20}, {20, 20}}, rotation = 0), iconTransformation(origin = {-94, 12}, extent = {{-20, -20}, {20, 20}}, rotation = 0)));
  Modelica.Blocks.Interfaces.RealOutput realoutM annotation(
    Placement(visible = true, transformation(origin = {77, 43}, extent = {{-17, -17}, {17, 17}}, rotation = 0), iconTransformation(origin = {94, 16}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.IntegerStep integerStep(height = 3, offset = 1, startTime = 0)  annotation(
    Placement(visible = true, transformation(origin = {-78, -4}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(realInM, add.u1) annotation(
    Line(points = {{-80, 52}, {-44, 52}, {-44, 6}, {18, 6}}, color = {0, 0, 127}));
  connect(add.y, realoutM) annotation(
    Line(points = {{41, 0}, {77, 0}, {77, 43}}, color = {0, 0, 127}));
  connect(integerStep.y, add.u2) annotation(
    Line(points = {{-67, -4}, {-19.5, -4}, {-19.5, -6}, {18, -6}}, color = {255, 127, 0}));
  annotation(
    uses(Modelica(version = "4.0.0")),
    Diagram);
end addme;
