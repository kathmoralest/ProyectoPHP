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

# En esta seccion se compara los valores usando los operadores
def p_comparacion(p):
    '''comparacion : valor operadorC expresion PTOCO
                | valor operadorM expresion PTOCO
                | valor operadorL expresion PTOCO
    '''

#Tipo de expresiones
def p_expresion(p):
    '''expresion : valor
                 | expresion_aritmetica
                 | expresion_logica
                 | expresion_comparativa
    '''

#Formas de mostrar una expresion
def p_expresion_aritmetica(p):
    '''expresion_aritmetica : valor operadorM expresion
    '''

def p_expresion_logica(p):
    '''expresion_logica : valor operadorL expresion
                        | booleano
    '''

def p_expresion_comparativa(p):
    '''expresion_comparativa : valor operadorC expresion
    '''

def p_condicion(p):
    '''condicion : expresion_logica
                | expresion_comparativa
    '''
#Operadores matematicos
def p_operadorM(p):
    '''operadorM : MAS
                   | RESTA
                   | PROD
                   | DIV
                   | MOD
                   | POTENCIA
    '''
#Operadores matematicos
def p_operadorC(p):
    '''operadorC : MAYOR
                   | MENOR
                   | COMPARACION
                   | IDENTICO
                   | DIFERENTE
                   | NOIDENTICO
                   | MENOROIGUAL
                   | MAYOROIGUAL
                   | NAVEESPACIAL
    '''
#con esto se finaliza un php
def p_terminar(p):
    '''terminar : BREAK PTOCO
    '''

#Operadores logicos
def p_operadorL(p):
    '''operadorL : AND
                  | XOR
                  | OR
                  | NOT
    '''

#se crea el valor de una variable
def p_valor(p):
    '''valor : INTEGER
             | booleano
             | STRING
             | FLOAT
             | VARIABLE
             | BOOLEAN
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
