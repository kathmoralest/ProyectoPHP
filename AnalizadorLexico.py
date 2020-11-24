import ply.lex as lex

# Palabras reservadas
reserved = {
    "const":"CONST", # VARIABLES
    "var":"VAR",
    "this":"THIS",
    "static":"STATIC",
    "global":"GLOBAL",
    "true":"TRUE", # BOOLEANOS
    "false":"FALSE",
    "and":"AND", # OPERADORES LOGICOS
    "or":"OR",
    "xor":"XOR",
    "not":"NOT",
    "if":"IF", # ESTSRUCTURA DE CONTROL IF
    "else":"ELSE",
    "elseif":"ELSEIF",
    "switch":"SWITCH", # ESTRUCTURA DE CONTROL SWITCH
    "case":"CASE",
    "break":"BREAK",
    "default":"DEFAULT",
    "while":"WHILE", # LAZO WHILE
    "do":"DO",
    "for":"FOR", # LAZO FOR
    "foreach":"FOREACH",
    "array()":"ARRAY", # ARRAY
    "echo":"ECHO", # SALIDA POR PANTALLA
    "__halt_compiler()":"HALTCOMPILER",
    "abstract":"ABSTRACT",
    "as":"AS",
    "callable":"CALLABLE",
    "catch":"CATCH",
    "class":"CLASS",
    "clone":"CLONE",
    "continue":"CONTINUE",
    "declare":"DECLARE",
    "die()":"DIE",
    "empty()":"EMPTY",
    "enddeclare":"ENDDECLARE",
    "endfor":"ENDFOR",
    "endforeach":"ENDFOREACH",
    "endif":"ENDIF",
    "endswitch":"ENDSWITCH",
    "endwhile":"ENDWHILE",
    "eval()":"EVAL",
    "exit()":"EXIT",
    "extends":"EXTENDS",
    "final":"FINAL",
    "finally":"FINALLY",
    "function":"FUNCTION",
    "goto":"GOTO",
    "implements":"IMPLEMENTS",
    "include":"INCLUDE",
    "include_once":"INCLUDEONE",
    "instanceof":"INSTANCEOF",
    "insteadof":"INSTEADOF",
    "interface":"INTERFACE",
    "isset()":"ISSET",
    "list()":"LIST",
    "namespace":"NAMESPACE",
    "new":"NEW",
    "print":"PRINT",
    "private":"PRIVATE",
    "protected":"PROTECTED",
    "public":"PUBLIC",
    "require":"REQUIRE",
    "require_once":"REQUIREONCE",
    "return":"RETURN",
    "throw":"THROW",
    "trait":"TRAIT",
    "try":"TRY",
    "unset()":"UNSET",
    "use":"USE",
    "yield":"YIELD",
    "yield from":"YIELDFROM"
}

# Lista de tokens
tokens = [
    "VARIABLE",
    "CONSTANTE",
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
    "DIV",
    "RESTA",
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
    "PTO",
    "PTOCO",
    "PIZQ",
    "PDER",
    "DPTS"

] + list(reserved.values())

# Especificaciones de cada token
t_IGUAL=r"="
t_PROD = r"\*"
t_MAS = r"\+"
t_MOD = r"%"
t_MAYOR = r">"
T_MENOR = r"<"
t_DIV=r"\/"
t_POTENCIA=r"\*\*"
t_RESTA=r"-"
t_CIZQ=r"\["
t_CDER=r"\]"
t_LIZQ=r"\{"
t_LDER=r"\}"
t_PTO=r"\."
t_PTOCO=r";"
t_PIZQ=r"\("
t_PDER=r"\)"
t_DPTS=r"\:"

t_COMPARACION=r"=="
t_IDENTICO=r"==="
t_DIFERENTE=r"!=|<>"
t_NOIDENTICO=r"!=="
t_MENOROIGUAL=r"<="
t_MAYOROIGUAL=r">="
t_NAVEESPACIAL=r"<=>"
t_FUSIONNULL=r"\?\?"

# Tokens complejos
def t_ECHO(t):
    r'echo'
    return t

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

def t_CONSTANTE(t):
    r"[a-zA-Z_][a-zA-Z0-9]*"
    t.type = reserved.get(t.value, 'CONSTANTE')  # Check for reserved words
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

def t_THIS(t):
    r"this"
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
    
def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t

def t_FALSE(t):
    r"false"
    return t

#Ignorar caracteres
t_ignore = ' \t'
t_ignore_CM = r"//.*"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Token NO reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def analizar(data):
    lexer.input(data)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

listaTXT=["codigoKatherineMorales.txt","codigoAngieArgudo.txt"]
for integrante in listaTXT:
    print("Ejemplo de: "+integrante)
    archivo = open(integrante)
    for linea in archivo:
        print(">>"+linea)
        analizar(linea)
        if len(linea)==0:
            break

'''
while True:
    data = input("> ")
    analizar(data)
    if len(data)==0:
        break
'''