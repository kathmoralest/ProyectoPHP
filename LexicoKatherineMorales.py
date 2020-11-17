# Palabras reservadas
reserved = {
    "if":"IF",
    "break":"BREAK",
    "else":"ELSE",
    "this":"THIS"
}

# Lista de tokens
tokens = [
    "VARIABLE",
    "INTEGER"
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