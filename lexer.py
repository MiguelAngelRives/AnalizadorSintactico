import ply.lex as lex

Reservadas = (
    # LISTA DE PALABRAS RESERVADAS
    'MEDIANA', 'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 'PUNTO', 'CRUZ', 'MAGNITUD',
    'NORMALIZA', 'IMPRIMIR', 'VALI', 'MODA', 'MEDIA', 'VARIANZA', 'RANGO', 'MOSTRAR',
    'SUMA_RESULTADO', 'RESTA_RESULTADO', 'MULTIPLICACION_RESULTADO', 'DIVISION_RESULTADO', 'PRINTER', 'PRINTER_TEXTO'
)

Operadores = (
    # OPERADORES
    'SUM', 'PRD', 'IGL', 'DIV',
    'MGN', 'PRP', 'INTGR', 'DER', 'RES', 'PRC', 'PUNT', 'TOTAL', 'MULT'
)
Funciones = (
    # FUNCIONES
    'RES_V', 'MAG_V',
    'NORM_V', 'CRUZ_V', 'SUM_V', 'AND'
)
Otros = (
    # OTROS
    'NUM', 'PARIZQ', 'PARDER', 'CORIZQ',
    'CORDER', 'PNTCOM', 'TEXTO', 'COMA', 'ID', 'LISTA_NUMS'
)
tokens = Reservadas + Operadores + Funciones + Otros
t_ignore = " \t"

def get_token_category(token_value):
    if token_value in Reservadas:
        return 'Reservadas'
    elif token_value in Operadores:
        return 'Operadores'
    elif token_value in Funciones:
        return 'Funciones'
    elif token_value in Otros:
        return 'Otros'
    else:
        return 'Desconocido'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_LISTA_NUMS(t):
    r'\[([a-zA-Z],?\s*)+\];'
    t.value = t.value[1:-2]  # Para eliminar corchetes y punto y coma
    return t

def t_error(t):
    print(chr(27) + "[1;31m" + "\t ERROR: Illegal character" + chr(27) + "[0m")
    print("\t\tLine: " + str(t.lexer.lineno) + "\t=> " + t.value[0])
    t.lexer.skip(1)

# LISTA DE PALABRAS RESERVADAS
def t_MEDIANA(t):
    r'MEDIANA'
    return t

def t_TOTAL(t):
    r'\bTOTAL\b'
    return t

def t_MOSTRAR(t):
    r'MOSTRAR'
    return t

# Agregar la palabra reservada 'PRINTER'
def t_PRINTER(t):
    r'\bPRINTER\b'
    return t

# Agregar la regla para capturar el texto dentro de paréntesis
def t_PRINTER_TEXTO(t):
    r'PRINTER\s*\(\s*\"[^\"]*\"\s*\);'
    return t

def t_SUMA_RESULTADO(t):
    r'\bSUMA_RESULTADO\b'
    return t

def t_RESTA_RESULTADO(t):
    r'RESTA_RESULTADO'
    return t

def t_MULTIPLICACION_RESULTADO(t):
    r'\bMULTIPLICACION_RESULTADO\b'
    return t

def t_DIVISION_RESULTADO(t):
    r'DIVISION_RESULTADO'
    return t

def t_SUMA(t):
    r'\bSUMA\b'
    return t

def t_RESTA(t):
    r'\bRESTA\b'
    return t

def t_MULTIPLICA(t):
    r'\bMULTIPLICA\b'
    return t

def t_PUNTO(t):
    r'\bPUNTO\b'
    return t

def t_CRUZ(t):
    r'\bCRUZ\b'
    return t

def t_MODA(t):
    r'MODA'
    return t

def t_MEDIA(t):
    r'MEDIA'
    return t

def t_VARIANZA(t):
    r'VARIANZA'
    return t

def t_RANGO(t):
    r'RANGO'
    return t

def t_MAGNITUD(t):
    r'\bMAGNITUD\b'
    return t

def t_NORMALIZA(t):
    r'\bNORMALIZA\b'
    return t

def t_ANGULO(t):
    r'\bANGULO\b'
    return t

def t_IMPRIMIR(t):
    r'\bIMPRIMIR\b'
    return t

def t_VALI(t):
    r'\bVALI\b'
    return t

def t_AND(t):
    r'\b&\b'
    return t

def t_MULT(t):
    r'MULT'
    return t

# OPERADORES
t_SUM = r'\+'
t_PRD = r'\*'
t_IGL = r'\='
t_DIV = r'\/'
t_MGN = r'\|A\|'
t_INTGR = r'//'
t_DER = r'<>'
t_RES = r'-'
t_PRC = r'><'
t_PUNT = r'.'

# OTROS
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_PNTCOM = r'\;'
t_COMA = r'\,'
t_TEXTO = r'\".*\"'

def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(\w\d)*'
    if t.value in Reservadas:
        t.type = t.value
    elif t.value in Operadores:
        t.type = t.value
    elif t.value in Funciones:
        t.type = t.value
    else:
        t.type = 'ID'
    return t


lexer = lex.lex()