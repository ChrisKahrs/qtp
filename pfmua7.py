from pythonfmu import Fmi2Causality, Fmi2Slave, Boolean, Integer, Real, String, Fmi2Variability, Fmi2Initial


class Pfmua7(Fmi2Slave):

    author = "Chris Kahrs"
    description = "A FMU simple description7"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = 0
        
        self.value = 0.0
        self.addend = 0.0
        self.initial_value = 1.0
        
        self.register_variable(Real("initial_value", causality=Fmi2Causality.parameter, variability=Fmi2Variability.tunable))
        self.register_variable(Real("value", causality=Fmi2Causality.output, initial=Fmi2Initial.exact))
        self.register_variable(Real("addend", causality=Fmi2Causality.input))
        
    def enter_initialization_mode(self):
        print("value before: ", self.value)
        print("initial before: ", self.initial_value)
        self.value = self.initial_value
        print("value after: ", self.value)
        return super().enter_initialization_mode()
        
    def do_step(self, current_time, step_size):
        self.value += self.addend
        self.counter += 1
        print("Step: ", self.counter, "addend: ", self.addend, "value: " , self.value)
        return True