from pythonfmu import Fmi2Causality, Fmi2Slave, Boolean, Integer, Real, String, Fmi2Variability, Fmi2Initial


class Pfmua4(Fmi2Slave):

    author = "Chris Kahrs"
    description = "A FMU simple description4"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = 0
        # self.intState = 1
        # self.booleanVariable = True
        # self.stringVariable = "Hello World!"
        # self.intAction = 0
        self.value = 0.0
        self.addend = 0.0
        self.initial_value = 1.0
        
        self.register_variable(Real("initial_value", causality=Fmi2Causality.parameter, variability=Fmi2Variability.tunable))
        self.register_variable(Real("value", causality=Fmi2Causality.output))
        self.register_variable(Real("addend", causality=Fmi2Causality.input))
        
        # self.register_variable(Actionteger("intState", causality=Fmi2Causality.input))
        # self.register_variable(Actionteger("intAction", causality=Fmi2Causality.input))
        # self.register_variable(Real("arealState", causality=Fmi2Causality.input,initial=Fmi2Initial.exact))
        # self.register_variable(Boolean("booleanVariable", causality=Fmi2Causality.local))
        # self.register_variable(String("stringVariable", causality=Fmi2Causality.local))
        
        print("after register: value", self.value)
        print("after register: initial_value", self.initial_value)
        print("after register: addend", self.addend)

    def do_step(self, current_time, step_size):
        self.counter += 1
        if self.counter == 1:
            self.value = self.addend
        self.value += self.addend

        print("Step: ct: ", self.counter, "value: ", self.value, "addend: ", self.addend, "IV: ", self.initial_value)
        return True