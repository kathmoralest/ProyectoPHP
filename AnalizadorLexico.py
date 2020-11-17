# Palabras reservadas
reserved = {
    "if":"IF",
    "for":"FOR"
    "break":"BREAK",
    "else":"ELSE",
    "this":"THIS",
    "true":"TRUE",
    "false":"FALSE"
}

# Lista de tokens
tokens = [
    "VARIABLE",
    "INTEGER",
    "BOOLEAN",
    "STRING"
] + list(reserved.values())

# Especificaciones de cada token

# Tokens complejos
def t_VARIABLE(t):
    r"\$[a-zA-Z_][a-zA-Z0-9]*"
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
    return t

def t_INTEGER(t):
    r"-?\d+"
    t.value = int(t.value)
    return t
    
def t_FOR(t):
    r"for"
    return t
    
def t_TRUE(t):
    r"true"
    return t

def t_FALSE(t):
    r"false"
    return t
