model addme
  Modelica.Blocks.Math.Add add annotation(
    Placement(visible = true, transformation(origin = {-8, 12}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Interfaces.RealInput realInM annotation(
    Placement(visible = true, transformation(origin = {-94, 12}, extent = {{-20, -20}, {20, 20}}, rotation = 0), iconTransformation(origin = {-94, 12}, extent = {{-20, -20}, {20, 20}}, rotation = 0)));
  Modelica.Blocks.Sources.Constant adderM(k = 2)  annotation(
    Placement(visible = true, transformation(origin = {-54, -40}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(adderM.y, add.u2) annotation(
    Line(points = {{-42, -40}, {-20, -40}, {-20, 6}}, color = {0, 0, 127}));
  connect(realInM, add.u1) annotation(
    Line(points = {{-94, 12}, {-20, 12}, {-20, 18}}, color = {0, 0, 127}));
  annotation(
    uses(Modelica(version = "4.0.0")));
end addme;
