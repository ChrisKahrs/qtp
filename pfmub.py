from pythonfmu import Fmi2Causality, Fmi2Slave, Boolean, Integer, Real, String, Fmi2Variability


class Pfmub(Fmi2Slave):

    author = "John Doe"
    description = "A simple description"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.intOut = 1
        self.brealOut = 0.0
        self.booleanVariable = True
        self.stringVariable = "Hello World!"
        self.intIn = 0
        self.brealIn = 0.0
        
        self.badder = 1.0
        
        self.register_variable(Real("badder", causality=Fmi2Causality.parameter, variability=Fmi2Variability.tunable))
        # self.register_variable(Integer("intOut", causality=Fmi2Causality.output))
        # self.register_variable(Integer("intIn", causality=Fmi2Causality.input))
        self.register_variable(Real("brealOut", causality=Fmi2Causality.output))
        self.register_variable(Real("brealIn", causality=Fmi2Causality.input))
        # self.register_variable(Boolean("booleanVariable", causality=Fmi2Causality.local))
        # self.register_variable(String("stringVariable", causality=Fmi2Causality.local))

    def do_step(self, current_time, step_size):
        self.brealOut += (self.brealIn + self.badder)
        return True