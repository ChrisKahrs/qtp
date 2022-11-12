from pythonfmu import Fmi2Causality, Fmi2Slave, Boolean, Integer, Real, String


class PythonSlave(Fmi2Slave):

    author = "John Doe"
    description = "A simple description"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.intOut = 1
        self.realOut = 3.0
        self.booleanVariable = True
        self.stringVariable = "Hello World!"
        self.intIn = 0
        self.realIn = 0.0
        # self.register_variable(Integer("intOut", causality=Fmi2Causality.output))
        # self.register_variable(Integer("intIn", causality=Fmi2Causality.input))
        self.register_variable(Real("realOut", causality=Fmi2Causality.output))
        self.register_variable(Real("realIn", causality=Fmi2Causality.input))
        # self.register_variable(Boolean("booleanVariable", causality=Fmi2Causality.local))
        # self.register_variable(String("stringVariable", causality=Fmi2Causality.local))

    def do_step(self, current_time, step_size):
        self.realOut += (self.realIn + 1.0)
        return True