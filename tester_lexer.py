# Siempre mandar a traer los token el lexer y lista de errores
from lexer import *

# Test
'''
rutas = ['./test/Asignaciones y Declaraciones/AsignacionDeclaraciones.ts', 
         './test/Asignaciones y Declaraciones/Alcance.ts',
         './test/Asignaciones y Declaraciones/AsignacionDeclaraciones.ts'
         ]
'''

def prueba_archivo(ruta):
    print('------------------')
    print(ruta)
    archivo = open(ruta, 'r')
    data = archivo.read()
  

def pruebas_archivos():
    rutas = ['./test/GeneraTest.ts']

    for ruta in rutas:
        print('------------------')
        print(ruta)
        archivo = open(ruta, 'r')
        data = archivo.read()
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok: 
                break      # No more input
            print(tok.type, tok.value, tok.lineno, tok.lexpos)
        archivo.close()
        print('------------------')

    # Print errors
    print('--------- Errors ---------')
    for error in errors:
        print(error)

def prueba_normal(input):
    lexer.input(input)
    while True:
        tok = lexer.token()
        if not tok:  # manejar errores lexicos
            break      # No more input
        print(tok.type, tok.value, tok.lineno, tok.lexpos)

entrada = '''
mkdisk 
 
'''

prueba_normal(entrada)