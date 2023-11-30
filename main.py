import p
import ply.yacc as yacc
from lexer import tokens

# Reglas de precedencia
precedence = (
    ('left', 'SUM', 'RES'),
    ('left', 'PRD', 'DIV'),
)

def p_expression_vali_id(p):
    """expression : VALI PARIZQ ID PARDER PNTCOM"""
    p[0] = ('VALI_ID', p[3], p[5])

def p_suma_resultado(p):
    """expression : SUMA_RESULTADO IGL SUM PUNT ID PUNT ID PNTCOM"""
    p[0] = ('SUMA_RESULTADO', p[3], p[5], p[7])

def p_resta_resultado(p):
    """expression : RESTA_RESULTADO IGL RES PUNT ID PUNT ID PNTCOM"""
    p[0] = ('RESTA_RESULTADO', p[3], p[5], p[7])

def p_multiplicacion_resultado(p):
    """expression : MULTIPLICACION_RESULTADO IGL MULT PUNT ID PUNT ID PNTCOM"""
    p[0] = ('MULTIPLICACION_RESULTADO', p[3], p[5], p[7])

def p_division_resultado(p):
    """expression : DIVISION_RESULTADO IGL DIV PUNT ID PUNT ID PNTCOM"""
    p[0] = ('DIVISION_RESULTADO', p[3], p[5], p[7])

def p_expression_id_add_num(p):
    """expression : ID IGL CORIZQ NUM COMA NUM CORDER PNTCOM"""
    p[0] = ('ID_ADD_NUM', p[1], p[5], p[7])

def p_expression_printer_texto(p):
    """expression : PRINTER PARIZQ TEXTO PARDER PNTCOM"""
    p[0] = ('PRINTER_TEXTO', p[3])

def p_expression_total_assign_num_and_num(p):
    """expression : TOTAL IGL ID AND ID PNTCOM"""
    p[0] = ('TOTAL_ASSIGN_NUM_AND_NUM', p[1], p[4], p[5])

def p_expression_list_nums(p):
    """expression : ID IGL LISTA_NUMS"""
    p[0] = ('ASIGNACION_LISTA_NUMS', p[1], p[3])

def p_expression_id_assign_num(p):
    """expression : ID IGL NUM PNTCOM"""
    p[0] = ('ID_ASSIGN_NUM', p[1], p[3], p[4], p[5])

def p_expression_mediana(p):
    """expression : MEDIANA IGL MEDIANA PUNT ID PNTCOM"""
    p[0] = ('MEDIANA_ASSIGN_EXPRESSION', p[1], p[3], p[5])

def p_expression_moda(p):
    """expression : MODA IGL MODA PUNT ID PNTCOM"""
    p[0] = ('MODA_EXPRESSION', p[1], p[3], p[5])

def p_expression_mostrar_estadisticas(p):
    """expression : MOSTRAR PARIZQ MODA COMA MEDIA COMA MEDIANA COMA VARIANZA COMA RANGO PARDER PUNT ID PNTCOM"""
    p[0] = ('MOSTRAR_ESTADISTICAS', p[3], p[5], p[7], p[9], p[11], p[14])


def p_expression_media_assign(p):
    """expression : MEDIA IGL MEDIA PUNT ID PNTCOM"""
    p[0] = ('MEDIA_ASSIGN_EXPRESSION', p[1], p[3], p[5])

def p_expression_varianza_assign(p):
    """expression : VARIANZA IGL VARIANZA PUNT ID PNTCOM"""
    p[0] = ('VARIANZA_ASSIGN_EXPRESSION', p[1], p[3], p[5])

def p_expression_rango_assign(p):
    """expression : RANGO IGL RANGO PUNT ID PNTCOM"""
    p[0] = ('RANGO_ASSIGN_EXPRESSION', p[1], p[3], p[5])

def p_expression_id_assign_num(p):
    """expression : ID IGL NUM PNTCOM"""
    p[0] = ('ID_ASSIGN_NUM', p[1], p[4])

def p_expression_imprimir(p):
    """expression : IMPRIMIR PARIZQ TEXTO PARDER PNTCOM"""
    p[0] = ('IMPRIMIR', p[3])

def p_expression_imprimir_cruz_v(p):
    """expression : IMPRIMIR PARIZQ CRUZ_V PARDER PNTCOM"""
    p[0] = ('IMPRIMIR_CRUZ', ('CRUZ_V',))

def p_expression_imprimir_sum_v(p):
    """expression : IMPRIMIR PARIZQ SUM_V PARDER PNTCOM"""
    p[0] = ('IMPRIMIR_SUM_V', ('SUM_V',))

# ERRORRES DE SINTAXIS
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
while True:
    try:
        s = input('')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
