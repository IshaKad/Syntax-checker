symbol_table = {}

def declare_variable(name):
    if name in symbol_table:
        return False
    symbol_table[name] = "int"
    return True

def is_declared(name):
    return name in symbol_table

def print_table():
    print("\n========== SYMBOL TABLE ==========")

    if not symbol_table:
        print("Empty")
        return

    for variable, datatype in symbol_table.items():
        print(f"{variable} : {datatype}")