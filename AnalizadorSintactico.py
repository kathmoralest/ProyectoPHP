import ply.yacc as yacc
from AnalizadorLexico import tokens


def p_phpSyntax(p):  # define que se empiece el código correctamente con "<?php" y se termine con "?>"
    '''phpSyntax : inicio codigo fin
                  | inicio fin
    '''


def p_codigo(p):  # define todo el código
    '''codigo : algoritmo
                | algoritmo codigo
                | ""
    '''


def p_inicio(p):
    '''inicio : INICIO
    '''


def p_fin(p):
    '''fin : FIN
    '''


def p_algoritmo(p):  # diferentes algoritmos que se pueden utilizar
    '''algoritmo : asignacion
                 | declaracion
                 | comparacion
                 | condicionalIF
                 | iteracionFOR
                 | bucleWHILE
                 | bucleDO_WHILE
                 | indexacion
                 | echo
                 | list
                 | terminar
                 | funciones
                 | funcCOD
                 | ingresoDatos
                 | arrayfunctionsC
    '''


def p_asignacion(p):  # se pueden asignar variables usando el ambito o no, intentamos usar el empty para esto pero no nos funciono
    '''asignacion : ambito multiVariable IGUAL expresion PTOCO
                  | multiVariable IGUAL expresion PTOCO
                  | CONST multiConstante IGUAL expresion PTOCO
                  | multiConstante IGUAL expresion PTOCO
    '''


def p_declaracion(p):  # se pueden definir variables usando el ambito o no
    '''declaracion : ambito multiVariable PTOCO
                   | multiVariable PTOCO
                   | CONST multiConstante PTOCO
                   | multiConstante PTOCO
    '''


def p_multiVariable(p):  # se puede definir una variable o varias seguidas de coma
    '''multiVariable : VARIABLE
                     | VARIABLE COMA multiVariable
    '''


def p_multiConstante(p):  # se puede definir una variable o varias seguidas de coma
    '''multiConstante : VARIABLEFUNC
                     | VARIABLEFUNC COMA multiConstante
    '''


def p_ambito(p):  # se utilizan para definir variables, se pueden no utilizar
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

def p_multiIngreso(p):  # se puede definir una variable o varias seguidas de coma
    '''multiIngreso : VARIABLE
                     | expresion
                     | VARIABLE COMA multiIngreso
                     | expresion COMA multiIngreso
    '''
#
def p_funcCOD(p):
    '''funcCOD : VARIABLEFUNC PIZQ multiIngreso PDER PTOCO
                | VARIABLEFUNC PIZQ PDER PTOCO
    '''

#nombre de la funcion
def p_funcAsig(p):
    '''funcAsig : VARIABLEFUNC PIZQ multiVariable PDER
    '''


def p_Arreglo(p):
    '''Arreglo : ARRAY PIZQ innerColection PDER
    '''

# asignacion indice de expresion $array=array('nombre'=>2,'miguel'=>3,'katherine')
def p_Asig(p):
    '''Asig : expresion FLECHA expresion
    '''


def p_innerColection(p):
    '''innerColection : expresion
                      | Asig
                      | expresion COMA innerColection
                      | Asig COMA innerColection
    '''

# Tipo de expresiones
def p_expresion(p):
    '''expresion : valor
                 | expresion_aritmetica
                 | expresion_logica
                 | expresion_comparativa
                 | VARIABLE
                 | funcAsig
                 | arrayfunctions
                 | Arreglo
                 | matematica
    '''

def p_avInner(p):
    '''avInner : Arreglo
                | VARIABLE
    '''

#
def p_arrayfunctionsC(p):
    '''arrayfunctionsC : KEY PIZQ avInner PDER PTOCO
                       | CURRENT PIZQ avInner PDER PTOCO
                       | NEXT PIZQ avInner PDER PTOCO
    '''

# trata los arrays como variables
def p_arrayfunctions(p):
    '''arrayfunctions : KEY PIZQ avInner PDER
                       | CURRENT PIZQ avInner PDER
                       | NEXT PIZQ avInner PDER
    '''


# Formas de mostrar una expresion
def p_expresion_aritmetica(p):
    '''expresion_aritmetica : valor operadorM expresion
    '''


def p_expresion_logica(p):
    '''expresion_logica : valor operadorL expresion
                        | booleano
    '''


def p_expresion_comparativa(p):
    '''expresion_comparativa : expresion operadorC expresion
    '''


