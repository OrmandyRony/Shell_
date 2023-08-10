# import ply
import ply.lex as lex
# Lista de errores
errors = []

# palabras reservadas
reserved_words = {
    # Manage disk
    # MKDISK -> mkdisk >size=3000 >unit=K >path=”/home/user/Disco1.dsk”
    # patron : token que recibimos en analizador lexico
    'mkdisk' : 'MKDISK', # es por convencion 

    # Comand
    '>size': 'SIZE',
    'unit': 'UNIT',
    '>path': 'PATH',

    #Parametros
    'K': 'KILOBYTE'

    #Valores
}

# Lista de tokens GLOBAL tokens es una palabra del analizador
tokens = [
   'ENTERO',
   'CADENA',
   'ID',
   'IGUAL',
   'MAYOR_QUE'
] + list(reserved_words.values())

# Expresiones regulares para tokens simples
t_IGUAL = r'\=' 
t_MAYOR_QUE = r'\>'

# Expresiones regulares con acciones de codigo 55 
# todo ingresa como un string  "55" int(55) 
def t_ENTERO(t):
    r'd+'
    t.value = int(t.value)
    return

#  Cadena 
def t_CADENA(t):
    r'\"(.|\n)*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

#  ID mkdir -> ID mkdisk
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_words.get(t.value, 'ID') 
    return t

# New line
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#  Caracteres ignorados
t_ignore = ' \t'

def t_error(t):
    errors.append(t.value[0])
    print(f'Caracter no reconocido: {t.value[0]} en la linea {t.lexer.lineno}')
    t.lexer.skip(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

lexer = lex.lex()