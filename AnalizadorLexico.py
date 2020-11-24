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
    "PTOCO",
    "PIZQ",
    "PDER",
    "INICIO",
    "FIN",
    "COMA",
    "DOSPUNTOS"

] + list(reserved.values())

# Especificaciones de cada token
t_IGUAL=r"="
t_PROD = r"\*"
t_MAS = r"\+"
t_MOD = r"%"
t_MAYOR = r">"
t_MENOR = r"<"
t_DIV=r"\/"
t_POTENCIA=r"\*\*"
t_RESTA=r"-"
t_CIZQ=r"\["
t_CDER=r"\]"
t_LIZQ=r"\{"
t_LDER=r"\}"
t_PTOCO=r";"
t_PIZQ=r"\("
t_PDER=r"\)"
t_COMA=r","
t_DOSPUNTOS=r":"

t_COMPARACION=r"=="
t_IDENTICO=r"==="
t_DIFERENTE=r"!=|<>"
t_NOIDENTICO=r"!=="
t_MENOROIGUAL=r"<="
t_MAYOROIGUAL=r">="
t_NAVEESPACIAL=r"<=>"
t_FUSIONNULL=r"\?\?"

# CLAUSULAS
def t_INICIO(t):
    r'(<\?(php)?)'
    return t

def t_FIN(t):
    r'\?>'
    return t

# TOKENS COMPLEJOS
def t_VARIABLE(t):
    r"\$[a-zA-Z_][a-zA-Z0-9]*"
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
    return t

def t_INTEGER(t):
    r"-?\d+"
    t.value = int(t.value)
    return t

def t_CONSTANTE(t):
    r"[a-zA-Z_][a-zA-Z0-9]*"
    t.type = reserved.get(t.value, 'CONSTANTE')  # Check for reserved words
    return t

def t_FLOAT(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t

def t_CONST(t):
    r"const"
    return t

def t_VAR(t):
    r'var'
    return t

def t_THIS(t):
    r"this"
    return t

def t_STATIC(t):
    r"static"
    return t

def t_GLOBAL(t):
    r"global"
    return t

# BOOLEANOS
def t_TRUE(t):
    r"true"
    return t

def t_FALSE(t):
    r"false"
    return t

# OPERADORES LOGICOS
def t_AND(t):
    r'and'
    return t

def t_OR(t):
    r'or'
    return t

def t_XOR(t):
    r'xor'
    return t

def t_NOT(t):
    r'not'
    return t

# ESTRUCTURA DE CONTROL IF
def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELSEIF(t):
    r'(elseif)|(else if)'
    return t

# ESTRUCTURA DE CONTROL SWITCH
def t_SWITCH(t):
    r'switch'
    return t

def t_CASE(t):
    r'case'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_DEFAULT(t):
    r'default'
    return t

# LAZO WHILE
def t_WHILE(t):
    r'while'
    return t

def t_DO(t):
    r'do'
    return t

# LAZO FOR
def t_FOR(t):
    r'for'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

# ARRAY
def t_ARRAY(t):
    r'array(\(\))?'
    return t

# SALIDA POR PANTALLA
def t_ECHO(t):
    r'echo'
    return t

# OTRAS PALABRAS RESERVADAS
def t_HALTCOMPILER(t):
    r'__halt_compiler(\(\))?'
    return t

def t_ABSTRACT(t):
    r'abstract'
    return t

def t_AS(t):
    r'as'
    return t

def t_CALLABLE(t):
    r'callable'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CLONE(t):
    r'clone'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DECLARE(t):
    r'declare'
    return t

def t_DIE(t):
    r'die(\(\))?'
    return t

def t_EMPTY(t):
    r'empty(\(\))?'
    return t

def t_ENDDECLARE(t):
    r'enddeclare'
    return t

def t_ENDFOR(t):
    r'endfor'
    return t

def t_ENDFOREACH(t):
    r'endforeach'
    return t

def t_ENDIF(t):
    r'endif'
    return t

def t_ENDSWITCH(t):
    r'endswitch'
    return t

def t_ENDWHILE(t):
    r'endwhile'
    return t

def t_EVAL(t):
    r'eval(\(\))?'
    return t

def t_EXIT(t):
    r'exit(\(\))?'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_FINAL(t):
    r'final'
    return t

def t_FINALLY(t):
    r'finally'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_IMPLEMENTS(t):
    r'implements'
    return t

def t_INCLUDE(t):
    r'include'
    return t

def t_INCLUDEONE(t):
    r'include_once'
    return t

def t_INSTANCEOF(t):
    r'instanceof'
    return t

def t_INSTEADOF(t):
    r'insteadof'
    return t

def t_INTERFACE(t):
    r'interface'
    return t

def t_ISSET(t):
    r'isset(\(\))?'
    return t

def t_LIST(t):
    r'list(\(\))?'
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_NEW(t):
    r'new'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_REQUIREONCE(t):
    r'require_once'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_THROW(t):
    r'throw'
    return t

def t_TRAIT(t):
    r'trait'
    return t

def t_TRY(t):
    r'try'
    return t

def t_UNSET(t):
    r'unset(\(\))?'
    return t

def t_USE(t):
    r'use'
    return t

def t_YIELD(t):
    r'yield'
    return t

def t_YIELDFROM(t):
    r'yield from'
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

listaTXT=["codigoKatherineMorales.txt","codigoAngieArgudo.txt","codigoMiguelParra.txt"]
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