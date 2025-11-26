# Matriz de transiciones 
from dataclasses import dataclass 

@dataclass
class Token:
    tipo: str      # "NUMERO", "IDENTIFICADOR", "KEYWORD", etc.
    valor: str     # lexema: "gym", "num", "+", "(", "123", etc.
    linea: int
tokens = []            # lista de tokens producidos por el léxico
current_index = 0      # índice del token actual para el parser
current_token = None   # token actual
word = None  

palabra_reservada = [
  #  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63  64
  #  a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z  #  {  }  (  )  =  ,  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  q  R  S  T  U  V  W  X  Y  Z  %  +  -  <  >   *
    [0 ,5 ,20,3 ,14,0 ,42,0 ,0 ,0 ,0 ,1 ,0 ,39,0 ,37,0 ,15,12,9 ,0 ,0 ,26,0 ,0 ,0 ,44,99,99,99,99,99,99,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,46,99,99,99,99,99], #0
    [0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #1
    [0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #2 leg
    [4 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #3
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #4 day
    [6 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,8 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #5 
    [0 ,0 ,7 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #6 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #7 back
    [0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #8 bic
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,10,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #9 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,11,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #10 
    [0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #11 tric
    [0 ,0 ,0 ,0 ,24,0 ,0 ,13,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #12 si
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #13 sho
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,41,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #14 ex
    [0 ,0 ,0 ,0 ,16,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,49,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #15
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,31,0 ,0 ,17,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #16  
    [0 ,0 ,0 ,0 ,18,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #17  reps
    [19,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #18 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #19 repeat
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,21,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #20 
    [0 ,0 ,0 ,0 ,22,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #21    
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,47,0 ,0 ,0 ,23,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #22  
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #23  chest
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,25,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #24  
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #25 sets  
    [0 ,0 ,0 ,0 ,27,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #26  
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,28,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #27 
    [0 ,0 ,0 ,0 ,0 ,0 ,29,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #28
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,30,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #29     
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #30 weight  
    [32,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #31 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,33,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #32   
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,34,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #33  
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,35,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #34 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,36,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #35   
    [0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #36  remaining
    [0 ,0 ,0 ,0 ,53,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,38,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #37
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #38 prn
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,40,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #39
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #40 num
    [0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #41 end
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,43,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #42
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #43 gym
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,44,99,99,99,99,99,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #44 NUMEROS
    [45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,0 ,99,99,99,99,99,99,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,0 ,0 ,0 ,0 ,0 , 0], #45 IDENTIFICADORES
    [46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,45,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46, 0], #46 IGNORER
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,48,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #47
    [0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #48 word
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,50,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #49 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,51,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #50 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,52,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #51 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #52 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,54,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #53 
    [0 ,0 ,0 ,0 ,0 ,55,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #54
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,56,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #55
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,57,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #56
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,58,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #57
    [59,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #58
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,60,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #59
    [0 ,0 ,61,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #60
    [0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , 0], #61 performance
]

# Estados de aceptación y sus correspondientes y sus tipos de token
# Mapea estado final 
estados_aceptacion = {
    2: ("MUSCLEKW", "leg"),           # leg
    4: ("KEYWORD", "day"),           # day  
    7: ("MUSCLEKW", "back"),          # back
    8: ("MUSCLEKW", "bic"),           # bic
    11: ("MUSCLEKW", "tric"),         # tric
    12: ("KEYWORD", "si"),           # si
    13: ("MUSCLEKW", "sho"),          # sho
    14: ("KEYWORD", "ex"),           # ex
    17: ("KEYWORD", "reps"),         # reps
    19: ("KEYWORD", "repeat"),       # repeat
    23: ("MUSCLEKW", "chest"),        # chest
    25: ("KEYWORD", "sets"),         # sets
    30: ("KEYWORD", "weight"),       # weight
    36: ("KEYWORD", "remaining"),    # remaining
    38: ("KEYWORD", "prn"),          # prn (print)
    40: ("KEYWORD", "num"),          # num
    41: ("KEYWORD", "end"),          # end
    43: ("KEYWORD", "gym"),          # gym
    48: ("KEYWORD", "word"),         # word
    44: ("NUMERO", ""),              # números
    45: ("IDENTIFICADOR", ""),       # identificadores
    52: ("KEYWORD", "routin"),       # routin
    61: ("KEYWORD", "performance")   #performance
}

# Variable types que pueden declarar variables
tipos_variable = {"leg", "back", "bic", "tric", "sho", "chest", "num", "word"}

# mapeo de caracteres a idices de columna en la matriz
def get_column_index(char):
    if char == 'a': return 0
    elif char == 'b': return 1
    elif char == 'c': return 2
    elif char == 'd': return 3
    elif char == 'e': return 4
    elif char == 'f': return 5
    elif char == 'g': return 6
    elif char == 'h': return 7
    elif char == 'i': return 8
    elif char == 'j': return 9
    elif char == 'k': return 10
    elif char == 'l': return 11
    elif char == 'm': return 12
    elif char == 'n': return 13
    elif char == 'o': return 14
    elif char == 'p': return 15
    elif char == 'q': return 16
    elif char == 'r': return 17
    elif char == 's': return 18
    elif char == 't': return 19
    elif char == 'u': return 20
    elif char == 'v': return 21
    elif char == 'w': return 22
    elif char == 'x': return 23
    elif char == 'y': return 24
    elif char == 'z': return 25
    elif char.isdigit(): return 26
    elif char == '{': return 27
    elif char == '}': return 28
    elif char == '(': return 29
    elif char == ')': return 30
    elif char == '=': return 31
    elif char == ',': return 32
    elif char == 'A': return 33
    elif char == 'B': return 34
    elif char == 'C': return 35
    elif char == 'D': return 36
    elif char == 'E': return 37
    elif char == 'F': return 38
    elif char == 'G': return 39
    elif char == 'H': return 40
    elif char == 'I': return 41
    elif char == 'J': return 42
    elif char == 'K': return 43
    elif char == 'L': return 44
    elif char == 'M': return 45
    elif char == 'N': return 46
    elif char == 'O': return 47
    elif char == 'P': return 48
    elif char == 'Q': return 49
    elif char == 'R': return 50
    elif char == 'S': return 51
    elif char == 'T': return 52
    elif char == 'U': return 53
    elif char == 'V': return 54
    elif char == 'W': return 55
    elif char == 'X': return 56
    elif char == 'Y': return 57
    elif char == 'Z': return 58
    elif char == '%': return 59
    elif char == '+': return 60
    elif char == '-': return 61
    elif char == '<': return 62
    elif char == '>': return 63
    elif char == '*': return 64
    else: return -1

#tablas de símbolos
Nombres = []
Tipo = []
Tamano = []
Dimension = []
DeclarationLine = []
UsageLine = []

def openjax():
    with open('pruebas.txt', 'r', encoding='utf-8') as file:
        contents = file.read()
        print (" ANALISIS LEXICO")
        analizador(contents) #analisis lexico
        if len(tokens) == 0:
            print("No se genero ningun token")
            return
        print("-----------------------------")
        print (" ANALISIS SINTATICO")
        GetNextWorld()
        res = PROGRAMA()
        if res == True and word == 'eof':
            print('sintaxis correcta')
        else:
            print('sintaxis incorrecta')

        print("\n")
        print("TABLA DE SÍMBOLOS:")
        print(" NOMBRE   TIPO   TAMANO   DIMENSION   DECLARATIONLINE   USAGELINE")
        for variable in range(len(Nombres)):
            usage_str = str(UsageLine[variable]) if isinstance(UsageLine[variable], list) else str(UsageLine[variable])
            print(f"{Nombres[variable]:<8} {Tipo[variable]:<6} {Tamano[variable]:<7} {Dimension[variable]:<10} {DeclarationLine[variable]:<16} {usage_str}")

def determinar_tipo_token(estado_final, cadena):
    """Determina el tipo de token basado en el estado final del autómata"""
    if estado_final in estados_aceptacion:
        tipo, _ = estados_aceptacion[estado_final]
        if tipo == "NUMERO":
            return ("NUMERO", cadena)
        elif tipo == "IDENTIFICADOR":
            return ("IDENTIFICADOR", cadena)
        else:
            return (tipo, estados_aceptacion[estado_final][1])
    elif estado_final == 99:  # Estados especiales para operadores y puntuación
        if cadena in ['=', '+', '-', '<', '>','*']:
            return ("OPERATOR", cadena)
        elif cadena in ['{', '}', '(', ')', ',']:
            return ("PUNCTUATION", cadena)
        else:
            return ("UNKNOWN", cadena)
    else:
        return ("UNKNOWN", cadena)

def analizador(contents):
    pila_par = [] 
    await_type = " "
    ignorer_mode = False
    linea_codigo = 1
    parentesisabiertos = 0
    llavesabiertos = 0
    cadena = ""
    fila = 0
    contador = 0
    codigo = len(contents)
    
    print(f"Código a analizar tiene {codigo} caracteres")
    
    while contador < codigo:
        caracter = contents[contador]
        
        # saltos de línea 
        if caracter in ['\n', '\t']:
            if caracter == '\n':
                linea_codigo += 1
                ignorer_mode = False
            # procweea cadena pendiente antes del salto de linea
            if cadena != "":
                await_type = procesar_cadena_completa(cadena, fila, await_type, linea_codigo - (1 if caracter == '\n' else 0))
                cadena = ""
                fila = 0
            contador += 1
            continue
        
        # ignorar espacios si no estamos haciendo una cadena
        if caracter == ' ':
            if cadena != "":
                await_type = procesar_cadena_completa(cadena, fila, await_type, linea_codigo)
                cadena = ""
                fila = 0
            contador += 1
            continue
        
        # modo comentario
        if ignorer_mode:
            if caracter == '%':
                ignorer_mode = False
            contador += 1
            continue
        
        # empieza comentario
        if caracter == '%':
            ignorer_mode = True
            if cadena != "":
                await_type = procesar_cadena_completa(cadena, fila, await_type, linea_codigo)
                cadena = ""
                fila = 0
            contador += 1
            continue
        
        # agarra indice de columna
        columnainicial = get_column_index(caracter)
        
        if columnainicial == -1:
            print(f"Error léxico en línea {linea_codigo}: caracter no reconocido '{caracter}'")
            return
        
        # si estamos en estado inicial, comienza nueva cadena
        if fila == 0:
            cadena = caracter
            fila = palabra_reservada[0][columnainicial]
            if fila == 0:
                print(f"Error léxico en línea {linea_codigo}: transición no válida desde estado inicial con '{caracter}'")
                return
        else:
            # obtiene siguiente estado del autómata
            nuevo_estado = palabra_reservada[fila][columnainicial]
            
            # si el nuevo estado es 0 (error) y no estamos en el estado inicial
            if nuevo_estado == 0:
                # Procesar la cadena actual
                await_type = procesar_cadena_completa(cadena, fila, await_type, linea_codigo)
                # Reiniciar con el caracter actual
                cadena = caracter
                fila = palabra_reservada[0][columnainicial]
                if fila == 0:
                    print(f"Error léxico en línea {linea_codigo}: transición no válida '{caracter}'")
                    return
            else:
                # Continuar construyendo la cadena
                cadena += caracter
                fila = nuevo_estado
        
        # Si llegamos a un estado final especial (99)
        if fila == 99:
            await_type = procesar_token_especial(cadena, await_type, linea_codigo)
            cadena = ""
            fila = 0
        
        # Manejar paréntesis y llaves para verificar balance
        # if caracter == '(':
        #     parentesisabiertos += 1
        # elif caracter == ')':
        #     parentesisabiertos -= 1
        # elif caracter == '{':
        #     llavesabiertos += 1
        # elif caracter == '}':
        #     llavesabiertos -= 1
         # Manejo con pila de paréntesis/llaves (mejor que contadores)
        if caracter in ('(', '{'):
            # guardar tipo y línea para mensaje claro si queda sin cerrar
            pila_par.append((caracter, linea_codigo))
        elif caracter in (')', '}'):
            if not pila_par:
                print(f"Error léxico en línea {linea_codigo}: cierre '{caracter}' sin apertura correspondiente")
                return
            apertura, linea_apertura = pila_par.pop()
            pares = {'(':')', '{':'}'}
            if pares.get(apertura) != caracter:
                print(f"Error léxico en línea {linea_codigo}: cierre '{caracter}' no coincide con apertura '{apertura}' en línea {linea_apertura}")
                return
        
        contador += 1
    
    # Procesar cadena final si existe
    if cadena != "":
        procesar_cadena_completa(cadena, fila, await_type, linea_codigo)
    
    # Verificar balance
    # if llavesabiertos != 0:
    #     print("Error Léxico: llaves desbalanceadas")
    #     return
    # if parentesisabiertos != 0:
    #     print("Error Léxico: paréntesis desbalanceados") 
    #     return
    if pila_par:
        # reportar cada apertura sin cerrar
        for apertura, linea_apertura in reversed(pila_par):
            print(f"Error Léxico: apertura '{apertura}' en línea {linea_apertura} sin su cierre correspondiente")
        return
    tokens.append(Token("EOF", "eof", linea_codigo))

def procesar_cadena_completa(cadena, estado_actual, await_type, linea_codigo):
    """Procesa una cadena completa usando solo el autómata"""
    tipo_token, valor = determinar_tipo_token(estado_actual, cadena)
    print(f"<{tipo_token}, {valor}>")
    tokens.append(Token(tipo_token, valor, linea_codigo))
    # Manejar lógica de declaración/uso de variables
    if tipo_token == "KEYWORD" and valor in tipos_variable:
        return valor  # Estamos esperando un identificador para declarar
    elif tipo_token == "MUSCLEKW" and valor in tipos_variable:
        return valor
    elif tipo_token == "IDENTIFICADOR":
        return manejar_identificador(cadena, await_type, linea_codigo)
    
    return " "  # Resetear await_type

def procesar_token_especial(cadena, await_type, linea_codigo):
    """Procesa tokens especiales que terminan en estado 99"""
    # El último caracter determina el tipo de token especial
    if len(cadena) > 1:
        # Procesar la parte anterior primero
        cadena_anterior = cadena[:-1]
        if cadena_anterior:
            # Necesitamos determinar el estado de la cadena anterior
            estado_anterior = simular_automata(cadena_anterior)
            await_type = procesar_cadena_completa(cadena_anterior, estado_anterior, await_type, linea_codigo)
    
    # Procesar el último caracter
    ultimo_caracter = cadena[-1]
    if ultimo_caracter in ['=', '+', '-', '<', '>','*']:
        print(f"<OPERATOR, {ultimo_caracter}>")
        tokens.append(Token("OPERATOR", ultimo_caracter, linea_codigo))
    elif ultimo_caracter in ['{', '}', '(', ')', ',']:
        print(f"<PUNCTUATION, {ultimo_caracter}>")
        tokens.append(Token("PUNCTUATION", ultimo_caracter, linea_codigo))
    
    return await_type

def simular_automata(cadena):
    """Simula el autómata para obtener el estado final de una cadena"""
    estado = 0
    for char in cadena:
        col_index = get_column_index(char)
        if col_index == -1:
            return 0
        estado = palabra_reservada[estado][col_index]
        if estado == 0:
            break
    return estado

def manejar_identificador(identificador, await_type, linea_codigo):
    """Maneja la lógica de declaración y uso de identificadores"""
    if await_type != " " and await_type in tipos_variable:
        # Es una declaración de variable
        if identificador in Nombres:
            print(f"Error: Identificador '{identificador}' ya fue declarado")
        else:
            Nombres.append(identificador)
            Tipo.append(await_type)
            Tamano.append(len(identificador))
            if await_type == "word":
                Dimension.append(1)
            else:
                Dimension.append(0)
            DeclarationLine.append(linea_codigo)
            UsageLine.append([linea_codigo])
        return " "  # Resetear await_type después de declaración
    else:
        # Es un uso de variable
        if identificador in Nombres:
            posicion_identificador = Nombres.index(identificador)
            if isinstance(UsageLine[posicion_identificador], list):
                UsageLine[posicion_identificador].append(linea_codigo)
            else:
                UsageLine[posicion_identificador] = [UsageLine[posicion_identificador], linea_codigo]
        # No imprimir error para variables no declaradas, solo seguir el flujo
        return await_type  # Mantener await_type
def GetNextWorld():
    global current_index
    global current_token
    global word
    if current_index < len(tokens):
        current_token = tokens[current_index]
        current_index += 1
    else:
         print('eof')
         current_token = Token("EOF", "eof", current_token.linea if current_token else 0)
    if current_token.tipo == "NUMERO":
        word = "numero"
    elif current_token.tipo == "IDENTIFICADOR":
        word = "identificador"
    elif current_token.tipo in ("KEYWORD", "MUSCLEKW"):
        # lexema tal cual: gym, day, num, sho, bic, si, repeat, etc.
        word = current_token.valor
    elif current_token.tipo in ("OPERATOR", "PUNCTUATION"):
        # +, -, *, (, ), {, }, =, , , <, >
        word = current_token.valor
    elif current_token.tipo == "EOF":
        word = "eof"
    else:
        word = "ERROR"
    return word
def syntax_error(msg):
    # current_token es global; tiene .linea y .valor
    print(f"Error sintáctico en línea {current_token.linea}: {msg}. "
          f"Token encontrado siguiente: '{current_token.valor}' ") #(clase: {word})
    return False
def PROGRAMA() :
    #print("PROGRAMA -> gym day { ... } gym end FUNCLIST")
    if word != 'gym':
        syntax_error("se esperaba 'gym' al inicio del programa")
        return False
    GetNextWorld()
    if word != 'day':
        print('fallo analisis sintactico: day')
        syntax_error("se esperaba 'day' al inicio del programa")
        return False
    GetNextWorld()
    if word != '{':
        print('fallo analisis sintactico: {')
        syntax_error("se esperaba '{' al inicio del programa")
        return False
    GetNextWorld()
    res = ASSIGNPERFORMANCE()
    if res == False:
        print('Fallo en ASSIGNPERFORMANCE')
        return False
    #GetNextWorld()
    res = STMTLIST()
    if res == False:
        print('Fallo en STMTLIST() en PROGRAMA')
        return False
    #GetNextWorld()
    if word != '}':
        print('Fallo en }')
        syntax_error("se esperaba '}' al inicio del programa")
        return False
    GetNextWorld()
    if word != 'gym':
        print('Fallo en gym en PROGRAMA')
        syntax_error("se esperaba 'gym' al inicio del programa")
        return False
    GetNextWorld()
    if word != 'end':
        print('Fallo en end rn PROGRAMA')
        syntax_error("se esperaba 'end' al inicio del programa")
        return False
    GetNextWorld()
    res = FUNCLIST()
    if res == False:
        print('Fallo en FUNCLIST()')
        return False
    print("PROGRAMA -> gym day {ASSIGNPERFORMANCE  } gym end FUNCLIST")
    return True
def FUNCLIST(): #E | FUNCDEF FUNCLIST
    if word == 'eof':
        print("FUNCLIST -> E")
        return True
    elif word == 'routin':
        res = FUNCDEF()
        if res == False:
            print('Fallo en FUNCDEF FUNCLIST()')
            
            return False
        GetNextWorld()
        res = FUNCLIST()
        if res == False:
            print('Fallo en FUNCLIST FUNCLIST()')
            return False
        print("FUNCLIST -> FUNCDEF FUNCLIST")
        return True
    syntax_error("se esperaba 'routin' o fin de archivo en la lista de funciones (FUNCLIST)")
    return False
def FUNCDEF(): #routin identificador ( PARAMS ) { STMTLIST } end
    if word != 'routin':
        print('Fallo en routin FUNCDEF()')
        syntax_error("se esperaba 'routin' ")
        return False
    GetNextWorld()
    if word != 'identificador':
        print('Fallo en identificador FUNCDEF()')
        syntax_error("se esperaba 'identificador' ")
        return False
    GetNextWorld()
    if word != '(':
        print('Fallo en ( FUNCDEF()')
        syntax_error("se esperaba '(' ")
        return False
    GetNextWorld()
    res = PARAMS()
    if res == False:
        print('Fallo en PARAMS FUNCDEF()')
        return False
    #GetNextWorld()
    if word != ')':
        print('Fallo en ) FUNCDEF()')
        syntax_error("se esperaba ')' ")
        return False
    GetNextWorld()
    if word != '{':
        print('Fallo en { FUNCDEF()')
        syntax_error("se esperaba '{' ")
        return False
    GetNextWorld()
    res =  STMTLIST()
    if res == False:
        print('Fallo en STMTLIST FUNCLIST()')
        return False
    #GetNextWorld()
    if word != '}':
        print('Fallo en } FUNCDEF()')
        syntax_error("se esperaba '}' ")
        return False
    GetNextWorld()
    if word != 'end':
        print('Fallo en end FUNCDEF()')
        syntax_error("se esperaba 'end' ")
        return False
    print("FUNCDEF ->  routin identificador ( PARAMS ) { STMTLIST } end")
    return True
def PARAMS(): # E | PARAM PARAMS_TAIL
    if word == ')':
        print('PARAMS -> E')
        return True
    elif word in ('num', 'sho', 'bic', 'leg', 'chest', 'back', 'tric'):
        res = PARAM()
        if res == False:
            print('Fallo en PARAM PARAMS()')
            return False
        GetNextWorld()
        res = PARAMS_TAIL()
        if res == False:
                print('Fallo en PARAMS_TAIL PARAMS()')
                return False
        print("PARAMS ->  PARAM PARAMS_TAIL")
        return True
    syntax_error("se esperaba 'num' o MUSCLEKW (sho, bic, leg, chest, back, tric) en la lista de parámetros (PARAMS)")
    return False
def PARAM(): #num identificador | MUSCLEKW identificador
    if word == 'num': # num identificador
        GetNextWorld()
        if word != 'identificador':
            print('Fallo en identificador PARAMS()')
            syntax_error("se esperaba 'identificador' ")
            return False
        print("PARAM -> num identificador")
        return True
    elif word in ('sho', 'bic', 'leg', 'chest', 'back', 'tric'):
        GetNextWorld()
        if word != 'identificador':
            print('Fallo en identificador PARAMS()')
            syntax_error("se esperaba 'identificador' ")
            return False
        print("PARAM -> MUSCLEKW identificador")
        return True
    return False
def PARAMS_TAIL(): # E|, PARAM PARAMS_TAIL 
    if word == ')': # E
        print("PARAMS_TAIL -> E")
        return True
    if word == ',': #, PARAM PARAMS_TAIL 
        # print('Fallo en , en PARAMS_TAIL')
        # return False
        GetNextWorld()
        res = PARAM()
        if res ==  False:
            print('Fallo en PARAM en PARAMS_TAIL')
            return False
        GetNextWorld()
        res = PARAMS_TAIL()
        if res ==  False:
            print('Fallo en PARAMS_TAIL en PARAMS_TAIL')
            return False
        print("FUNCLIST -> , PARAM PARAMS_TAIL")
        return True
    syntax_error("se esperaba ',' o ')' en la lista de parámetros (PARAMS_TAIL)")
    return False
def ASSIGNPERFORMANCE(): # num performance = numero
    if word != 'num':
        print('Fallo en num EN ASSIGNPERFORMANCE')
        syntax_error("se esperaba 'num' ")
        return False
    GetNextWorld()
    # if word != 'identificador': #performance PERFORMANCE
    #     print('Fallo en identificador ASSIGNPERFORMANCE()')
    #     return False
    if word != 'performance':
        print('Fallo en performance ASSIGNPERFORMANCE()')
        syntax_error("se esperaba 'performance' ")
        return False
    GetNextWorld()
    if word != '=':
         print('Fallo en PERFORMANCE')
         syntax_error("se esperaba '=' ")
         return False
    GetNextWorld()
    if word != 'numero':
         print('Fallo en numero')
         syntax_error("se esperaba 'numero' ")
         return False
    GetNextWorld()
    print("ASSIGNPERFORMANCE ->  num PERFORMANCE = numero")
    return True
def STMTLIST(): #  E |STMT STMTLIST
    if word in ('}', 'end', 'eof'): # E
        print("STMTLIST -> E")
        return True
    if word in ( 'sho' ,'bic', 'leg' ,'chest', 'back' ,'tric' ,'num' , 'identificador', 'si' ,'repeat' ,'prn' ): #solo estaba numero # STMT STMTLIST #numero puede faltar
        res = STMT()
        if res == False:
            print('Fallo en STMT() em STMTLIST')
            return False
        #GetNextWorld()
        res = STMTLIST()
        if res == False:
            print('Fallo en STMTLIST() en ASSIGNPERFORMANCE')
            return False
        print("STMTLIST -> STMT STMTLIST")
        return True
    syntax_error("se esperaba inicio de instrucción válida (sho, bic, leg, chest, back, tric, 'num', identificador, 'si', 'repeat' o 'prn') o cierre de bloque ('}' o 'end') en STMTLIST")
    return False
def STMT() : #EXDCL | VARDECL | IF | REPEAT | PRINT | IDLEAD
    if word in ('sho', 'bic', 'leg', 'chest', 'back', 'tric'):
        res = EXDCL()
        if res == False:
            print('Fallo en EXDCL()')
            return False
        print("STMT -> EXDCL()")
        return True
    elif word == 'num':
        res = VARDECL()
        if res == False:
            print('Fallo en VARDECL()')
            return False
        print("STMT -> VARDECL()")
        return True
    elif word == 'si':
        res = IF()
        if res == False:
            return False
        print("STMT -> IF()")
        return True
    elif word == 'repeat':
        res = REPEAT()
        if res == False:
            return False
        print("STMT -> REPEAT()")
        return True
    elif word == 'prn':
        res = PRINT()
        if res == False:
            return False
        print("STMT -> PRINT()")
        return True
    elif word == 'identificador':
        res = IDLEAD()
        if res == False:
            return False
        print("STMT -> IDLEAD()")
        return True
    syntax_error("se esperaba inicio de instrucción válida (MUSCLEKW, 'num', 'si', 'repeat', 'prn' o identificador) en STMT")
    return False
def IDLEAD(): # identificador IDTAIL 
    if word != 'identificador':
        print('Fallo en  identificador IDLEAD()')
        return False
    GetNextWorld()
    res = IDTAIL()
    if res == False:
        print('Fallo en  IDTAIL IDLEAD()')
        return False
    return True
def IDTAIL(): # =ASSIGNRHS | ( ARGS )
    if word =='=': #word in ('sho', 'bic', 'leg', 'chest', 'back', 'tric'):
        GetNextWorld()
        res = ASSIGNRHS()
        if res == False:
            print('Fallo en  ASSIGNRHS IDTAIL()') 
            return False
        print("IDTAIL-> =ASSIGNRHS")
        return True
    elif word == '(':
        # if word != '(':
        #     print ('Fallo ( en IDTAIL()')
        #     return False
        GetNextWorld()
        res = ARGS()
        if res == False:
            print ('Fallo ARGS en IDTAIL()')
            return False
        if word != ')':
            print ('Fallo ) en IDTAIL()')
            syntax_error("se esperaba ')' ")
            GetNextWorld()
            return False
        GetNextWorld()
        return True
    syntax_error("se esperaba '=' o '(' después de un identificador en IDTAIL")
    return False
def ASSIGNRHS(): # EXPR | EXRHS
    if word in ('numero', 'identificador', '('):
        res = EXPR()
        if res == False:
            print ('Fallo EXPR en ASSSIGNRHS()')
            return False
        print("ASSIGNRHS-> EXPR")
        return True
    elif word == 'ex' :
        res = EXRHS()
        if res == False:
            print ('Fallo EXRHS en ASSSIGNRHS()')
            return False
        print("ASSIGNRHS-> EXRHS")
        return True
    syntax_error("se esperaba 'numero', 'identificador', '(' o 'ex' en el lado derecho de la asignación (ASSIGNRHS)")
    return False
def ARGS():  # E | ARG ARGS_TAIL
    if word == ')':
        print("ARGS -> ε")
        return True
    if word == 'identificador' :
        res = ARG()
        if res == False:
            print ('Fallo ARG en ARGS()')
            return False
        GetNextWorld()
        res = ARGS_TAIL()
        if res == False:
            print ('Fallo ARGS_TAIL en ARGS()')
            return False
        print("ARGS-> ARG ARGS_TAIL")
        return True
    syntax_error("se esperaba 'identificador' o ')' en la lista de argumentos (ARGS)")
    return False
def ARG(): # identificador
 if word != 'identificador':
     print ('Fallo identificador en ARG()')
     syntax_error("se esperaba 'identificador' ")
     return False
 print("ARG-> identificador")
 return True
def ARGS_TAIL(): #E | , ARG ARGS_TAIL
    if word == ')':
        print("ARGS_TAIL -> ε")
        return True
    elif word == ',': #, ARG ARGS_TAIL
        GetNextWorld()
        res = ARG()
        if res == False:
            print ('Fallo ARG en ARGS_TAIL()')
            return False
        GetNextWorld()
        res = ARGS_TAIL()
        return True
    syntax_error("se esperaba ',' o ')' en la lista de argumentos (ARGS_TAIL)")
    return False
def PRINT(): # prn ( PRINTARG )
    if word != 'prn':
        print('Fallo en  prn PRINT()')
        syntax_error("se esperaba 'prn' ")
        return False
    GetNextWorld()
    if word != '(':
        print('Fallo en ( PRINT()')
        syntax_error("se esperaba '(' ")
        return False
    GetNextWorld()
    res = PRINTARG()
    if res == False:
        print('Fallo en PRINTARG en PRINT()')
        return False
    #GetNextWorld()
    if word != ')':
        print('Fallo en ) en PRINT()')
        syntax_error("se esperaba ')' ")
        return False
    GetNextWorld()
    
    return True
def PRINTARG(): #EXPR |”string” 
    if word in ('numero', 'identificador', '('):
        res = EXPR()
        if res == False:
            print('Fallo en EXPR en PRINTARG()')
            return False
    elif word == '”':
        if word !=  '”':
            print('Fallo en ” en PRINTARG()')
            syntax_error("se esperaba ” ")
            return False
        GetNextWorld()
        if word != '”':
            print('Fallo en ” en PRINTARG()')
            syntax_error("se esperaba ” ")
            return False
    return True
def EXDCL(): # MUSCLEKW identificador = EXRHS
    res = MUSCLEKW()
    if res == False:
        print('Fallo en MUSCLEKW EXDCL')
        return False
    #GetNextWorld()
    if word != 'identificador':
        print('Fallo en identificador EXDCL')
        syntax_error("se esperaba identificador ")
        return False
    GetNextWorld()
    if word != '=':
        print('Fallo en  = EXDCL')
        syntax_error("se esperaba = ")
        return False
    GetNextWorld()
    res = EXRHS()
    if res == False:
        print('Fallo en EXRHS() en EXDCL')
        return False
    return True
def VARDECL(): #num identificador = EXPR
    if word != 'num':
        print('Fallo en num en VARDECL()')
        syntax_error("se esperaba num ")
        return False
    GetNextWorld()
    if word != 'identificador':
        print('Fallo en identificador en VARDECL()')
        syntax_error("se esperaba identificador ")
        return False
    GetNextWorld()
    if word != '=':
        print('Fallo en = en VARDECL()')
        syntax_error("se esperaba =")
        return False
    GetNextWorld()
    res = EXPR()
    if res == False:
        print('Fallo en EXPR en VARDECL()')
        return False
    return True
def REPEAT(): #repeat REPEATOP { STMTLIST }
    if word != 'repeat':
        print('Fallo en EXPR en REPEAT()')
        syntax_error("se esperaba repeat")
        return False
    GetNextWorld()
    res = REPEATOP()
    if  res == False:
        print('Fallo en REPEAT en REPEAT()')
        return False
    #GetNextWorld() ###############################
    if word != '{':
        print('Fallo en { en REPEAT()')
        syntax_error("se esperaba {")
        return False
    GetNextWorld()
    res = STMTLIST()
    if res == False:
        print('Fallo en STMTLIST en REPEAT()')
        return False
    #GetNextWorld() ###################################
    if word != '}':
        print('Fallo en } en REPEAT()')
        syntax_error("se esperaba }")
        return False
    GetNextWorld()
    print("REPEAT-> repeat REPEATOP { STMTLIST }")
    return True
def REPEATOP(): # EXPR | remaining 
    if word in ('numero', 'identificador', '('):
        res = EXPR()
        if res == False:
            print('Fallo en EXPR en REPEATOP()')
            return False
        print("REPEATOP-> EXPR")
        return True
    elif word == 'remaining':
        GetNextWorld()   
        print("REPEATOP-> remaining")
        return True
    syntax_error("se esperaba una expresión o la palabra clave 'remaining' después de 'repeat' (REPEATOP)")
    return False
def MUSCLEKW(): # sho | bic | leg | chest | back | tric 

    if word in ('sho', 'bic', 'leg', 'chest', 'back', 'tric'):
        print("MUSCLEKW ->", word)
        GetNextWorld()     
        return True
    syntax_error("se esperaba MUSCLEKW")
    return False
   
def EXRHS(): #ex ( sets = numero , reps = numero ,weight = numero )
    if word != 'ex':
        print('Fallo en ex EXRHS')
        syntax_error("se esperaba ex")
        return False
    GetNextWorld()
    if word != '(':
        print('Fallo en ( EXRHS')
        syntax_error("se esperaba (")
        return False
    GetNextWorld()
    if word != 'sets':
        print('Fallo en sets EXRHS')
        syntax_error("se esperaba sets")
        return False
    GetNextWorld()
    if word != '=':
        print('Fallo en = EXRHS')
        syntax_error("se esperaba =")
        return False
    GetNextWorld()
    if word != 'numero':
        print('Fallo en numero EXRHS')
        syntax_error("se esperaba numero")
        return False
    GetNextWorld()
    if word != ',':
        print('Fallo en , EXRHS')
        syntax_error("se esperaba ,")
        return False
    GetNextWorld()
    if word != 'reps':
        print('Fallo en reps EXRHS')
        syntax_error("se esperaba reps")
        return False
    GetNextWorld()
    if word != '=':
        print('Fallo en = EXRHS')
        syntax_error("se esperaba =")
        return False
    GetNextWorld()
    if word != 'numero':
        print('Fallo en numero EXRHS')
        syntax_error("se esperaba numero")
        return False
    GetNextWorld()
    if word != ',':
        print('Fallo en , EXRHS')
        syntax_error("se esperaba ,")
        return False
    GetNextWorld()
    if word != 'weight':
        print('Fallo en weight EXRHS')
        syntax_error("se esperaba weight")
        return False
    GetNextWorld()
    if word != '=':
        print('Fallo en = en EXRHS')
        syntax_error("se esperaba =")
        return False
    GetNextWorld()
    if word != 'numero':
        print('Fallo en numero EXRHS')
        syntax_error("se esperaba numero")
        return False
    GetNextWorld()
    if word != ')':
        print('Fallo en ) EXRHS')
        syntax_error("se esperaba )")
        return False
    GetNextWorld()
    print("EXRHS -> ex ( sets = numero , reps = numero ,weight = numero )")
    return True
def IF(): #si Releq { STMTLIST }
    if word != 'si':
        print('Fallo en si IF')
        syntax_error("se esperaba si")
        return False
    GetNextWorld()
    res = RELEQ()
    if res == False:
        print("Fallo en Releq en IF")
        return False
    #GetNextWorld()
    if word != '{':
        print('Fallo en { IF')
        syntax_error("se esperaba {")
        return False
    GetNextWorld()
    res = STMTLIST()
    if res == False:
        print("Fallo en stmtlist IF") 
        return False
    #GetNextWorld()
    if word != '}':
        print('Fallo en } IF')
        syntax_error("se esperaba }")
        return False
    GetNextWorld()
    print("IF-> si Releq { STMTLIST }")
    return True
def RELEQ(): #EXPR EXPRLOG
    res = EXPR()
    if res == False:
        print("Fallo en EXPR RELEQ") 
        return False
    #GetNextWorld()
    res = EXPRLOG()
    if res == False:
        print("Fallo en EXPRLOG RELEQ")
        return False
    print("RELEQ -> EXPR EXPRLOG")
    return True
def EXPR(): # TERM EXPRTAIL
    res = TERM()
    if res == False:
        print("Fallo en TERM EXPR")
        return False
    #GetNextWorld()
    res = EXPRTAIL()
    if res == False:
        print("Fallo en EXPRTAIL EXPR")
        return False
    print("EXPR-> TERM EXPRTAIL")
    return True
def EXPRLOG(): # OPLOG EXPR
    res = OPLOG()
    if res == False:
        print("Fallo en OPLOG EXPRLOG")
        return False
    GetNextWorld()
    res = EXPR()
    if res == False:
        print("Fallo en EXPR EXPRLOG")
        return False
    print("EXPRLOG-> OPLOG EXPR")
    return True
def OPLOG(): # <|>|=
    if word == '<':
        return True
    elif word == '>':
        return True
    elif word == '=':
        return True
    syntax_error("se esperaba un operador relacional '<', '>' o '=' (OPLOG)")
    return False
def TERM(): # FACTOR TERMTAIL  FACTOR TERMTAIL
    res = FACTOR()
    if res == False:
        print("Fallo en FACTOR TERM")
        return False
    #GetNextWorld()
    res = TERMTAIL()
    if res == False:
        print("Fallo en TERMTAIL TERM")
        return False
    print("TERM -> FACTOR TERMTAIL")
    return True
def FACTOR(): # identificador | numero | (EXPR)  
    if word =='identificador':
        print("FACTOR -> identificador")
        GetNextWorld()
        return True
    elif word == 'numero':
        print("FACTOR -> numero")
        GetNextWorld()
        return True
    elif word == '(':
        GetNextWorld()
        #print("FACTOR -> (")
        res = EXPR()
        if res == False:
            print("Fallo en EXPR en FACTOR")
            return False
        if word != ')':
            print("Fallo en ) en FACTOR")
            syntax_error("se esperaba )")
            return False
        print("FACTOR -> (EXPR)")
        GetNextWorld()
        return True
    syntax_error("se esperaba identificador, numero o (")
    return False
def TERMTAIL(): # E |*FACTOR TERMTAIL
    if word in ('+','-','<','>', '=',',',')', '{', '}', 'sho', 'bic', 'leg', 'chest','back', 'tric', 'num', 'identificador', 'si', 'repeat', 'prn'): # E
        print("TERMTAIL -> E")
        return True
    elif word == '*': # *FACTOR TERMTAIL
        # print("Fallo en * TERMTAIL")
        # return False
        GetNextWorld()
        res = FACTOR()
        if res == False:
            print("Fallo en FACTOR TERMTAIL")
            return False
        res = TERMTAIL()
        if res == False:
            print("Fallo en TERMTAIL TERMTAIL")
            return False
        print("TERMTAIL -> *FACTOR TERMTAIL")
        return True
    syntax_error("se esperaba * , operadores, {, }, tipos de varible, identificadores, si , repeat, prn")
    return False
def EXPRTAIL(): # E|+TERM EXPRTAIL | -TERM EXPRTAIL
    if word in ( '<', '>', '=',',',')', '{', '}', 'sho', 'bic', 'leg', 'chest', 'back', 'tric', 'num', 'identificador', 'si', 'repeat', 'prn'): # E
        print("EXPRTAIL -> E")
        return True
    elif word == '+':
        # print('Fallo en + EXPRTAIL')
        # return False
        GetNextWorld()
        res = TERM()
        if res == False:
            print("Fallo en TERM EXPRTAIL")
            return False
        #GetNextWorld()
        res = EXPRTAIL()
        if res == False:
            print("Fallo en EXPRTAIL EXPRTAIL")
            return False
        print("EXPRTAIL -> +TERM EXPRTAIL")
        return True
    elif word == '-':
        # print('Fallo en - EXPRTAIL')
        # return False
        GetNextWorld()
        res = TERM()
        if res == False:
            print("Fallo en TERM EXPRTAIL")
            return False
        #GetNextWorld()
        res = EXPRTAIL()
        if res == False:
            print("Fallo en EXPRTAIL EXPRTAIL")
            return False
        print("EXPRTAIL -> -TERM EXPRTAIL")
        return True
    syntax_error("se esperaba '+' o '-' o fin de expresión (EXPRTAIL)")
    return False

# Ejecutar analizador
if __name__ == "__main__":
    openjax()