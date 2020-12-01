
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOLEAN BREAK CDER CIZQ COMA COMPARACION CONST DIFERENTE DIV DO ECHO ELSE ELSEIF FALSE FIN FLOAT FOR FUSIONNULL GLOBAL IDENTICO IF IGUAL INICIO INTEGER LDER LIZQ MAS MAYOR MAYOROIGUAL MENOR MENOROIGUAL MENOS MOD NAVEESPACIAL NOIDENTICO NOT OR PDER PIZQ POTENCIA PROD PTOCO RESTA STATIC STRING TRUE VAR VARIABLE WHILE XORphpSyntax : inicio codigo fin\n                  | inicio fin\n    codigo : algoritmo\n                | algoritmo codigo\n                | ""\n    inicio : INICIO\n    fin : FIN\n    algoritmo : asignacion\n                 | declaracion\n                 | comparacion\n                 | condicionalIF\n                 | iteracionFOR\n                 | bucleWHILE\n                 | bucleDO_WHILE\n                 | indexacion\n                 | echo\n                 | terminar\n    asignacion : ambito multiVariable IGUAL expresion PTOCO\n                  | multiVariable IGUAL expresion PTOCO\n    declaracion : ambito multiVariable PTOCO\n                   | multiVariable PTOCO\n    multiVariable : VARIABLE\n                      | VARIABLE COMA multiVariable\n     ambito : STATIC\n               | VAR\n               | GLOBAL\n               | CONST\n    comparacion : valor operadorC expresion PTOCO\n                | valor operadorM expresion PTOCO\n                | valor operadorL expresion PTOCO\n    expresion : valor\n                 | expresion_aritmetica\n                 | expresion_logica\n                 | expresion_comparativa\n    expresion_aritmetica : valor operadorM expresion\n    expresion_logica : valor operadorL expresion\n                        | booleano\n    expresion_comparativa : valor operadorC expresion\n    condicion : expresion_logica\n                | expresion_comparativa\n    operadorM : MAS\n                   | RESTA\n                   | PROD\n                   | DIV\n                   | MOD\n                   | POTENCIA\n    operadorC : MAYOR\n                   | MENOR\n                   | COMPARACION\n                   | IDENTICO\n                   | DIFERENTE\n                   | NOIDENTICO\n                   | MENOROIGUAL\n                   | MAYOROIGUAL\n                   | NAVEESPACIAL\n    terminar : BREAK PTOCO\n    operadorL : AND\n                  | XOR\n                  | OR\n                  | NOT\n    valor : INTEGER\n             | booleano\n             | STRING\n             | FLOAT\n             | VARIABLE\n             | BOOLEAN\n    booleano : TRUE\n                | FALSE\n    adicion : MAS MAS VARIABLE\n               | MENOS MENOS VARIABLE\n               | VARIABLE MAS MAS\n               | VARIABLE MENOS MENOS\n    condicionalIF : IF PIZQ condicion PDER LIZQ codigo LDER\n\t\t\t\t\t  | IF PIZQ condicion PDER LIZQ codigo LDER condicionalELSE\n\t\t\t\t\t  | IF PIZQ condicion PDER codigo\n\t\t\t\t\t  | IF PIZQ condicion PDER codigo condicionalELSE\n\tcondicionalELSE : ELSE LIZQ codigo LDER\n\t\t\t\t | ELSEIF PIZQ condicion PDER LIZQ codigo LDER condicionalELSE\n\t\t\t\t | ELSE codigo\n\t\t\t\t | ELSEIF PIZQ condicion PDER codigo condicionalELSE\n\t iteracionFOR : FOR PIZQ asignacion condicion PTOCO adicion PDER codigo\n\t                | FOR PIZQ asignacion condicion PTOCO adicion PDER LIZQ codigo LDER\n\tbucleWHILE : WHILE PIZQ condicion PDER codigo\n\t                | WHILE PIZQ condicion PDER LIZQ codigo LDER\n\tbucleDO_WHILE : DO LIZQ codigo LDER WHILE PIZQ condicion PDER codigo\n\t                | DO LIZQ codigo LDER WHILE PIZQ condicion PDER LIZQ codigo LDER\n\tindexacion :  VARIABLE CIZQ INTEGER CDER\n                    | VARIABLE CIZQ RESTA INTEGER CDER\n                    | VARIABLE CIZQ INTEGER CDER FUSIONNULL\n                    | VARIABLE CIZQ RESTA INTEGER CDER FUSIONNULL\n    echo : ECHO VARIABLE PTOCO\n            | ECHO expresion PTOCO\n    '
    
