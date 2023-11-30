
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSUMRESleftPRDDIVAND COMA CORDER CORIZQ CRUZ CRUZ_V DER DIV DIVISION DIVISION_RESULTADO ID IGL IMPRIMIR INTGR LISTA_NUMS MAGNITUD MAG_V MEDIA MEDIANA MGN MODA MOSTRAR MULT MULTIPLICACION MULTIPLICACION_RESULTADO NORMALIZA NORM_V NUM PARDER PARIZQ PNTCOM PRC PRD PRINTER PRINTER_TEXTO PRP PUNT PUNTO RANGO RES RESTA RESTA_RESULTADO RES_V SUM SUMA SUMA_RESULTADO SUM_V TEXTO TOTAL VALI VARIANZAexpression : VALI PARIZQ ID PARDER PNTCOMexpression : SUMA_RESULTADO IGL SUM PUNT ID PUNT ID PNTCOMexpression : RESTA_RESULTADO IGL RES PUNT ID PUNT ID PNTCOMexpression : MULTIPLICACION_RESULTADO IGL MULT PUNT ID PUNT ID PNTCOMexpression : DIVISION_RESULTADO IGL DIV PUNT ID PUNT ID PNTCOMexpression : ID IGL CORIZQ NUM COMA NUM CORDER PNTCOMexpression : PRINTER PARIZQ TEXTO PARDER PNTCOMexpression : TOTAL IGL ID AND ID PNTCOMexpression : ID IGL LISTA_NUMSexpression : MEDIANA IGL MEDIANA PUNT ID PNTCOMexpression : MODA IGL MODA PUNT ID PNTCOMexpression : MOSTRAR PARIZQ MODA COMA MEDIA COMA MEDIANA COMA VARIANZA COMA RANGO PARDER PUNT ID PNTCOMexpression : MEDIA IGL MEDIA PUNT ID PNTCOMexpression : VARIANZA IGL VARIANZA PUNT ID PNTCOMexpression : RANGO IGL RANGO PUNT ID PNTCOMexpression : ID IGL NUM PNTCOMexpression : IMPRIMIR PARIZQ TEXTO PARDER PNTCOMexpression : IMPRIMIR PARIZQ CRUZ_V PARDER PNTCOMexpression : IMPRIMIR PARIZQ SUM_V PARDER PNTCOM'
    
_lr_action_items = {'VALI':([0,],[2,]),'SUMA_RESULTADO':([0,],[4,]),'RESTA_RESULTADO':([0,],[5,]),'MULTIPLICACION_RESULTADO':([0,],[6,]),'DIVISION_RESULTADO':([0,],[7,]),'ID':([0,17,24,54,55,56,57,59,60,61,63,64,65,87,88,89,90,114,],[3,32,41,71,72,73,74,76,77,78,80,81,82,99,100,101,102,115,]),'PRINTER':([0,],[8,]),'TOTAL':([0,],[9,]),'MEDIANA':([0,25,94,],[10,42,103,]),'MODA':([0,26,27,],[11,43,44,]),'MOSTRAR':([0,],[12,]),'MEDIA':([0,28,62,],[13,45,79,]),'VARIANZA':([0,29,109,],[14,46,110,]),'RANGO':([0,30,111,],[15,47,112,]),'IMPRIMIR':([0,],[16,]),'$end':([1,35,53,69,75,83,84,85,91,92,93,95,96,97,104,105,106,107,108,116,],[0,-9,-16,-1,-7,-17,-18,-19,-8,-10,-11,-13,-14,-15,-6,-2,-3,-4,-5,-12,]),'PARIZQ':([2,8,12,16,],[17,23,27,31,]),'IGL':([3,4,5,6,7,9,10,11,13,14,15,],[18,19,20,21,22,24,25,26,28,29,30,]),'CORIZQ':([18,],[33,]),'LISTA_NUMS':([18,],[35,]),'NUM':([18,33,70,],[34,52,86,]),'SUM':([19,],[36,]),'RES':([20,],[37,]),'MULT':([21,],[38,]),'DIV':([22,],[39,]),'TEXTO':([23,31,],[40,48,]),'CRUZ_V':([31,],[49,]),'SUM_V':([31,],[50,]),'PARDER':([32,40,48,49,50,112,],[51,58,66,67,68,113,]),'PNTCOM':([34,51,58,66,67,68,76,77,78,80,81,82,98,99,100,101,102,115,],[53,69,75,83,84,85,91,92,93,95,96,97,104,105,106,107,108,116,]),'PUNT':([36,37,38,39,42,43,45,46,47,71,72,73,74,113,],[54,55,56,57,60,61,63,64,65,87,88,89,90,114,]),'AND':([41,],[59,]),'COMA':([44,52,79,103,110,],[62,70,94,109,111,]),'CORDER':([86,],[98,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> VALI PARIZQ ID PARDER PNTCOM','expression',5,'p_expression_vali_id','main.py',12),
  ('expression -> SUMA_RESULTADO IGL SUM PUNT ID PUNT ID PNTCOM','expression',8,'p_suma_resultado','main.py',16),
  ('expression -> RESTA_RESULTADO IGL RES PUNT ID PUNT ID PNTCOM','expression',8,'p_resta_resultado','main.py',20),
  ('expression -> MULTIPLICACION_RESULTADO IGL MULT PUNT ID PUNT ID PNTCOM','expression',8,'p_multiplicacion_resultado','main.py',24),
  ('expression -> DIVISION_RESULTADO IGL DIV PUNT ID PUNT ID PNTCOM','expression',8,'p_division_resultado','main.py',28),
  ('expression -> ID IGL CORIZQ NUM COMA NUM CORDER PNTCOM','expression',8,'p_expression_id_add_num','main.py',32),
  ('expression -> PRINTER PARIZQ TEXTO PARDER PNTCOM','expression',5,'p_expression_printer_texto','main.py',36),
  ('expression -> TOTAL IGL ID AND ID PNTCOM','expression',6,'p_expression_total_assign_num_and_num','main.py',40),
  ('expression -> ID IGL LISTA_NUMS','expression',3,'p_expression_list_nums','main.py',44),
  ('expression -> MEDIANA IGL MEDIANA PUNT ID PNTCOM','expression',6,'p_expression_mediana','main.py',52),
  ('expression -> MODA IGL MODA PUNT ID PNTCOM','expression',6,'p_expression_moda','main.py',56),
  ('expression -> MOSTRAR PARIZQ MODA COMA MEDIA COMA MEDIANA COMA VARIANZA COMA RANGO PARDER PUNT ID PNTCOM','expression',15,'p_expression_mostrar_estadisticas','main.py',60),
  ('expression -> MEDIA IGL MEDIA PUNT ID PNTCOM','expression',6,'p_expression_media_assign','main.py',65),
  ('expression -> VARIANZA IGL VARIANZA PUNT ID PNTCOM','expression',6,'p_expression_varianza_assign','main.py',69),
  ('expression -> RANGO IGL RANGO PUNT ID PNTCOM','expression',6,'p_expression_rango_assign','main.py',73),
  ('expression -> ID IGL NUM PNTCOM','expression',4,'p_expression_id_assign_num','main.py',77),
  ('expression -> IMPRIMIR PARIZQ TEXTO PARDER PNTCOM','expression',5,'p_expression_imprimir','main.py',81),
  ('expression -> IMPRIMIR PARIZQ CRUZ_V PARDER PNTCOM','expression',5,'p_expression_imprimir_cruz_v','main.py',85),
  ('expression -> IMPRIMIR PARIZQ SUM_V PARDER PNTCOM','expression',5,'p_expression_imprimir_sum_v','main.py',89),
]
