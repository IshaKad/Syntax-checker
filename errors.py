syntax_errors = []

def add_error(message):
    syntax_errors.append(message)

def print_errors():
    if syntax_errors:
        print("\n========== SYNTAX ERRORS ==========")
        for error in syntax_errors:
            print(error)
    else:
        print("\nNo syntax errors found.")