_lr_action_items = {'INICIO':([0,],[3,]),'$end':([1,5,8,40,],[0,-2,-7,-1,]),'':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,41,45,71,81,83,102,103,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,141,142,143,144,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[7,-6,7,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,7,-56,-20,-91,-92,-19,-28,-29,-30,7,7,-87,-18,7,-75,-83,7,-89,-88,-76,7,-90,-73,7,-79,7,-84,-74,-81,7,7,-77,7,7,-85,7,-82,-80,-86,-78,]),'FIN':([2,3,4,6,7,9,10,11,12,13,14,15,16,17,18,41,45,81,83,102,103,108,109,110,111,117,122,124,126,129,130,132,141,142,144,151,153,156,163,167,170,173,174,176,],[8,-6,8,-3,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,-56,-20,-91,-92,-19,-28,-29,-30,-87,-18,-75,-83,-89,-88,-76,-90,-73,-79,-84,-74,-81,-77,-85,-82,-80,-86,-78,]),'IF':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,41,45,71,81,83,102,103,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,141,142,143,144,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[22,-6,22,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,22,-56,-20,-91,-92,-19,-28,-29,-30,22,22,-87,-18,22,-75,-83,22,-89,-88,-76,22,-90,-73,22,-79,22,-84,-74,-81,22,22,-77,22,22,-85,22,-82,-80,-86,-78,]),'FOR':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,41,45,71,81,83,102,103,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,141,142,143,144,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[23,-6,23,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,23,-56,-20,-91,-92,-19,-28,-29,-30,23,23,-87,-18,23,-75,-83,23,-89,-88,-76,23,-90,-73,23,-79,23,-84,-74,-81,23,23,-77,23,23,-85,23,-82,-80,-86,-78,]),'WHILE':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,41,45,71,81,83,102,103,108,109,110,111,112,115,116,117,122,123,124,126,127,129,130,132,133,141,142,143,144,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[24,-6,24,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,24,-56,-20,-91,-92,-19,-28,-29,-30,24,24,128,-87,-18,24,-75,-83,24,-89,-88,-76,24,-90,-73,24,-79,24,-84,-74,-81,24,24,-77,24,24,-85,24,-82,-80,-86,-78,]),'DO':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,41,45,71,81,83,102,103,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,141,142,143,144,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[25,-6,25,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,25,-56,-20,-91,-92,-19,-28,-29,-30,25,25,-87,-18,25,-75,-83,25,-89,-88,-76,25,-90,-73,25,-79,25,-84,-74,-81,25,25,-77,25,25,-85,25,-82,-80,-86,-78,]),'VARIABLE':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,19,28,30,31,32,33,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,73,81,82,83,94,95,102,103,104,105,106,108,109,110,111,112,115,117,122,123,124,125,126,127,129,130,132,133,140,141,142,143,144,145,146,147,150,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[26,-6,26,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,43,74,-24,-25,-26,-27,-4,85,-21,85,85,85,-47,-48,-49,-50,-51,-52,-53,-54,-55,-41,-42,-43,-44,-45,-46,-57,-58,-59,-60,85,43,85,26,43,-56,85,-20,85,43,-91,-92,85,85,85,-19,-28,-29,-30,26,26,-87,-18,26,-75,137,-83,26,-89,-88,-76,26,85,-90,-73,26,-79,85,26,158,161,-84,-74,-81,26,26,-77,26,26,-85,26,-82,-80,-86,-78,]),'ECHO':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,41,45,71,81,83,102,103,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,141,142,143,144,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[28,-6,28,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,28,-56,-20,-91,-92,-19,-28,-29,-30,28,28,-87,-18,28,-75,-83,28,-89,-88,-76,28,-90,-73,28,-79,28,-84,-74,-81,28,28,-77,28,28,-85,28,-82,-80,-86,-78,]),'BREAK':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,41,45,71,81,83,102,103,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,141,142,143,144,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[29,-6,29,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,29,-56,-20,-91,-92,-19,-28,-29,-30,29,29,-87,-18,29,-75,-83,29,-89,-88,-76,29,-90,-73,29,-79,29,-84,-74,-81,29,29,-77,29,29,-85,29,-82,-80,-86,-78,]),'STATIC':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,41,45,69,71,81,83,102,103,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,141,142,143,144,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[30,-6,30,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,30,30,-56,-20,-91,-92,-19,-28,-29,-30,30,30,-87,-18,30,-75,-83,30,-89,-88,-76,30,-90,-73,30,-79,30,-84,-74,-81,30,30,-77,30,30,-85,30,-82,-80,-86,-78,]),'VAR':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,41,45,69,71,81,83,102,103,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,141,142,143,144,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[31,-6,31,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,31,31,-56,-20,-91,-92,-19,-28,-29,-30,31,31,-87,-18,31,-75,-83,31,-89,-88,-76,31,-90,-73,31,-79,31,-84,-74,-81,31,31,-77,31,31,-85,31,-82,-80,-86,-78,]),'GLOBAL':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,41,45,69,71,81,83,102,103,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,141,142,143,144,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[32,-6,32,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,32,32,-56,-20,-91,-92,-19,-28,-29,-30,32,32,-87,-18,32,-75,-83,32,-89,-88,-76,32,-90,-73,32,-79,32,-84,-74,-81,32,32,-77,32,32,-85,32,-82,-80,-86,-78,]),'CONST':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,41,45,69,71,81,83,102,103,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,141,142,143,144,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[33,-6,33,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,33,33,-56,-20,-91,-92,-19,-28,-29,-30,33,33,-87,-18,33,-75,-83,33,-89,-88,-76,33,-90,-73,33,-79,33,-84,-74,-81,33,33,-77,33,33,-85,33,-82,-80,-86,-78,]),'INTEGER':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,28,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,72,81,82,83,94,100,102,103,104,105,106,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,140,141,142,143,144,145,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[27,-6,27,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,27,-4,27,-21,27,27,27,-47,-48,-49,-50,-51,-52,-53,-54,-55,-41,-42,-43,-44,-45,-46,-57,-58,-59,-60,27,27,27,99,-56,27,-20,27,118,-91,-92,27,27,27,-19,-28,-29,-30,27,27,-87,-18,27,-75,-83,27,-89,-88,-76,27,27,-90,-73,27,-79,27,27,-84,-74,-81,27,27,-77,27,27,-85,27,-82,-80,-86,-78,]),'STRING':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,28,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,81,82,83,94,102,103,104,105,106,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,140,141,142,143,144,145,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[35,-6,35,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,35,-4,35,-21,35,35,35,-47,-48,-49,-50,-51,-52,-53,-54,-55,-41,-42,-43,-44,-45,-46,-57,-58,-59,-60,35,35,35,-56,35,-20,35,-91,-92,35,35,35,-19,-28,-29,-30,35,35,-87,-18,35,-75,-83,35,-89,-88,-76,35,35,-90,-73,35,-79,35,35,-84,-74,-81,35,35,-77,35,35,-85,35,-82,-80,-86,-78,]),'FLOAT':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,28,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,81,82,83,94,102,103,104,105,106,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,140,141,142,143,144,145,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[36,-6,36,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,36,-4,36,-21,36,36,36,-47,-48,-49,-50,-51,-52,-53,-54,-55,-41,-42,-43,-44,-45,-46,-57,-58,-59,-60,36,36,36,-56,36,-20,36,-91,-92,36,36,36,-19,-28,-29,-30,36,36,-87,-18,36,-75,-83,36,-89,-88,-76,36,36,-90,-73,36,-79,36,36,-84,-74,-81,36,36,-77,36,36,-85,36,-82,-80,-86,-78,]),'BOOLEAN':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,28,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,81,82,83,94,102,103,104,105,106,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,140,141,142,143,144,145,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[37,-6,37,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,37,-4,37,-21,37,37,37,-47,-48,-49,-50,-51,-52,-53,-54,-55,-41,-42,-43,-44,-45,-46,-57,-58,-59,-60,37,37,37,-56,37,-20,37,-91,-92,37,37,37,-19,-28,-29,-30,37,37,-87,-18,37,-75,-83,37,-89,-88,-76,37,37,-90,-73,37,-79,37,37,-84,-74,-81,37,37,-77,37,37,-85,37,-82,-80,-86,-78,]),'TRUE':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,28,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,81,82,83,94,102,103,104,105,106,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,140,141,142,143,144,145,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[38,-6,38,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,38,-4,38,-21,38,38,38,-47,-48,-49,-50,-51,-52,-53,-54,-55,-41,-42,-43,-44,-45,-46,-57,-58,-59,-60,38,38,38,-56,38,-20,38,-91,-92,38,38,38,-19,-28,-29,-30,38,38,-87,-18,38,-75,-83,38,-89,-88,-76,38,38,-90,-73,38,-79,38,38,-84,-74,-81,38,38,-77,38,38,-85,38,-82,-80,-86,-78,]),'FALSE':([2,3,6,7,9,10,11,12,13,14,15,16,17,18,28,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,81,82,83,94,102,103,104,105,106,108,109,110,111,112,115,117,122,123,124,126,127,129,130,132,133,140,141,142,143,144,145,146,151,153,156,157,162,163,164,166,167,168,170,173,174,176,],[39,-6,39,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,39,-4,39,-21,39,39,39,-47,-48,-49,-50,-51,-52,-53,-54,-55,-41,-42,-43,-44,-45,-46,-57,-58,-59,-60,39,39,39,-56,39,-20,39,-91,-92,39,39,39,-19,-28,-29,-30,39,39,-87,-18,39,-75,-83,39,-89,-88,-76,39,39,-90,-73,39,-79,39,39,-84,-74,-81,39,39,-77,39,39,-85,39,-82,-80,-86,-78,]),'LDER':([6,7,9,10,11,12,13,14,15,16,17,18,41,45,81,83,98,102,103,108,109,110,111,117,122,124,126,129,130,131,132,139,141,142,144,151,153,154,156,163,165,167,170,171,172,173,174,176,],[-3,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,-56,-20,116,-91,-92,-19,-28,-29,-30,-87,-18,-75,-83,-89,-88,142,-76,151,-90,-73,-79,-84,-74,163,-81,-77,170,-85,-82,174,175,-80,-86,-78,]),'ELSE':([6,7,9,10,11,12,13,14,15,16,17,18,41,45,81,83,102,103,108,109,110,111,117,122,124,126,129,130,132,141,142,144,151,153,156,163,167,169,170,173,174,175,176,],[-3,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,-56,-20,-91,-92,-19,-28,-29,-30,-87,-18,133,-83,-89,-88,-76,-90,133,-79,-84,-74,-81,-77,-85,133,-82,-80,-86,133,-78,]),'ELSEIF':([6,7,9,10,11,12,13,14,15,16,17,18,41,45,81,83,102,103,108,109,110,111,117,122,124,126,129,130,132,141,142,144,151,153,156,163,167,169,170,173,174,175,176,],[-3,-5,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-4,-21,-56,-20,-91,-92,-19,-28,-29,-30,-87,-18,134,-83,-89,-88,-76,-90,134,-79,-84,-74,-81,-77,-85,134,-82,-80,-86,134,-78,]),'IGUAL':([20,26,42,43,96,101,114,],[44,-22,82,-22,44,-23,82,]),'PTOCO':([20,26,27,29,35,36,37,38,39,42,43,74,75,76,77,78,79,80,84,85,86,87,88,90,91,93,101,107,113,119,120,121,],[45,-22,-61,81,-63,-64,-66,-67,-68,83,-22,102,103,-31,-32,-33,-34,-37,108,-65,109,110,111,-39,-40,-37,-23,122,125,-35,-36,-38,]),'MAYOR':([21,26,27,34,35,36,37,38,39,74,76,80,85,92,93,],[49,-65,-61,-62,-63,-64,-66,-67,-68,-65,49,-62,-65,49,-62,]),'MENOR':([21,26,27,34,35,36,37,38,39,74,76,80,85,92,93,],[50,-65,-61,-62,-63,-64,-66,-67,-68,-65,50,-62,-65,50,-62,]),'COMPARACION':([21,26,27,34,35,36,37,38,39,74,76,80,85,92,93,],[51,-65,-61,-62,-63,-64,-66,-67,-68,-65,51,-62,-65,51,-62,]),'IDENTICO':([21,26,27,34,35,36,37,38,39,74,76,80,85,92,93,],[52,-65,-61,-62,-63,-64,-66,-67,-68,-65,52,-62,-65,52,-62,]),'DIFERENTE':([21,26,27,34,35,36,37,38,39,74,76,80,85,92,93,],[53,-65,-61,-62,-63,-64,-66,-67,-68,-65,53,-62,-65,53,-62,]),'NOIDENTICO':([21,26,27,34,35,36,37,38,39,74,76,80,85,92,93,],[54,-65,-61,-62,-63,-64,-66,-67,-68,-65,54,-62,-65,54,-62,]),'MENOROIGUAL':([21,26,27,34,35,36,37,38,39,74,76,80,85,92,93,],[55,-65,-61,-62,-63,-64,-66,-67,-68,-65,55,-62,-65,55,-62,]),'MAYOROIGUAL':([21,26,27,34,35,36,37,38,39,74,76,80,85,92,93,],[56,-65,-61,-62,-63,-64,-66,-67,-68,-65,56,-62,-65,56,-62,]),'NAVEESPACIAL':([21,26,27,34,35,36,37,38,39,74,76,80,85,92,93,],[57,-65,-61,-62,-63,-64,-66,-67,-68,-65,57,-62,-65,57,-62,]),'MAS':([21,26,27,34,35,36,37,38,39,74,76,80,85,125,136,137,148,],[58,-65,-61,-62,-63,-64,-66,-67,-68,-65,58,-62,-65,136,147,148,159,]),'RESTA':([21,26,27,34,35,36,37,38,39,72,74,76,80,85,],[59,-65,-61,-62,-63,-64,-66,-67,-68,100,-65,59,-62,-65,]),'PROD':([21,26,27,34,35,36,37,38,39,74,76,80,85,],[60,-65,-61,-62,-63,-64,-66,-67,-68,-65,60,-62,-65,]),'DIV':([21,26,27,34,35,36,37,38,39,74,76,80,85,],[61,-65,-61,-62,-63,-64,-66,-67,-68,-65,61,-62,-65,]),'MOD':([21,26,27,34,35,36,37,38,39,74,76,80,85,],[62,-65,-61,-62,-63,-64,-66,-67,-68,-65,62,-62,-65,]),'POTENCIA':([21,26,27,34,35,36,37,38,39,74,76,80,85,],[63,-65,-61,-62,-63,-64,-66,-67,-68,-65,63,-62,-65,]),'AND':([21,26,27,34,35,36,37,38,39,74,76,80,85,92,93,],[64,-65,-61,-62,-63,-64,-66,-67,-68,-65,64,-62,-65,64,-62,]),'XOR':([21,26,27,34,35,36,37,38,39,74,76,80,85,92,93,],[65,-65,-61,-62,-63,-64,-66,-67,-68,-65,65,-62,-65,65,-62,]),'OR':([21,26,27,34,35,36,37,38,39,74,76,80,85,92,93,],[66,-65,-61,-62,-63,-64,-66,-67,-68,-65,66,-62,-65,66,-62,]),'NOT':([21,26,27,34,35,36,37,38,39,74,76,80,85,92,93,],[67,-65,-61,-62,-63,-64,-66,-67,-68,-65,67,-62,-65,67,-62,]),'PIZQ':([22,23,24,128,134,],[68,69,70,140,145,]),'LIZQ':([25,112,115,133,146,162,164,],[71,123,127,143,157,166,168,]),'CIZQ':([26,],[72,]),'COMA':([26,43,],[73,73,]),'PDER':([27,35,36,37,38,39,76,77,78,79,80,85,89,90,91,93,97,119,120,121,135,152,155,158,159,160,161,],[-61,-63,-64,-66,-67,-68,-31,-32,-33,-34,-37,-65,112,-39,-40,-37,115,-35,-36,-38,146,162,164,-69,-71,-72,-70,]),'CDER':([99,118,],[117,130,]),'FUSIONNULL':([117,130,],[129,141,]),'MENOS':([125,137,138,149,],[138,149,150,160,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'phpSyntax':([0,],[1,]),'inicio':([0,],[2,]),'codigo':([2,6,71,112,115,123,127,133,143,146,157,162,164,166,168,],[4,41,98,124,126,131,139,144,154,156,165,167,169,171,172,]),'fin':([2,4,],[5,40,]),'algoritmo':([2,6,71,112,115,123,127,133,143,146,157,162,164,166,168,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'asignacion':([2,6,69,71,112,115,123,127,133,143,146,157,162,164,166,168,],[9,9,94,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'declaracion':([2,6,71,112,115,123,127,133,143,146,157,162,164,166,168,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'comparacion':([2,6,71,112,115,123,127,133,143,146,157,162,164,166,168,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'condicionalIF':([2,6,71,112,115,123,127,133,143,146,157,162,164,166,168,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'iteracionFOR':([2,6,71,112,115,123,127,133,143,146,157,162,164,166,168,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'bucleWHILE':([2,6,71,112,115,123,127,133,143,146,157,162,164,166,168,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'bucleDO_WHILE':([2,6,71,112,115,123,127,133,143,146,157,162,164,166,168,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'indexacion':([2,6,71,112,115,123,127,133,143,146,157,162,164,166,168,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'echo':([2,6,71,112,115,123,127,133,143,146,157,162,164,166,168,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'terminar':([2,6,71,112,115,123,127,133,143,146,157,162,164,166,168,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'ambito':([2,6,69,71,112,115,123,127,133,143,146,157,162,164,166,168,],[19,19,95,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'multiVariable':([2,6,19,69,71,73,95,112,115,123,127,133,143,146,157,162,164,166,168,],[20,20,42,96,20,101,114,20,20,20,20,20,20,20,20,20,20,20,20,]),'valor':([2,6,28,44,46,47,48,68,70,71,82,94,104,105,106,112,115,123,127,133,140,143,145,146,157,162,164,166,168,],[21,21,76,76,76,76,76,92,92,21,76,92,76,76,76,21,21,21,21,21,92,21,92,21,21,21,21,21,21,]),'booleano':([2,6,28,44,46,47,48,68,70,71,82,94,104,105,106,112,115,123,127,133,140,143,145,146,157,162,164,166,168,],[34,34,80,80,80,80,80,93,93,34,80,93,80,80,80,34,34,34,34,34,93,34,93,34,34,34,34,34,34,]),'operadorC':([21,76,92,],[46,106,106,]),'operadorM':([21,76,],[47,104,]),'operadorL':([21,76,92,],[48,105,105,]),'expresion':([28,44,46,47,48,82,104,105,106,],[75,84,86,87,88,107,119,120,121,]),'expresion_aritmetica':([28,44,46,47,48,82,104,105,106,],[77,77,77,77,77,77,77,77,77,]),'expresion_logica':([28,44,46,47,48,68,70,82,94,104,105,106,140,145,],[78,78,78,78,78,90,90,78,90,78,78,78,90,90,]),'expresion_comparativa':([28,44,46,47,48,68,70,82,94,104,105,106,140,145,],[79,79,79,79,79,91,91,79,91,79,79,79,91,91,]),'condicion':([68,70,94,140,145,],[89,97,113,152,155,]),'condicionalELSE':([124,142,169,175,],[132,153,173,176,]),'adicion':([125,],[135,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> phpSyntax","S'",1,None,None,None),
  ('phpSyntax -> inicio codigo fin','phpSyntax',3,'p_phpSyntax','php_parserLP.py',7),
  ('phpSyntax -> inicio fin','phpSyntax',2,'p_phpSyntax','php_parserLP.py',8),
  ('codigo -> algoritmo','codigo',1,'p_codigo','php_parserLP.py',13),
  ('codigo -> algoritmo codigo','codigo',2,'p_codigo','php_parserLP.py',14),
  ('codigo -> ','codigo',1,'p_codigo','php_parserLP.py',15),
  ('inicio -> INICIO','inicio',1,'p_inicio','php_parserLP.py',19),
  ('fin -> FIN','fin',1,'p_fin','php_parserLP.py',23),
  ('algoritmo -> asignacion','algoritmo',1,'p_algoritmo','php_parserLP.py',27),
  ('algoritmo -> declaracion','algoritmo',1,'p_algoritmo','php_parserLP.py',28),
  ('algoritmo -> comparacion','algoritmo',1,'p_algoritmo','php_parserLP.py',29),
  ('algoritmo -> condicionalIF','algoritmo',1,'p_algoritmo','php_parserLP.py',30),
  ('algoritmo -> iteracionFOR','algoritmo',1,'p_algoritmo','php_parserLP.py',31),
  ('algoritmo -> bucleWHILE','algoritmo',1,'p_algoritmo','php_parserLP.py',32),
  ('algoritmo -> bucleDO_WHILE','algoritmo',1,'p_algoritmo','php_parserLP.py',33),
  ('algoritmo -> indexacion','algoritmo',1,'p_algoritmo','php_parserLP.py',34),
  ('algoritmo -> echo','algoritmo',1,'p_algoritmo','php_parserLP.py',35),
  ('algoritmo -> terminar','algoritmo',1,'p_algoritmo','php_parserLP.py',36),
  ('asignacion -> ambito multiVariable IGUAL expresion PTOCO','asignacion',5,'p_asignacion','php_parserLP.py',40),
  ('asignacion -> multiVariable IGUAL expresion PTOCO','asignacion',4,'p_asignacion','php_parserLP.py',41),
  ('declaracion -> ambito multiVariable PTOCO','declaracion',3,'p_declaracion','php_parserLP.py',45),
  ('declaracion -> multiVariable PTOCO','declaracion',2,'p_declaracion','php_parserLP.py',46),
  ('multiVariable -> VARIABLE','multiVariable',1,'p_multiVariable','php_parserLP.py',50),
  ('multiVariable -> VARIABLE COMA multiVariable','multiVariable',3,'p_multiVariable','php_parserLP.py',51),
  ('ambito -> STATIC','ambito',1,'p_ambito','php_parserLP.py',55),
  ('ambito -> VAR','ambito',1,'p_ambito','php_parserLP.py',56),
  ('ambito -> GLOBAL','ambito',1,'p_ambito','php_parserLP.py',57),
  ('ambito -> CONST','ambito',1,'p_ambito','php_parserLP.py',58),
  ('comparacion -> valor operadorC expresion PTOCO','comparacion',4,'p_comparacion','php_parserLP.py',62),
  ('comparacion -> valor operadorM expresion PTOCO','comparacion',4,'p_comparacion','php_parserLP.py',63),
  ('comparacion -> valor operadorL expresion PTOCO','comparacion',4,'p_comparacion','php_parserLP.py',64),
  ('expresion -> valor','expresion',1,'p_expresion','php_parserLP.py',69),
  ('expresion -> expresion_aritmetica','expresion',1,'p_expresion','php_parserLP.py',70),
  ('expresion -> expresion_logica','expresion',1,'p_expresion','php_parserLP.py',71),
  ('expresion -> expresion_comparativa','expresion',1,'p_expresion','php_parserLP.py',72),
  ('expresion_aritmetica -> valor operadorM expresion','expresion_aritmetica',3,'p_expresion_aritmetica','php_parserLP.py',77),
  ('expresion_logica -> valor operadorL expresion','expresion_logica',3,'p_expresion_logica','php_parserLP.py',81),
  ('expresion_logica -> booleano','expresion_logica',1,'p_expresion_logica','php_parserLP.py',82),
  ('expresion_comparativa -> valor operadorC expresion','expresion_comparativa',3,'p_expresion_comparativa','php_parserLP.py',86),
  ('condicion -> expresion_logica','condicion',1,'p_condicion','php_parserLP.py',90),
  ('condicion -> expresion_comparativa','condicion',1,'p_condicion','php_parserLP.py',91),
  ('operadorM -> MAS','operadorM',1,'p_operadorM','php_parserLP.py',95),
  ('operadorM -> RESTA','operadorM',1,'p_operadorM','php_parserLP.py',96),
  ('operadorM -> PROD','operadorM',1,'p_operadorM','php_parserLP.py',97),
  ('operadorM -> DIV','operadorM',1,'p_operadorM','php_parserLP.py',98),
  ('operadorM -> MOD','operadorM',1,'p_operadorM','php_parserLP.py',99),
  ('operadorM -> POTENCIA','operadorM',1,'p_operadorM','php_parserLP.py',100),
  ('operadorC -> MAYOR','operadorC',1,'p_operadorC','php_parserLP.py',104),
  ('operadorC -> MENOR','operadorC',1,'p_operadorC','php_parserLP.py',105),
  ('operadorC -> COMPARACION','operadorC',1,'p_operadorC','php_parserLP.py',106),
  ('operadorC -> IDENTICO','operadorC',1,'p_operadorC','php_parserLP.py',107),
  ('operadorC -> DIFERENTE','operadorC',1,'p_operadorC','php_parserLP.py',108),
  ('operadorC -> NOIDENTICO','operadorC',1,'p_operadorC','php_parserLP.py',109),
  ('operadorC -> MENOROIGUAL','operadorC',1,'p_operadorC','php_parserLP.py',110),
  ('operadorC -> MAYOROIGUAL','operadorC',1,'p_operadorC','php_parserLP.py',111),
  ('operadorC -> NAVEESPACIAL','operadorC',1,'p_operadorC','php_parserLP.py',112),
  ('terminar -> BREAK PTOCO','terminar',2,'p_terminar','php_parserLP.py',116),
  ('operadorL -> AND','operadorL',1,'p_operadorL','php_parserLP.py',121),
  ('operadorL -> XOR','operadorL',1,'p_operadorL','php_parserLP.py',122),
  ('operadorL -> OR','operadorL',1,'p_operadorL','php_parserLP.py',123),
  ('operadorL -> NOT','operadorL',1,'p_operadorL','php_parserLP.py',124),
  ('valor -> INTEGER','valor',1,'p_valor','php_parserLP.py',129),
  ('valor -> booleano','valor',1,'p_valor','php_parserLP.py',130),
  ('valor -> STRING','valor',1,'p_valor','php_parserLP.py',131),
  ('valor -> FLOAT','valor',1,'p_valor','php_parserLP.py',132),
  ('valor -> VARIABLE','valor',1,'p_valor','php_parserLP.py',133),
  ('valor -> BOOLEAN','valor',1,'p_valor','php_parserLP.py',134),
  ('booleano -> TRUE','booleano',1,'p_booleano','php_parserLP.py',138),
  ('booleano -> FALSE','booleano',1,'p_booleano','php_parserLP.py',139),
  ('adicion -> MAS MAS VARIABLE','adicion',3,'p_incDec','php_parserLP.py',143),
  ('adicion -> MENOS MENOS VARIABLE','adicion',3,'p_incDec','php_parserLP.py',144),
  ('adicion -> VARIABLE MAS MAS','adicion',3,'p_incDec','php_parserLP.py',145),
  ('adicion -> VARIABLE MENOS MENOS','adicion',3,'p_incDec','php_parserLP.py',146),
  ('condicionalIF -> IF PIZQ condicion PDER LIZQ codigo LDER','condicionalIF',7,'p_condicionalIF','php_parserLP.py',150),
  ('condicionalIF -> IF PIZQ condicion PDER LIZQ codigo LDER condicionalELSE','condicionalIF',8,'p_condicionalIF','php_parserLP.py',151),
  ('condicionalIF -> IF PIZQ condicion PDER codigo','condicionalIF',5,'p_condicionalIF','php_parserLP.py',152),
  ('condicionalIF -> IF PIZQ condicion PDER codigo condicionalELSE','condicionalIF',6,'p_condicionalIF','php_parserLP.py',153),
  ('condicionalELSE -> ELSE LIZQ codigo LDER','condicionalELSE',4,'p_condicionalELSE','php_parserLP.py',157),
  ('condicionalELSE -> ELSEIF PIZQ condicion PDER LIZQ codigo LDER condicionalELSE','condicionalELSE',8,'p_condicionalELSE','php_parserLP.py',158),
  ('condicionalELSE -> ELSE codigo','condicionalELSE',2,'p_condicionalELSE','php_parserLP.py',159),
  ('condicionalELSE -> ELSEIF PIZQ condicion PDER codigo condicionalELSE','condicionalELSE',6,'p_condicionalELSE','php_parserLP.py',160),
  ('iteracionFOR -> FOR PIZQ asignacion condicion PTOCO adicion PDER codigo','iteracionFOR',8,'p_iteracionFOR','php_parserLP.py',164),
  ('iteracionFOR -> FOR PIZQ asignacion condicion PTOCO adicion PDER LIZQ codigo LDER','iteracionFOR',10,'p_iteracionFOR','php_parserLP.py',165),
  ('bucleWHILE -> WHILE PIZQ condicion PDER codigo','bucleWHILE',5,'p_bucleWHILE','php_parserLP.py',169),
  ('bucleWHILE -> WHILE PIZQ condicion PDER LIZQ codigo LDER','bucleWHILE',7,'p_bucleWHILE','php_parserLP.py',170),
  ('bucleDO_WHILE -> DO LIZQ codigo LDER WHILE PIZQ condicion PDER codigo','bucleDO_WHILE',9,'p_bucleDO_WHILE','php_parserLP.py',174),
  ('bucleDO_WHILE -> DO LIZQ codigo LDER WHILE PIZQ condicion PDER LIZQ codigo LDER','bucleDO_WHILE',11,'p_bucleDO_WHILE','php_parserLP.py',175),
  ('indexacion -> VARIABLE CIZQ INTEGER CDER','indexacion',4,'p_indexacion','php_parserLP.py',179),
  ('indexacion -> VARIABLE CIZQ RESTA INTEGER CDER','indexacion',5,'p_indexacion','php_parserLP.py',180),
  ('indexacion -> VARIABLE CIZQ INTEGER CDER FUSIONNULL','indexacion',5,'p_indexacion','php_parserLP.py',181),
  ('indexacion -> VARIABLE CIZQ RESTA INTEGER CDER FUSIONNULL','indexacion',6,'p_indexacion','php_parserLP.py',182),
  ('echo -> ECHO VARIABLE PTOCO','echo',3,'p_echo','php_parserLP.py',186),
  ('echo -> ECHO expresion PTOCO','echo',3,'p_echo','php_parserLP.py',187),
]
