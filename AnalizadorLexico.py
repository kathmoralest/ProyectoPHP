import ply.lex as lex

# Palabras reservadas
reserved = {
    "const:CONST"
    "if":"IF",
    "for":"FOR",
    "while":"WHILE",
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
    "STRING",
    "FLOAT"
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

def t_CONST(t):
    r"const"
    return t

def t_FLOAT(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t

def t_FOR(t):
    r"for"
    return t

def t_WHILE(t):
    r"while"
    return t
    
def t_TRUE(t):
    r"true"
    return t

def t_FALSE(t):
    r"false"
    return t

#Ignorar caracteres
t_ignore = ' \t'
t_ignore_CM = r"//.*"


lexer = lex.lex()

def analizar(data):
    lexer.input(data)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

listaTXT=["codigoKatherineMorales.txt"]
for integrante in listaTXT:
    print("Ejemplo de: "+integrante)
    archivo = open(integrante)
    for linea in archivo:
        print(">>"+linea)
        analizar(linea)
        if len(linea)==0:
            break