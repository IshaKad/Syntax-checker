from parser import parser
from ast_printer import print_ast
from errors import print_errors
from symbol_table import print_table

with open("sample.c") as file:
    code = file.read()

tree = parser.parse(code)

print_errors()

print_table()

print("\n========== ABSTRACT SYNTAX TREE ==========\n")

if tree:
    print_ast(tree)