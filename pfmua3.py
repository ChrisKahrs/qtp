from pythonfmu import Fmi2Causality, Fmi2Slave, Boolean, Integer, Real, String, Fmi2Variability, Fmi2Initial


class Pfmua3(Fmi2Slave):

    author = "Chris Kahrs"
    description = "A FMU simple description"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = 0
        self.intState = 1
        self.arealState = 0.0
        self.booleanVariable = True
        self.stringVariable = "Hello World!"
        self.intAction = 0
        self.arealAction = 0.0

        self.aadder = 1.0
        
        self.register_variable(Real("aadder", causality=Fmi2Causality.parameter, variability=Fmi2Variability.tunable))
        # self.register_variable(Actionteger("intState", causality=Fmi2Causality.input))
        # self.register_variable(Actionteger("intAction", causality=Fmi2Causality.input))
        # self.register_variable(Real("arealState", causality=Fmi2Causality.input,initial=Fmi2Initial.exact))
        self.register_variable(Real("arealState", causality=Fmi2Causality.input))
        self.register_variable(Real("arealAction", causality=Fmi2Causality.input))
        # self.register_variable(Boolean("booleanVariable", causality=Fmi2Causality.local))
        # self.register_variable(String("stringVariable", causality=Fmi2Causality.local))
        print("after register: State", self.arealState)
        print("after register: in", self.arealAction)
        print("after register: aadder", self.aadder)

    def do_step(self, current_time, step_size):
        self.arealState += self.arealAction
        self.counter += 1
        if self.counter == 1:
            self.arealState = self.aadder
        print("Step: ct: ", self.counter, "State: ", self.arealState, "in: ", self.arealAction, "aadder: ", self.aadder)
        print("Step State: ", self.arealState)
        return True