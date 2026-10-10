import ply.lex as lex

reserved = {
    'int': 'INT',
    'if': 'IF',
    'while': 'WHILE',
    'print': 'PRINT'
}

tokens = [
    'ID',
    'NUMBER',

    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',

    'ASSIGN',

    'SEMICOLON',

    'LPAREN',
    'RPAREN',

    'LBRACE',
    'RBRACE'
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_ASSIGN = r'='

t_SEMICOLON = r';'

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Ignore spaces and tabs
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()