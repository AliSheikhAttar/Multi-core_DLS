class CustomExampleDSLCodeGenerator:
    def __init__(self):
        self.non_operands = ['program', 'initiate_game',
                             'bomb_location', 'output', 'hint',
                             'bomb_placements', 'begin_scope_operator',
                             'end_scope_operator']
        self.operand_stack = []
        self.code_stack = []
        self.hint = False
        self.width = 0
        self.height = 0

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

        elif item == "output":
            self.set_output_type()

        elif item == "initiate_game":
            self.generate_initiate_game()

        elif item == "bomb_location":
            self.generate_bomb()

        elif item == "bomb_placements":
            self.generate_bomb_placements()

        elif item == "begin_scope_operator":
            self.generate_begin_scope_operator()

        elif item == "end_scope_operator":
            self.generate_end_scope_operator()

        elif item == "hint":
            self.set_hint()


    def generate_program(self):
        placements_code = self.code_stack.pop()
        initiate_code = self.code_stack.pop()
        output_type = 'console'
        if len(self.code_stack) > 0:
            temp_code = self.code_stack.pop()
            if temp_code.startswith('##COMPILER_PARAM:::output_type:::'):
                output_type = temp_code.replace('##COMPILER_PARAM:::output_type:::', '')
            else:
                self.code_stack.append(temp_code)

        if output_type == 'console':
            program_code = (initiate_code + placements_code
                            + f"\nfor i in range({self.width}):\n" +
                            f"\tfor j in ()range({self.height}):\n" +
                            "\t\tif bombs[i][j]:\n" +
                            "\t\t\tprint('*', end ='')\n" +
                            "\t\telif hint and hints[i][j] > 0:\n" +
                            "\t\t\tprint(hints[i][j], end ='')\n" +
                            "\t\telse:\n" +
                            "\t\t\tprint('#', end ='')\n" +
                            "\tprint()"
                            )
            self.code_stack.append(program_code)

    def generate_initiate_game(self):
        self.height = int(self.operand_stack.pop())
        self.width = int(self.operand_stack.pop())
        code_string = f"bombs = [[False for y in range({self.height})] for x in range({self.width})]\n"
        self.code_stack.append(code_string)
        if self.hint:
            hint_string = "hint = True\n"
            self.code_stack.append(hint_string)
            hints = f"hints = [[0 for _ in range({self.height})] for __ in range({self.width})]\n"
            self.code_stack.append(hints)
            hint_function = "\ndef hint_func(x, y):\n"
            self.code_stack.append(hint_function)
            hint_function = f"\tif {self.width} > x - 1 >= {0} and {self.height} > y - 1 >= {0}:\n"
            self.code_stack.append(hint_function)
            hint_function = "\t\thints[x - 1][y - 1] += 1\n"
            self.code_stack.append(hint_function)
            hint_function = f"\tif {self.width} > x - 1 >= {0} and {self.height} > y >= {0}:\n"
            self.code_stack.append(hint_function)
            hint_function = "\t\thints[x - 1][y] += 1\n"
            self.code_stack.append(hint_function)
            hint_function = f"\tif {self.width} > x - 1 >= {0} and {self.height} > y + 1>= {0}:\n"
            self.code_stack.append(hint_function)
            hint_function = "\t\thints[x - 1][y + 1] += 1\n"
            self.code_stack.append(hint_function)
            hint_function = f"\tif {self.width} > x >= {0} and {self.height} > y + 1 >= {0}:\n"
            self.code_stack.append(hint_function)
            hint_function = "\t\thints[x][y + 1] += 1\n"
            self.code_stack.append(hint_function)
            hint_function = f"\tif {self.width} > x + 1 >= {0} and {self.height} > y + 1 >= {0}:\n"
            self.code_stack.append(hint_function)
            hint_function = "\t\thints[x + 1][y + 1] += 1\n"
            self.code_stack.append(hint_function)
            hint_function = f"\tif {self.width} > x + 1 >= {0} and {self.height} > y >= {0}:\n"
            self.code_stack.append(hint_function)
            hint_function = "\t\thints[x + 1][y] += 1\n"
            self.code_stack.append(hint_function)
            hint_function = f"\tif {self.width} > x + 1 >= {0} and {self.height} > y - 1 >= {0}:\n"
            self.code_stack.append(hint_function)
            hint_function = "\t\thints[x + 1][y - 1] += 1\n"
            self.code_stack.append(hint_function)
            hint_function = f"\tif {self.width} > x >= {0} and {self.height} > y - 1 >= {0}:\n"
            self.code_stack.append(hint_function)
            hint_function = "\t\thints[x][y - 1] += 1\n\n\n"
            self.code_stack.append(hint_function)

        else:
            hint_string = "hint = False\n"
            self.code_stack.append(hint_string)
            hints = "hints = []\n"
            self.code_stack.append(hints)
    def generate_bomb(self):
        y = int(self.operand_stack.pop())
        x = int(self.operand_stack.pop())
        code_string = f"bombs[{x - 1}][{y - 1}] = True\n"
        self.code_stack.append(code_string)
        if self.hint:
            call_hint_function = f"hint_func({x - 1}, {y - 1})\n\n"
            self.code_stack.append(call_hint_function)
    def set_output_type(self):
        self.code_stack.append(f"##COMPILER_PARAM:::output_type:::{self.operand_stack.pop()}\n")

    def generate_bomb_placements(self):
        temp_block_stack = []
        current_code = self.code_stack.pop()
        if current_code != '##COMPILER_PARAM:::scope:::end_scope_operator':
            self.code_stack.append(current_code)
            return
        while current_code != '##COMPILER_PARAM:::scope:::begin_scope_operator':
            current_code = self.code_stack.pop()
            temp_block_stack.append(current_code)
        temp_block_stack.pop()
        result = ''
        while len(temp_block_stack) != 0:
            result = result + temp_block_stack.pop()
        self.code_stack.append(result)

    def set_hint(self):
        flag = self.operand_stack.pop()
        if flag == 'True':
            self.hint = True

    def generate_begin_scope_operator(self):
        self.code_stack.append("##COMPILER_PARAM:::scope:::begin_scope_operator")

    def generate_end_scope_operator(self):
        self.code_stack.append("##COMPILER_PARAM:::scope:::end_scope_operator")
