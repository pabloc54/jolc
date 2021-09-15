
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftop_rangorightop_ternarialeftorleftandleftigualaciondiferenciacionleftmenormenor_igualmayormayor_igualleftmasmenosleftasteriscobarramodulorightcaretrightop_negacionnotleftop_llamadaleftop_accesononassocop_agrupacionBool Char Float64 Int64 Nothing String and asterisco barra bool break caret char coma continue corA corB diferenciacion dospuntos else elseif end float64 for function global id if igual igualacion in int64 interrog llaveA llaveB local mas mayor mayor_igual menor menor_igual menos modulo mutable not or parA parB punto puntoycoma return string struct tipo while\n  INS : INS I puntoycoma\n      | I puntoycoma\n  \n  INS : INS error puntoycoma\n      | error puntoycoma\n  \n  I : ASIGNACION\n    | FUNCION\n    | STRUCT\n    | LLAMADA\n    | IF\n    | WHILE\n    | FOR\n    | BREAK\n    | CONTINUE\n    | RETURN\n  \n  BLOQUE  : INS end\n  \n  BLOQUE_ABIERTO  : INS\n  \n  TIPO  : Int64\n        | Float64\n        | Bool\n        | Char\n        | String\n  \n  SCOPE : local\n        | global\n  \n  ASIGNACION  : ID igual ASIGNACION_VALOR\n              | SCOPE id igual ASIGNACION_VALOR\n              | SCOPE id\n  \n  ASIGNACION_VALOR  : E\n                    | E tipo TIPO\n  \n  ID  : ID punto id\n      | ID corA E corB\n      | id\n  \n  FUNCION : function id parA PAR parB BLOQUE\n          | function id parA parB BLOQUE\n  \n  PAR : PAR coma P\n      | P\n  \n  P : id\n  \n  STRUCT  : struct id ATR end\n          | mutable struct id ATR end\n  \n  ATR : ATR A\n      | A\n  \n  A : id tipo TIPO puntoycoma\n    | id puntoycoma\n  \n  EXP : EXP coma E\n      | E\n  \n  E : E mas E\n    | E menos E\n    | E asterisco E\n    | E barra E\n    | E caret E\n    | E modulo E\n    | menos E                     %prec op_negacion\n    | E mayor E\n    | E menor E\n    | E mayor_igual E\n    | E menor_igual E\n    | E igualacion E\n    | E diferenciacion E\n    | E or E\n    | E and E\n    | not E\n    | E interrog E dospuntos E  %prec op_ternaria\n    | ID                        %prec op_acceso\n    | parA E parB               %prec op_agrupacion\n    | LLAMADA                   %prec op_llamada\n    | RANGO                     %prec op_rango\n    | ARREGLO\n    | int64\n    | float64\n    | bool\n    | char\n    | STRING\n    | Nothing\n  \n  STRING  : STRING S\n          | S\n  \n  S : string\n    | llaveA E llaveB\n  \n  ARREGLO : corA EXP corB\n          | corA corB\n  \n  LLAMADA : id parA EXP parB\n          | id parA parB\n  \n  IF  : if E BLOQUE\n      | if E BLOQUE_ABIERTO ELSE\n      | if E BLOQUE_ABIERTO ELSEIF\n  \n  ELSEIF  : elseif E BLOQUE\n          | elseif E BLOQUE_ABIERTO ELSEIF\n          | elseif E BLOQUE_ABIERTO ELSE\n  \n  ELSE : else BLOQUE\n  \n  WHILE : while E BLOQUE\n  \n  FOR : for id in E BLOQUE\n  \n  RANGO : E dospuntos E\n        | dospuntos\n  \n  BREAK : break\n  \n  CONTINUE : continue\n  \n  RETURN  : return E\n          | return\n  '
    
