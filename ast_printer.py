def print_ast(node, indent=0):

    space = "    " * indent

    if node is None:
        return

    print(space + node.__class__.__name__)

    if hasattr(node, "__dict__"):

        for value in node.__dict__.values():

            if isinstance(value, list):

                for item in value:
                    print_ast(item, indent + 1)

            elif hasattr(value, "__dict__"):

                print_ast(value, indent + 1)

            else:

                print(space + "    " + str(value))