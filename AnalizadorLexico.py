import ply.lex as lex

estado = ""
# Palabras reservadas
##NUEVAS AÑADIDAS STATIC VAR GLOBAL
reserved = {
    "do": "DO",
    "const": "CONST",
    "if": "IF",
    "for": "FOR",
    "while": "WHILE",
    "break": "BREAK",
    "else": "ELSE",
    "elseif": "ELSEIF",
    "True": "TRUE",
    "False": "FALSE",
    "echo": "ECHO",
    "static": "STATIC",
    "var": "VAR",
    "global": "GLOBAL",
    "and": "AND",
    "or": "OR",
    "xor": "XOR",
    "not": "NOT",
    "list": "LIST",
    "function" : "FUNCTION",
    "return" : "RETURN",
    "array" : "ARRAY",
    "key" : "KEY",
    "current" : "CURRENT",
    "next" : "NEXT",
    "null": "NULL"
}

# Lista de tokens
tokens = [
             "VARIABLE",
             "VARIABLEFUNC",
             "INTEGER",
             "BOOLEAN",
             "STRING",
             "FLOAT",
             "IGUAL",
             "PROD",
             "MOD",
             "MAYOR",
             "MENOR",
             "MAS",
             "MENOS",
             "DIV",
             "POTENCIA",
             "LIZQ",
             "LDER",
             "CIZQ",
             "CDER",
             "COMPARACION",
             "IDENTICO",
             "DIFERENTE",
             "NOIDENTICO",
             "MENOROIGUAL",
             "MAYOROIGUAL",
             "NAVEESPACIAL",
             "FUSIONNULL",
             "FLECHA",
             "PTOCO",
             "PIZQ",
             "PDER",
             "INICIO",
             "FIN",
             "COMA",
             "POST",
             "GET"
             ]+ list(reserved.values())

# Especificaciones de cada token
t_IGUAL = r"="
t_PROD = r"\*"
t_MAS = r"\+"
t_MENOS = r"\-"
t_MOD = r"%"
t_MAYOR = r">"
t_MENOR = r"<"
t_DIV = r"\/"
t_POTENCIA = r"\*\*"
t_CIZQ = r"\["
t_CDER = r"\]"
t_LIZQ = r"\{"
t_LDER = r"\}"
t_PTOCO = r";"
t_PIZQ = r"\("
t_PDER = r"\)"
t_COMA = r","

t_COMPARACION = r"=="
t_IDENTICO = r"==="
t_DIFERENTE = r"!=|<>"
t_NOIDENTICO = r"!=="
t_MENOROIGUAL = r"<="
t_FLECHA = r"=>"
t_MAYOROIGUAL = r">="
t_NAVEESPACIAL = r"<=>"
t_FUSIONNULL = r"\?\?"


# Clausulas

def t_INICIO(t):
    r'(^<\?(php)?)'
    return t

def t_POST(t):
    r'(\$_POST)'
    return t

def t_GET(t):
    r'(\$_GET)'
    return t

def t_AND(t):
    r'and'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_KEY(t):
    r'key'
    return t

def t_CURRENT(t):
    r'current'
    return t

def t_NEXT(t):
    r'next'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_XOR(t):
    r'xor'
    return t

def t_OR(t):
    r'or'
    return t

def t_NOT(t):
    r'not'
    return t

def t_FIN(t):
    r'\?>$'
    return t

# Tokens complejos
def t_ECHO(t):
    r'echo'
    return t

def t_NULL(t):
    r'NULL'
    return t

# Tokens complejos

def t_VARIABLE(t):
    r"\$[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
    return t

def t_VARIABLEFUNC(t):
    r"[a-zA-Z_][a-zA-Z0-9]*"
    t.type = reserved.get(t.value, 'VARIABLEFUNC')  # Check for reserved words
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

def t_IF(t):
    r"if"
    return t

def t_BREAK(t):
    r"break"
    return t

def t_ELSE(t):
    r"else"
    return t

def t_DO(t):
    r"do"
    return t

def t_FOR(t):
    r"for"
    return t

def t_STATIC(t):
    r"static"
    return t

def t_VAR(t):
    r"var"
    return t

def t_GLOBAL(t):
    r"global"
    return t

def t_WHILE(t):
    r"while"
    return t

def t_TRUE(t):
    r"True"
    return t


def t_STRING(t):
    r'((".*")|(\'.*\'))'
    return t

def t_FALSE(t):
    r"False"
    return t

def t_LIST(t):
    r'list'
    return t

# Ignorar caracteres
t_ignore = ' \t'
t_ignore_CM = r"//.*"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    global estado
    estado+="\n\tToken NO reconocido '%s'" % t.value[0]+"\n\n"
    print("Token NO reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()



def l(texto):
    global estado
    estado=""
    data = texto
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        estado += str(tok) + "\n"
    return estado