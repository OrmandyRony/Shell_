import ply.yacc as yacc
# Obtener los tokens del lexer
from lexer import *
from Comands.command_mkdisk import *

precedence = ()

# Reglas Gramaticales
# Gustan que explique la gramatica
def p_init(t):
    'init : list_commands'
    t[0] = t[1]


# gramatica
def p_list_commands(t):
    '''list_commands : list_commands commands
                    | commands'''
    if len(t) != 2:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
    
def p_commands(t):
    '''commands : command_mkdisk
                | command_rmdisk'''
    t[0] = t[1]

def p_command_mkdisk(t):
    'command_mkdisk : MKDISK MAYOR_QUE UNIT'
    # t[0] : t[1] t[2] t[3]
    print(t[1])
    print(t[2])
    print(t[3])
    command_mkdisk_(t[1])
    t[0] = t[1]

def p_command_rmdisk(t):
    # recomendacion dejar el espacio
    'command_rmdisk : ENTERO  '
    print(t[1])
    #t[0] = t[1]

def prueba_archivo():
    print('------------------')
    ruta = '../test/EntradaFacil.ts'
    archivo = open(ruta, 'r')
    data = archivo.read()
    return data

# llevarla al main
def parse(input):
    global errors
    global parser
    parser = yacc.yacc()
    lexer.lineno = 1
    return parser.parse(input)

entrada = '''
mkdisk >unit
''' 
parse(entrada)