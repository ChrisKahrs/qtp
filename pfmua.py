from pythonfmu import Fmi2Causality, Fmi2Slave, Boolean, Integer, Real, String, Fmi2Variability, Fmi2Initial


class Pfmua(Fmi2Slave):

    author = "Chris Kahrs"
    description = "A FMU simple description"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.intOut = 1
        self.arealOut = 0.0
        self.booleanVariable = True
        self.stringVariable = "Hello World!"
        self.intIn = 0
        self.arealIn = 0.0
        
        self.aadder = 1.0
        
        self.register_variable(Real("aadder", causality=Fmi2Causality.parameter, variability=Fmi2Variability.tunable))
        # self.register_variable(Integer("intOut", causality=Fmi2Causality.output))
        # self.register_variable(Integer("intIn", causality=Fmi2Causality.input))
        self.register_variable(Real("arealOut", causality=Fmi2Causality.output,initial=Fmi2Initial.exact))
        self.register_variable(Real("arealIn", causality=Fmi2Causality.input))
        # self.register_variable(Boolean("booleanVariable", causality=Fmi2Causality.local))
        # self.register_variable(String("stringVariable", causality=Fmi2Causality.local))

    def do_step(self, current_time, step_size):
        self.arealOut += (self.arealIn + self.aadder)
        return True