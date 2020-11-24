import ply.yacc as yacc
from AnalizadorLexico import tokens

def p_phpSyntax(p):
    '''phpSyntax : inicio codigo fin
    '''

def p_codigo(p):
    '''codigo : algoritmo
                | algoritmo codigo
    '''

def p_inicio(p):
    '''inicio : INICIO
    '''

def p_fin(p):
    '''fin : FIN
    '''

def p_algoritmo(p):
    '''algoritmo : asignacion
                 | declaracion
                 | comparacion
                 | condicionalIF
                 | iteracionFOR
                 | bucleWHILE
                 | bucleDO_WHILE
                 | indexacion
                 | echo
                 | terminar
    '''

def p_asignacion(p):
    '''asignacion : ambito multiVariable IGUAL expresion PTOCO
                  | multiVariable IGUAL expresion PTOCO
    '''
   
def p_declaracion(p):
    '''declaracion : ambito multiVariable PTOCO
                   | multiVariable PTOCO
    '''

def p_multiVariable(p):
     '''multiVariable : VARIABLE
                      | VARIABLE COMA multiVariable
     '''

def p_ambito(p):
    '''ambito : STATIC
               | VAR
               | GLOBAL
               | CONST
    '''

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

parser=yacc.yacc()
f=open("codigo.txt")
s=f.read()
print(s)
result = parser.parse(s)
print(result)
f.close()
