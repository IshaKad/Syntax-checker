from ast_nodes import Assignment, BinaryOperation, Declaration, Number, Program, Variable
import ply.yacc as yacc

from lexer import tokens
from errors import add_error
from symbol_table import declare_variable, is_declared
from ast_nodes import *

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_program(p):
    '''
    program : statements
    '''
    p[0] = Program(p[1])

def p_statements_multiple(p):
    '''
    statements : statements statement
    '''
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    '''
    statements : statement
    '''
    p[0] = [p[1]]

def p_statement(p):
    '''
    statement : declaration
              | assignment
    '''
    p[0] = p[1]

def p_declaration(p):
    '''
    declaration : INT ID SEMICOLON
    '''

    if declare_variable(p[2]):
        p[0] = Declaration("int", p[2])

    else:
        add_error(
            f"Line {p.lineno(2)}: Variable '{p[2]}' already declared."
        )
        p[0] = Declaration("int", p[2])

def p_assignment(p):
    '''
    assignment : ID ASSIGN expression SEMICOLON
    '''

    if not is_declared(p[1]):
        add_error(
            f"Line {p.lineno(1)}: Variable '{p[1]}' used before declaration."
        )

    p[0] = Assignment(
        p[1],
        p[3]
    )

def p_expression_binop(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
    '''

    p[0] = BinaryOperation(
        p[1],
        p[2],
        p[3]
    )

def p_expression_term(p):
    '''
    expression : term
    '''

    p[0] = p[1]

def p_term_binop(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
    '''

    p[0] = BinaryOperation(
        p[1],
        p[2],
        p[3]
    )

def p_term_factor(p):
    '''
    term : factor
    '''

    p[0] = p[1]

def p_factor_number(p):
    '''
    factor : NUMBER
    '''

    p[0] = Number(p[1])

def p_factor_id(p):
    '''
    factor : ID
    '''

    if not is_declared(p[1]):
        add_error(
            f"Line {p.lineno(1)}: Variable '{p[1]}' used before declaration."
        )

    p[0] = Variable(p[1])

def p_factor_group(p):
    '''
    factor : LPAREN expression RPAREN
    '''

    p[0] = p[2]

# Syntax Error

def p_error(p):

    if p:

        add_error(
            f"Line {p.lineno}: Unexpected token '{p.value}'"
        )

        parser.errok()

    else:

        add_error(
            "Unexpected end of file."
        )

parser = yacc.yacc()