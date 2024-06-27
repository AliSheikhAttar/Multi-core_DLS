class CustomExampleDSLCodeGenerator:
    def __init__(self):
        self.non_operands = ['program', 'threadsNumber', 'time', 'codeAddress', 'begin_scope_operator',
                             'end_scope_operator']
        self.operand_stack = []
        self.code_stack = []

    def is_operand(self, item):
        if item in self.non_operands:
            return False
        else:
            return True

    def generate_code(self, post_order_array):
        for item in post_order_array:
            if not self.is_operand(item["label"]):
                self.generate_code_based_on_non_operand(item["label"])
            else:
                self.operand_stack.append(item["label"])

        result = ''
        for code_string in self.code_stack:
            if code_string is not None:
                result += code_string
        return result

    def generate_code_based_on_non_operand(self, item):
        if item == "program":
            self.generate_program()

        # elif item == "threadsNumber":
        #     self.set_output_type()
        #
        # elif item == "time":
        #     self.generate_initiate_game()
        #
        # elif item == "codeAddress":

        #
        # elif item == "begin_scope_operator":
        #     self.generate_begin_scope_operator()
        #
        # elif item == "end_scope_operator":
        #     self.generate_end_scope_operator()



    def generate_program(self):
        y = self.operand_stack.pop()
        # Open the file in read mode
        with open(y, 'r') as file:
            # Read the file line by line
            for line in file:
                # Print each line
                print(line.strip())  # strip() to remove the newline characters
                self.code_stack.append(line)

        # placements_code = self.code_stack.pop()
        # initiate_code = self.code_stack.pop()
        # output_type = 'console'
        # if len(self.code_stack) > 0:
        #     temp_code = self.code_stack.pop()
        #     if temp_code.startswith('##COMPILER_PARAM:::output_type:::'):
        #         output_type = temp_code.replace('##COMPILER_PARAM:::output_type:::', '')
        #     else:
        #         self.code_stack.append(temp_code)
        #
        # if output_type == 'console':
        #     program_code = (initiate_code + placements_code
        #                     + f"\nfor i in range({self.width}):\n" +
        #                     f"\tfor j in ()range({self.height}):\n" +
        #                     "\t\tif bombs[i][j]:\n" +
        #                     "\t\t\tprint('*', end ='')\n" +
        #                     "\t\telif hint and hints[i][j] > 0:\n" +
        #                     "\t\t\tprint(hints[i][j], end ='')\n" +
        #                     "\t\telse:\n" +
        #                     "\t\t\tprint('#', end ='')\n" +
        #                     "\tprint()"
        #                     )
        #     self.code_stack.append(program_code)


    def generate_begin_scope_operator(self):
        self.code_stack.append("##COMPILER_PARAM:::scope:::begin_scope_operator")

    def generate_end_scope_operator(self):
        self.code_stack.append("##COMPILER_PARAM:::scope:::end_scope_operator")
