import re
class CustomExampleDSLCodeGenerator:
    def __init__(self):
        self.non_operands = [ 'program', 'threadsNumber', 'threadST', 'time', 'code',
        'forLoop', 'variable', 'iterable', 'range', 'threads_no',
        'bool', 'otherCode', 'from', 'to']
        self.operand_stack = []
        self.code_stack = []
        self.thread_no = 2
        self.showTime = False
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
        if item == "threadsNumber":
            self.generate_threadsNumber()
        if item == "threadST":
            self.generate_threadST()
        if item == "time":
            self.generate_time()
        if item == "code":
            self.generate_Mcode()
        if item == "forLoop":
            self.generate_forLoop()
        if item == "variable":
            self.generate_variable()
        if item == "iterable":
            self.generate_iterable()
        if item == "range":
            self.generate_range()
        if item == "threads_no":
            self.generate_threads_no()
        if item == "bool":
            self.generate_bool()
        if item == "otherCode":
            self.generate_otherCode()
        if item == "from":
            self.generate_from()
        if item == "to":
            self.generate_to()

    def generate_program(self):
        self.code_stack.append("import threading\n")
        self.thread_no = 2
        address = self.operand_stack.pop()
        deflist = []
        with open(address, 'r') as file:
            lines = file.readlines()

            for i in range(len(lines)):
                if re.search(r'\bfor\b', lines[i]):
                    forline = i
                    for j in range(i - 1, -1, -1):
                        function_match = re.match(r'\s*def\s+(\w+)\s*\(', lines[j])
                        if function_match:
                            functionline = j
                            range_sp = (lines[j].split('(')[1]).split(',')
                            print(1)
                            start = (range_sp[0])
                            end = (range_sp[1].split(')'))[0]
                            function_name = function_match.group(1)
                            code_to_add = ""
                            for t in range(self.thread_no):
                                code_to_add += f"sep = {end} - {start} + 1\n"
                                code_to_add += f"thread{t} = threading.Thread(target={function_name}, args=({t}*(sep/{self.thread_no}), {t + 1}*(sep/{self.thread_no})))\n"
                            for s in range(self.thread_no):
                                code_to_add += f"thread{s}.start()\n"
                            for jo in range(self.thread_no):print(1)
                                code_to_add += f"thread{jo}.join()\n"
        print(0)



        # for line in lines:
        #     if line.startswith('def'):
        #         defname = (((line.split())[1]).split('('))[0]
        #         deflist.append(defname)
        # func_name
        # # Open the file in read mode
        # with open(y, 'r') as file:
        #     # Read the file line by line
        #     for i in range(len(file)):
        #         if 'def' in file[i]:
        #             func_name = find(def_name)
        #         if 'for' in file[i]:
        #             if func_name != '' and func_name in line[i+1]:
        #                 if(thread_num == 0):
        #                     string = """
        #                                 thread.joing({func_name})
        #                                 """
        #                     append(code_stack)
        #                     """
        #                     thread.wait({func_name})
        #                     """
        #                     append(code_stack)
        #
        #         append(code_stack)
        # print(y)
        # print(x)
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

    def generate_threadsNumber(self):
        pass
    def generate_threadST(self):
        pass
    def generate_time(self):
        pass
    def generate_forLoop(self):
        pass
    def generate_Mcode(self):
        pass
    def generate_variable(self):
        pass
    def generate_iterable(self):
        pass
    def generate_range(self):
        pass
    def generate_from(self):
        pass
    def generate_otherCode(self):
        pass
    def generate_bool(self):
        self.showTime = self.operand_stack.pop()
    def generate_threads_no(self):
        self.thread_no =int(self.operand_stack.pop())
    def generate_to(self):
        pass

    def generate_begin_scope_operator(self):
        self.code_stack.append("##COMPILER_PARAM:::scope:::begin_scope_operator")

    def generate_end_scope_operator(self):
        self.code_stack.append("##COMPILER_PARAM:::scope:::end_scope_operator")
