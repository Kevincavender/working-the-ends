class EquationCollection:
    def __init__(self):
        self.equations = {
            1: {'equation': 'x=1',"variables": 'X','solved': False, "line_number": 2},
            2: {'equation': 'y=2',"variables": 'Y','solved': False, "line_number": 4}
        }
        self.variables = {
            1: {'variable_name': 'x', 'equations': 'x=1', 'value': 1.0, 'initial_value': 1.0}
        }
        self.number_of_equations = 0
        self.number_of_variables = 0
        self.variable_list = []
        self.equation_list = []

    def update_from_equations(self):
        pass

    def add_equation_to_dictionary(self, equation_string, line_number=0):
        pass

    def parse_line(self, line_string):
        pass

    def is_equation(self):
        pass

    def number_of_equations(self):
        return self.number_of_equations

    def number_of_variables(self):
        return self.number_of_variables

    def variable_list(self):
        return self.variable_list

    def equation_list(self):
        return self.equation_list


equations = {1: {'equation':'X=1',"variables": 'X','solved': False},
             3: {'equation':'Y=2',"variables": 'Y','solved': False}}

print(equations)
print(equations[1])
print("length equations: " + str(len(equations)))
for i in equations:
    exec(equations[i]['equation']) #execute equation
    tn = equations[i]['variables']
    exec('print(' + str(tn) + ')')