def p_condicion(p):
    '''condicion : expresion_logica
                | expresion_comparativa
    '''


def p_retorno(p):
    '''retorno : RETURN multiVariable PTOCO
                | RETURN expresion PTOCO
    '''


def p_dentroFUNC(p):
    '''dentroFUNC : retorno
                    | codigo dentroFUNC
                    | codigo
    '''


def p_funciones(p):
    '''funciones : FUNCTION VARIABLEFUNC PIZQ multiVariable PDER LIZQ dentroFUNC LDER
                | FUNCTION VARIABLEFUNC PIZQ PDER LIZQ dentroFUNC LDER
    '''


# Operadores matematicos
def p_conjuntoMatematico(p):
    '''conjuntoMatematico : PIZQ matematica PDER'''

def p_Operator(p):
    '''Operator : INTEGER
                | conjuntoMatematico
                | VARIABLE
    '''
def p_matematica(p):
    '''matematica : Operator
                    | Operator operadorM matematica
    '''

def p_operadorM(p):
    '''operadorM : MAS
                   | MENOS
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
             | ingresoDatos
             | arrayfunctions
             | Arreglo
             | NULL
             | matematica
    '''


def p_ingresoDatos(p):
    '''ingresoDatos : GET CIZQ STRING CDER
                    | POST CIZQ STRING CDER
    '''


def p_booleano(p):  # se definen los booleanos a utilizar
    '''booleano : TRUE
                | FALSE
    '''

def p_incDec(p): # se define la estructura de la adicion por ejemplo: para agregar uno a un contador
    '''adicion : MAS MAS VARIABLE
               | MENOS MENOS VARIABLE
               | VARIABLE MAS MAS
               | VARIABLE MENOS MENOS
    '''


def p_condicionalIF(p):  # se definen las posibles formas de if que se pueden utilizar
    '''condicionalIF : IF PIZQ condicion PDER LIZQ codigo LDER
                      | IF PIZQ condicion PDER LIZQ codigo LDER condicionalELSE
                      | IF PIZQ condicion PDER codigo
                      | IF PIZQ condicion PDER codigo condicionalELSE
    '''


def p_condicionalELSE(p):  # se definen el condicional else y elseif
    '''condicionalELSE : ELSE LIZQ codigo LDER
                 | ELSEIF PIZQ condicion PDER LIZQ codigo LDER condicionalELSE
                 | ELSE codigo
                 | ELSEIF PIZQ condicion PDER codigo condicionalELSE
     '''


def p_iteracionFOR(p):  # se define la iteracion for
    '''iteracionFOR : FOR PIZQ asignacion condicion PTOCO adicion PDER codigo
                    | FOR PIZQ asignacion condicion PTOCO adicion PDER LIZQ codigo LDER
    '''

def p_bucleWHILE(p):
    '''bucleWHILE : WHILE PIZQ condicion PDER codigo
                    | WHILE PIZQ condicion PDER LIZQ codigo LDER
    '''

def p_bucleDO_WHILE(p):
    '''bucleDO_WHILE : DO LIZQ codigo LDER WHILE PIZQ condicion PDER PTOCO
	                | DO LIZQ codigo LDER WHILE PIZQ condicion PDER LIZQ codigo LDER
	'''

def p_list(p):
    '''list : LIST PIZQ valoresList PDER IGUAL VARIABLE PTOCO
    '''

def p_valoresList(p):
    '''valoresList : VARIABLE COMA valoresList
                    | VARIABLE
    '''

def p_indexacion(p): # se define la indexación en caso de necesitarse en los array
    '''indexacion :  VARIABLE CIZQ INTEGER CDER
                    | VARIABLE CIZQ MENOS INTEGER CDER
                    | VARIABLE CIZQ INTEGER CDER FUSIONNULL
                    | VARIABLE CIZQ MENOS INTEGER CDER FUSIONNULL
    '''


def p_echo(p):
    '''echo : ECHO VARIABLE PTOCO
            | ECHO expresion PTOCO
    '''


def p_error(p):
    global estado
    estado = "\n\n\n\n\n\n\n\n\n\n\tSyntax error in input!"
    print("Syntax error in input!")


parser = yacc.yacc()


def p(texto):
    global estado
    estado = "\n\n\n\n\n\n\n\n\n\n\t\tPERFECT!"
    parser.parse(texto)
    return estado