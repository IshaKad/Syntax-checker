class Program:
    def __init__(self, statements):
        self.statements = statements


class Declaration:
    def __init__(self, datatype, identifier):
        self.datatype = datatype
        self.identifier = identifier


class Assignment:
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression


class BinaryOperation:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class Number:
    def __init__(self, value):
        self.value = value


class Variable:
    def __init__(self, name):
        self.name = name