_lr_action_items = {'error':([0,1,30,31,40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,63,64,67,71,96,97,98,100,102,105,108,110,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,145,153,159,167,],[3,29,-2,-4,3,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,3,-1,-3,-29,-80,29,-51,-60,-73,-78,29,-30,-79,3,3,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,3,3,3,-61,]),'function':([0,1,30,31,40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,63,64,67,71,96,97,98,100,102,105,108,110,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,145,153,159,167,],[17,17,-2,-4,17,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,17,-1,-3,-29,-80,17,-51,-60,-73,-78,17,-30,-79,17,17,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,17,17,17,-61,]),'struct':([0,1,19,30,31,40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,63,64,67,71,96,97,98,100,102,105,108,110,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,145,153,159,167,],[18,18,39,-2,-4,18,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,18,-1,-3,-29,-80,18,-51,-60,-73,-78,18,-30,-79,18,18,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,18,18,18,-61,]),'mutable':([0,1,30,31,40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,63,64,67,71,96,97,98,100,102,105,108,110,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,145,153,159,167,],[19,19,-2,-4,19,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,19,-1,-3,-29,-80,19,-51,-60,-73,-78,19,-30,-79,19,19,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,19,19,19,-61,]),'id':([0,1,15,17,18,20,21,22,25,26,27,30,31,32,33,34,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,67,69,71,73,75,76,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,105,106,108,110,111,114,117,119,120,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,145,153,154,159,160,164,167,],[16,16,35,37,38,55,55,61,55,-22,-23,-2,-4,55,67,55,55,74,77,16,55,55,-91,-62,55,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,55,-74,-75,55,16,-1,-3,-29,55,-80,112,74,-40,74,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,16,-51,-60,-73,-78,16,55,-30,-79,55,16,-42,-39,74,16,55,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,16,16,112,16,55,-41,-61,]),'if':([0,1,30,31,40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,63,64,67,71,96,97,98,100,102,105,108,110,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,145,153,159,167,],[20,20,-2,-4,20,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,20,-1,-3,-29,-80,20,-51,-60,-73,-78,20,-30,-79,20,20,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,20,20,20,-61,]),'while':([0,1,30,31,40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,63,64,67,71,96,97,98,100,102,105,108,110,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,145,153,159,167,],[21,21,-2,-4,21,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,21,-1,-3,-29,-80,21,-51,-60,-73,-78,21,-30,-79,21,21,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,21,21,21,-61,]),'for':([0,1,30,31,40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,63,64,67,71,96,97,98,100,102,105,108,110,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,145,153,159,167,],[22,22,-2,-4,22,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,22,-1,-3,-29,-80,22,-51,-60,-73,-78,22,-30,-79,22,22,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,22,22,22,-61,]),'break':([0,1,30,31,40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,63,64,67,71,96,97,98,100,102,105,108,110,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,145,153,159,167,],[23,23,-2,-4,23,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,23,-1,-3,-29,-80,23,-51,-60,-73,-78,23,-30,-79,23,23,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,23,23,23,-61,]),'continue':([0,1,30,31,40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,63,64,67,71,96,97,98,100,102,105,108,110,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,145,153,159,167,],[24,24,-2,-4,24,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,24,-1,-3,-29,-80,24,-51,-60,-73,-78,24,-30,-79,24,24,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,24,24,24,-61,]),'return':([0,1,30,31,40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,63,64,67,71,96,97,98,100,102,105,108,110,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,145,153,159,167,],[25,25,-2,-4,25,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,25,-1,-3,-29,-80,25,-51,-60,-73,-78,25,-30,-79,25,25,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,25,25,25,-61,]),'local':([0,1,30,31,40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,63,64,67,71,96,97,98,100,102,105,108,110,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,145,153,159,167,],[26,26,-2,-4,26,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,26,-1,-3,-29,-80,26,-51,-60,-73,-78,26,-30,-79,26,26,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,26,26,26,-61,]),'global':([0,1,30,31,40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,63,64,67,71,96,97,98,100,102,105,108,110,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,145,153,159,167,],[27,27,-2,-4,27,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,27,-1,-3,-29,-80,27,-51,-60,-73,-78,27,-30,-79,27,27,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,27,27,27,-61,]),'$end':([1,30,31,63,64,],[0,-2,-4,-1,-3,]),'puntoycoma':([2,3,4,5,6,7,8,9,10,11,12,13,23,24,25,28,29,35,43,44,46,47,48,49,50,51,52,53,54,55,57,58,62,65,66,67,71,74,78,97,98,100,102,104,108,109,110,118,121,122,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,141,142,143,144,146,147,148,149,150,151,155,156,157,158,161,162,165,167,168,169,],[30,31,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-92,-93,-95,63,64,-26,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,-94,-24,-27,-29,-80,117,-81,-51,-60,-73,-78,-88,-30,-25,-79,-37,-82,-83,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-15,-63,-77,-76,-28,-17,-18,-19,-20,-21,-33,164,-38,-87,-89,-32,-84,-61,-85,-86,]),'igual':([14,16,35,67,108,],[32,-31,69,-29,-30,]),'punto':([14,16,44,55,67,108,],[33,-31,33,-31,-29,-30,]),'corA':([14,16,20,21,25,32,34,36,41,42,44,45,55,56,59,67,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,106,108,111,124,160,],[34,-31,56,56,56,56,56,56,56,56,34,56,-31,56,56,-29,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-30,56,56,56,]),'parA':([16,20,21,25,32,34,36,37,41,42,45,55,56,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,106,111,124,160,],[36,45,45,45,45,45,45,73,45,45,45,36,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'menos':([20,21,25,32,34,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,66,67,68,69,71,72,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,102,103,106,108,110,111,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,160,167,],[41,41,41,41,41,41,81,41,41,-91,-62,41,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,41,-74,-75,41,81,81,81,-29,81,41,-80,81,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-51,-60,81,-73,-78,81,41,-30,-79,41,41,-45,-46,-47,-48,-49,-50,81,81,81,81,81,81,81,81,81,81,-63,-77,-76,81,81,81,41,81,]),'not':([20,21,25,32,34,36,41,42,45,56,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,106,111,124,160,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'int64':([20,21,25,32,34,36,41,42,45,56,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,106,111,124,160,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'float64':([20,21,25,32,34,36,41,42,45,56,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,106,111,124,160,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'bool':([20,21,25,32,34,36,41,42,45,56,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,106,111,124,160,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'char':([20,21,25,32,34,36,41,42,45,56,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,106,111,124,160,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'Nothing':([20,21,25,32,34,36,41,42,45,56,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,106,111,124,160,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'dospuntos':([20,21,25,32,34,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,66,67,68,69,71,72,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,102,103,106,108,110,111,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,160,167,],[43,43,43,43,43,43,95,43,43,-91,-62,43,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,43,-74,-75,43,95,95,95,-29,95,43,-80,95,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-51,-60,95,-73,-78,95,43,-30,-79,43,43,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,160,95,-63,-77,-76,95,95,95,43,-61,]),'string':([20,21,25,32,34,36,41,42,45,53,56,57,58,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,100,106,111,124,144,160,],[58,58,58,58,58,58,58,58,58,58,58,-74,-75,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,-73,58,58,58,-76,58,]),'llaveA':([20,21,25,32,34,36,41,42,45,53,56,57,58,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,100,106,111,124,144,160,],[59,59,59,59,59,59,59,59,59,59,59,-74,-75,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-73,59,59,59,-76,59,]),'end':([30,31,63,64,75,76,96,105,117,119,120,164,],[-2,-4,-1,-3,118,-40,141,141,-42,-39,157,-41,]),'else':([30,31,63,64,79,96,166,],[-2,-4,-1,-3,123,-16,123,]),'elseif':([30,31,63,64,79,96,166,],[-2,-4,-1,-3,124,-16,124,]),'parB':([36,43,44,46,47,48,49,50,51,52,53,54,55,57,58,67,70,71,72,73,97,98,99,100,102,108,110,112,113,115,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,152,163,167,],[71,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,-29,110,-80,-44,114,-51,-60,142,-73,-78,-30,-79,-36,153,-35,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,-43,-34,-61,]),'mas':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[80,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,80,80,80,-29,80,-80,80,-51,-60,80,-73,-78,80,-30,-79,-45,-46,-47,-48,-49,-50,80,80,80,80,80,80,80,80,80,80,-63,-77,-76,80,80,80,80,]),'asterisco':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[82,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,82,82,82,-29,82,-80,82,-51,-60,82,-73,-78,82,-30,-79,82,82,-47,-48,-49,-50,82,82,82,82,82,82,82,82,82,82,-63,-77,-76,82,82,82,82,]),'barra':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[83,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,83,83,83,-29,83,-80,83,-51,-60,83,-73,-78,83,-30,-79,83,83,-47,-48,-49,-50,83,83,83,83,83,83,83,83,83,83,-63,-77,-76,83,83,83,83,]),'caret':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[84,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,84,84,84,-29,84,-80,84,-51,-60,84,-73,-78,84,-30,-79,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,-63,-77,-76,84,84,84,84,]),'modulo':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[85,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,85,85,85,-29,85,-80,85,-51,-60,85,-73,-78,85,-30,-79,85,85,-47,-48,-49,-50,85,85,85,85,85,85,85,85,85,85,-63,-77,-76,85,85,85,85,]),'mayor':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[86,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,86,86,86,-29,86,-80,86,-51,-60,86,-73,-78,86,-30,-79,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,86,86,86,86,86,86,-63,-77,-76,86,86,86,86,]),'menor':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[87,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,87,87,87,-29,87,-80,87,-51,-60,87,-73,-78,87,-30,-79,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,87,87,87,87,87,87,-63,-77,-76,87,87,87,87,]),'mayor_igual':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[88,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,88,88,88,-29,88,-80,88,-51,-60,88,-73,-78,88,-30,-79,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,88,88,88,88,88,88,-63,-77,-76,88,88,88,88,]),'menor_igual':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[89,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,89,89,89,-29,89,-80,89,-51,-60,89,-73,-78,89,-30,-79,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,89,89,89,89,89,89,-63,-77,-76,89,89,89,89,]),'igualacion':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[90,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,90,90,90,-29,90,-80,90,-51,-60,90,-73,-78,90,-30,-79,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,90,90,90,90,-63,-77,-76,90,90,90,90,]),'diferenciacion':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[91,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,91,91,91,-29,91,-80,91,-51,-60,91,-73,-78,91,-30,-79,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,91,91,91,91,-63,-77,-76,91,91,91,91,]),'or':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[92,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,92,92,92,-29,92,-80,92,-51,-60,92,-73,-78,92,-30,-79,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,92,92,-63,-77,-76,92,92,92,92,]),'and':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[93,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,93,93,93,-29,93,-80,93,-51,-60,93,-73,-78,93,-30,-79,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,93,-59,93,93,-63,-77,-76,93,93,93,93,]),'interrog':([40,43,44,46,47,48,49,50,51,52,53,54,55,57,58,60,62,66,67,68,71,72,97,98,99,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,142,143,144,145,152,159,167,],[94,-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,94,94,94,-29,94,-80,94,-51,-60,94,-73,-78,94,-30,-79,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,94,94,-63,-77,-76,94,94,94,-61,]),'tipo':([43,44,46,47,48,49,50,51,52,53,54,55,57,58,66,67,71,74,97,98,100,102,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,167,],[-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,107,-29,-80,116,-51,-60,-73,-78,-30,-79,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,-61,]),'corB':([43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,67,68,71,72,97,98,100,101,102,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,152,167,],[-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,102,-74,-75,-29,108,-80,-44,-51,-60,-73,143,-78,-30,-79,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,-43,-61,]),'coma':([43,44,46,47,48,49,50,51,52,53,54,55,57,58,67,70,71,72,97,98,100,101,102,108,110,112,113,115,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,152,163,167,],[-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,-29,111,-80,-44,-51,-60,-73,111,-78,-30,-79,-36,154,-35,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,-43,-34,-61,]),'llaveB':([43,44,46,47,48,49,50,51,52,53,54,55,57,58,67,71,97,98,100,102,103,108,110,125,126,127,128,129,130,131,132,133,134,135,136,137,138,140,142,143,144,167,],[-91,-62,-64,-65,-66,-67,-68,-69,-70,-71,-72,-31,-74,-75,-29,-80,-51,-60,-73,-78,144,-30,-79,-45,-46,-47,-48,-49,-50,-52,-53,-54,-55,-56,-57,-58,-59,-90,-63,-77,-76,-61,]),'in':([61,],[106,]),'Int64':([107,116,],[147,147,]),'Float64':([107,116,],[148,148,]),'Bool':([107,116,],[149,149,]),'Char':([107,116,],[150,150,]),'String':([107,116,],[151,151,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INS':([0,40,60,114,123,145,153,159,],[1,96,105,105,105,105,105,96,]),'I':([0,1,40,60,96,105,114,123,145,153,159,],[2,28,2,2,28,28,2,2,2,2,2,]),'ASIGNACION':([0,1,40,60,96,105,114,123,145,153,159,],[4,4,4,4,4,4,4,4,4,4,4,]),'FUNCION':([0,1,40,60,96,105,114,123,145,153,159,],[5,5,5,5,5,5,5,5,5,5,5,]),'STRUCT':([0,1,40,60,96,105,114,123,145,153,159,],[6,6,6,6,6,6,6,6,6,6,6,]),'LLAMADA':([0,1,20,21,25,32,34,36,40,41,42,45,56,59,60,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,105,106,111,114,123,124,145,153,159,160,],[7,7,46,46,46,46,46,46,7,46,46,46,46,46,7,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,7,7,46,46,7,7,46,7,7,7,46,]),'IF':([0,1,40,60,96,105,114,123,145,153,159,],[8,8,8,8,8,8,8,8,8,8,8,]),'WHILE':([0,1,40,60,96,105,114,123,145,153,159,],[9,9,9,9,9,9,9,9,9,9,9,]),'FOR':([0,1,40,60,96,105,114,123,145,153,159,],[10,10,10,10,10,10,10,10,10,10,10,]),'BREAK':([0,1,40,60,96,105,114,123,145,153,159,],[11,11,11,11,11,11,11,11,11,11,11,]),'CONTINUE':([0,1,40,60,96,105,114,123,145,153,159,],[12,12,12,12,12,12,12,12,12,12,12,]),'RETURN':([0,1,40,60,96,105,114,123,145,153,159,],[13,13,13,13,13,13,13,13,13,13,13,]),'ID':([0,1,20,21,25,32,34,36,40,41,42,45,56,59,60,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,105,106,111,114,123,124,145,153,159,160,],[14,14,44,44,44,44,44,44,14,44,44,44,44,44,14,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,14,14,44,44,14,14,44,14,14,14,44,]),'SCOPE':([0,1,40,60,96,105,114,123,145,153,159,],[15,15,15,15,15,15,15,15,15,15,15,]),'E':([20,21,25,32,34,36,41,42,45,56,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,106,111,124,160,],[40,60,62,66,68,72,97,98,99,72,103,66,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,145,152,159,167,]),'RANGO':([20,21,25,32,34,36,41,42,45,56,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,106,111,124,160,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'ARREGLO':([20,21,25,32,34,36,41,42,45,56,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,106,111,124,160,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'STRING':([20,21,25,32,34,36,41,42,45,56,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,106,111,124,160,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'S':([20,21,25,32,34,36,41,42,45,53,56,59,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,106,111,124,160,],[57,57,57,57,57,57,57,57,57,100,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'ASIGNACION_VALOR':([32,69,],[65,109,]),'EXP':([36,56,],[70,101,]),'ATR':([38,77,],[75,120,]),'A':([38,75,77,120,],[76,119,76,119,]),'BLOQUE':([40,60,114,123,145,153,159,],[78,104,155,158,161,162,165,]),'BLOQUE_ABIERTO':([40,159,],[79,166,]),'PAR':([73,],[113,]),'P':([73,154,],[115,163,]),'ELSE':([79,166,],[121,169,]),'ELSEIF':([79,166,],[122,168,]),'TIPO':([107,116,],[146,156,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INS","S'",1,None,None,None),
  ('INS -> INS I puntoycoma','INS',3,'p_INS','analyzer.py',233),
  ('INS -> I puntoycoma','INS',2,'p_INS','analyzer.py',234),
  ('INS -> INS error puntoycoma','INS',3,'p_INS_error','analyzer.py',244),
  ('INS -> error puntoycoma','INS',2,'p_INS_error','analyzer.py',245),
  ('I -> ASIGNACION','I',1,'p_I','analyzer.py',251),
  ('I -> FUNCION','I',1,'p_I','analyzer.py',252),
  ('I -> STRUCT','I',1,'p_I','analyzer.py',253),
  ('I -> LLAMADA','I',1,'p_I','analyzer.py',254),
  ('I -> IF','I',1,'p_I','analyzer.py',255),
  ('I -> WHILE','I',1,'p_I','analyzer.py',256),
  ('I -> FOR','I',1,'p_I','analyzer.py',257),
  ('I -> BREAK','I',1,'p_I','analyzer.py',258),
  ('I -> CONTINUE','I',1,'p_I','analyzer.py',259),
  ('I -> RETURN','I',1,'p_I','analyzer.py',260),
  ('BLOQUE -> INS end','BLOQUE',2,'p_BLOQUE','analyzer.py',266),
  ('BLOQUE_ABIERTO -> INS','BLOQUE_ABIERTO',1,'p_BLOQUE_ABIERTO','analyzer.py',272),
  ('TIPO -> Int64','TIPO',1,'p_TIPO','analyzer.py',278),
  ('TIPO -> Float64','TIPO',1,'p_TIPO','analyzer.py',279),
  ('TIPO -> Bool','TIPO',1,'p_TIPO','analyzer.py',280),
  ('TIPO -> Char','TIPO',1,'p_TIPO','analyzer.py',281),
  ('TIPO -> String','TIPO',1,'p_TIPO','analyzer.py',282),
  ('SCOPE -> local','SCOPE',1,'p_SCOPE','analyzer.py',288),
  ('SCOPE -> global','SCOPE',1,'p_SCOPE','analyzer.py',289),
  ('ASIGNACION -> ID igual ASIGNACION_VALOR','ASIGNACION',3,'p_ASIGNACION','analyzer.py',295),
  ('ASIGNACION -> SCOPE id igual ASIGNACION_VALOR','ASIGNACION',4,'p_ASIGNACION','analyzer.py',296),
  ('ASIGNACION -> SCOPE id','ASIGNACION',2,'p_ASIGNACION','analyzer.py',297),
  ('ASIGNACION_VALOR -> E','ASIGNACION_VALOR',1,'p_ASIGNACION_VALOR','analyzer.py',316),
  ('ASIGNACION_VALOR -> E tipo TIPO','ASIGNACION_VALOR',3,'p_ASIGNACION_VALOR','analyzer.py',317),
  ('ID -> ID punto id','ID',3,'p_ID','analyzer.py',326),
  ('ID -> ID corA E corB','ID',4,'p_ID','analyzer.py',327),
  ('ID -> id','ID',1,'p_ID','analyzer.py',328),
  ('FUNCION -> function id parA PAR parB BLOQUE','FUNCION',6,'p_FUNCION','analyzer.py',340),
  ('FUNCION -> function id parA parB BLOQUE','FUNCION',5,'p_FUNCION','analyzer.py',341),
  ('PAR -> PAR coma P','PAR',3,'p_PAR','analyzer.py',353),
  ('PAR -> P','PAR',1,'p_PAR','analyzer.py',354),
  ('P -> id','P',1,'p_P','analyzer.py',363),
  ('STRUCT -> struct id ATR end','STRUCT',4,'p_STRUCT','analyzer.py',369),
  ('STRUCT -> mutable struct id ATR end','STRUCT',5,'p_STRUCT','analyzer.py',370),
  ('ATR -> ATR A','ATR',2,'p_ATR','analyzer.py',383),
  ('ATR -> A','ATR',1,'p_ATR','analyzer.py',384),
  ('A -> id tipo TIPO puntoycoma','A',4,'p_A','analyzer.py',393),
  ('A -> id puntoycoma','A',2,'p_A','analyzer.py',394),
  ('EXP -> EXP coma E','EXP',3,'p_EXP','analyzer.py',405),
  ('EXP -> E','EXP',1,'p_EXP','analyzer.py',406),
  ('E -> E mas E','E',3,'p_E','analyzer.py',415),
  ('E -> E menos E','E',3,'p_E','analyzer.py',416),
  ('E -> E asterisco E','E',3,'p_E','analyzer.py',417),
  ('E -> E barra E','E',3,'p_E','analyzer.py',418),
  ('E -> E caret E','E',3,'p_E','analyzer.py',419),
  ('E -> E modulo E','E',3,'p_E','analyzer.py',420),
  ('E -> menos E','E',2,'p_E','analyzer.py',421),
  ('E -> E mayor E','E',3,'p_E','analyzer.py',422),
  ('E -> E menor E','E',3,'p_E','analyzer.py',423),
  ('E -> E mayor_igual E','E',3,'p_E','analyzer.py',424),
  ('E -> E menor_igual E','E',3,'p_E','analyzer.py',425),
  ('E -> E igualacion E','E',3,'p_E','analyzer.py',426),
  ('E -> E diferenciacion E','E',3,'p_E','analyzer.py',427),
  ('E -> E or E','E',3,'p_E','analyzer.py',428),
  ('E -> E and E','E',3,'p_E','analyzer.py',429),
  ('E -> not E','E',2,'p_E','analyzer.py',430),
  ('E -> E interrog E dospuntos E','E',5,'p_E','analyzer.py',431),
  ('E -> ID','E',1,'p_E','analyzer.py',432),
  ('E -> parA E parB','E',3,'p_E','analyzer.py',433),
  ('E -> LLAMADA','E',1,'p_E','analyzer.py',434),
  ('E -> RANGO','E',1,'p_E','analyzer.py',435),
  ('E -> ARREGLO','E',1,'p_E','analyzer.py',436),
  ('E -> int64','E',1,'p_E','analyzer.py',437),
  ('E -> float64','E',1,'p_E','analyzer.py',438),
  ('E -> bool','E',1,'p_E','analyzer.py',439),
  ('E -> char','E',1,'p_E','analyzer.py',440),
  ('E -> STRING','E',1,'p_E','analyzer.py',441),
  ('E -> Nothing','E',1,'p_E','analyzer.py',442),
  ('STRING -> STRING S','STRING',2,'p_STRING','analyzer.py',472),
  ('STRING -> S','STRING',1,'p_STRING','analyzer.py',473),
  ('S -> string','S',1,'p_S','analyzer.py',483),
  ('S -> llaveA E llaveB','S',3,'p_S','analyzer.py',484),
  ('ARREGLO -> corA EXP corB','ARREGLO',3,'p_ARREGLO','analyzer.py',490),
  ('ARREGLO -> corA corB','ARREGLO',2,'p_ARREGLO','analyzer.py',491),
  ('LLAMADA -> id parA EXP parB','LLAMADA',4,'p_LLAMADA','analyzer.py',499),
  ('LLAMADA -> id parA parB','LLAMADA',3,'p_LLAMADA','analyzer.py',500),
  ('IF -> if E BLOQUE','IF',3,'p_IF','analyzer.py',511),
  ('IF -> if E BLOQUE_ABIERTO ELSE','IF',4,'p_IF','analyzer.py',512),
  ('IF -> if E BLOQUE_ABIERTO ELSEIF','IF',4,'p_IF','analyzer.py',513),
  ('ELSEIF -> elseif E BLOQUE','ELSEIF',3,'p_ELSEIF','analyzer.py',524),
  ('ELSEIF -> elseif E BLOQUE_ABIERTO ELSEIF','ELSEIF',4,'p_ELSEIF','analyzer.py',525),
  ('ELSEIF -> elseif E BLOQUE_ABIERTO ELSE','ELSEIF',4,'p_ELSEIF','analyzer.py',526),
  ('ELSE -> else BLOQUE','ELSE',2,'p_ELSE','analyzer.py',537),
  ('WHILE -> while E BLOQUE','WHILE',3,'p_WHILE','analyzer.py',544),
  ('FOR -> for id in E BLOQUE','FOR',5,'p_FOR','analyzer.py',551),
  ('RANGO -> E dospuntos E','RANGO',3,'p_RANGO','analyzer.py',558),
  ('RANGO -> dospuntos','RANGO',1,'p_RANGO','analyzer.py',559),
  ('BREAK -> break','BREAK',1,'p_BREAK','analyzer.py',568),
  ('CONTINUE -> continue','CONTINUE',1,'p_CONTINUE','analyzer.py',574),
  ('RETURN -> return E','RETURN',2,'p_RETURN','analyzer.py',580),
  ('RETURN -> return','RETURN',1,'p_RETURN','analyzer.py',581),
]
