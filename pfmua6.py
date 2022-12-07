from pythonfmu import Fmi2Causality, Fmi2Slave, Boolean, Integer, Real, String, Fmi2Variability, Fmi2Initial


class Pfmua6(Fmi2Slave):

    author = "Chris Kahrs"
    description = "A FMU simple description6"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = 0
        
        self.value = 0.0
        self.addend = 0.0
        self.initial_value = 1.0
        
        self.register_variable(Real("initial_value", causality=Fmi2Causality.parameter, variability=Fmi2Variability.tunable))
        self.register_variable(Real("value", causality=Fmi2Causality.output, initial=Fmi2Initial.exact))
        self.register_variable(Real("addend", causality=Fmi2Causality.input))
        
    def do_step(self, current_time, step_size):
        self.counter += 1
        print("added: ", self.addend)
        if self.counter == 1:
            print("value before: ", self.value)
            print("initial value: ", self.initial_value)
            self.value = self.initial_value
            print("value before: ", self.value)
        self.value += self.addend

        print("Step: ct: ", self.counter, "value: " , self.value)
        return True