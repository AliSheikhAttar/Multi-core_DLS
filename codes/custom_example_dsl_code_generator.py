import re
class CustomExampleDSLCodeGenerator:
    def __init__(self):
        self.non_operands = [ 'program', 'threadsNumber', 'threadST', 'time', 'code',
        'forLoop', 'variable', 'iterable', 'range', 'threads_no',
        'bool', 'otherCode', 'from', 'to']
        self.operand_stack = []
        self.code_stack = []
        self.time = False
        self.thread_no = 2
        self.showTime = False
        self.case = 0
        self.file_address = ""
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
        if item == "time":
            self.generate_time()

    def generate_program(self):
        self.code_stack.append("import threading\n")
        if self.time:
            self.code_stack.append("import timeit\n")
        self.code_stack.append("threads = []\n")
        self.code_stack.append(f"threads_num = {self.thread_no}\n")

        self.file_address = self.operand_stack.pop()

        self.determine_case()

        match self.case:
            case 0:
                self.handle_case_0()
            case 1:
                self.handle_case_1()
            case 2:
                handle_case_2()
            case default:
                print("not supported for this version!")




    def determine_case(self):
        with open(self.file_address, 'r') as file:
            lines = file.readlines()
            for line in lines:
                function_match = re.match(r'\s*def\s+(\w+)\s*\(', line)
                if function_match:
                    self.case = 10
                    break

        if self.case == 10:
            with open(self.file_address, 'r') as file:
                lines = file.readlines()

                for line in lines:
                    stripped_line = line.lstrip()
                    # Check if the line starts with 'for' and is not preceded by any tabs or spaces
                    if stripped_line.startswith('for') and line.startswith('for'):
                        self.case = 1
                        break

                if self.case != 1:
                    self.case = 0
        else:
            self.case = 0

    def handle_case_0(self):
        function_name = ""
        with open(self.file_address, 'r') as file:
            lines = file.readlines()
            for line in lines:
                function_match = re.match(r'\s*def\s+(\w+)\s*\(', line)
                if function_match:
                    function_sec = line.split(" ")[1]
                    function_name = function_sec.split("(")[0]
                    break
        with open(self.file_address, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if not(line.startswith("def")) and line.__contains__(function_name):
                    arguments = line.split(")")[0].split("(")[1].split(",")
                    self.code_stack.append(f"end = {arguments[1]}\n")
                    self.code_stack.append(f"start = {arguments[0]}\n")
                    self.code_stack.append(f"step = {int((int(arguments[1]) - int(arguments[0]))/self.thread_no)}\n")
                    if self.time:
                        self.code_stack.append(f"""
start_time = timeit.timeit()

for i in range(start, end, step):
    thread = threading.Thread(target={function_name}, args=(i, i+step))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = timeit.timeit()
print(f"elapsed time : { '{' + 'end_time' + ' - ' + 'start_time' + '}'}")
                        """)
                    else:
                        self.code_stack.append(
                            f"""
for i in range(start, end, step):
    thread = threading.Thread(target={function_name}, args=(i, i+step))
    threads.append(thread)
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
""")
                else:
                    self.code_stack.append(line)


    def handle_case_1(self):
        with open(self.file_address, 'r') as file:
            lines = file.readlines()
            skip = False
            for i in range(len(lines)):
                if lines[i].startswith("for"):
                    if self.time:
                        self.code_stack.append("start_time = timeit.timeit()\n\n")
                    self.code_stack.append(lines[i])
                    function_name = lines[i+1].split("(")[0]
                    args = lines[i+1].split(function_name)[1]
                    self.code_stack.append(f"""                    
    thread = threading.Thread(target={function_name.lstrip()}, args={" ".join(args.rsplit())})
    threads.append(thread)
    
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()""")
                    if self.time:
                        self.code_stack.append(f"""

end_time = timeit.timeit()
print(f"elapsed time : { '{' + 'end_time' + ' - ' + 'start_time' + '}'}")
        """)
                    skip = True
                else:
                    if skip:
                        skip = False
                        continue
                    self.code_stack.append(lines[i])

    def generate_threadsNumber(self):
        self.thread_no = int(self.operand_stack.pop())

    def generate_time(self):
        operand = self.operand_stack.pop()
        self.time = True if operand == 'true' else False
    def generate_begin_scope_operator(self):
        self.code_stack.append("##COMPILER_PARAM:::scope:::begin_scope_operator")

    def generate_end_scope_operator(self):
        self.code_stack.append("##COMPILER_PARAM:::scope:::end_scope_operator")
