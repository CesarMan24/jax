KEYWORDS = ['leg','day','back','bic','tric','sho','ex','repeat','si','chest','sets','reps', 'weight', 'remaining','num','end','gym']
Variable_Types = ['leg', 'num', 'chest', 'sho', 'tric', 'back', 'bic', 'word'] #anadi uno 
palabra_reservada = [ # leg,day,back,bic,tric,sho,ex,repeat,si,chest,sets, reps, weight, remaining,num,end, gym 🗑️
     #KEYWORDS                                                 NUMEROS    PUNTUACION               IDENTIFICADORES                                            IGNORER    OPERATORS
#    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63
#    a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z  #  {  }  (  )  =  ,  A  B  C  D  E  F  G  H  I  J  K  M  N  L  O  P  q  R  S  T  U  V  W  X  Y  Z  %  +  -  <  >  
    [0 ,5 ,20,3 ,14,0 ,42,0 ,0 ,0 ,0 ,1 ,0 ,39,0 ,37,0 ,15,12,9 ,0 ,0 ,26,0 ,0 ,0 ,44,99,99,99,99,99,99,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,46,99,99,99,99,], #0
    [0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0,  ], #1
    [0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #2 leg
    [4 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #3
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #4 day
    [6 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,8 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #5 
    [0 ,0 ,7 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,5 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #6 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #7 back
    [0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #8 bic
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,10,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #9 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,11,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #10 
    [0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #11 tric
    [0 ,0 ,0 ,0 ,24,0 ,0 ,13,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #12 si
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #13 sho
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,41,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #14 ex
    [0 ,0 ,0 ,0 ,16,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #15
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,31,0 ,0 ,17,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #16  
    [0 ,0 ,0 ,0 ,18,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #17  reps
    [19,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #18 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #19 repeat
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,21,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #20 
    [0 ,0 ,0 ,0 ,22,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #21    
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,47,0 ,0 ,0 ,23,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #22  
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #23  chest
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,25,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #24  
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #25 sets  
    [0 ,0 ,0 ,0 ,27,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #26  
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,28,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #27 
    [0 ,0 ,0 ,0 ,0 ,0 ,29,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #28
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,30,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #29     
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #30 weight  
    [32,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #31 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,33,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #32   
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,34,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #33  
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,35,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #34 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,36,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #35   
    [0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #36  remaining
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,38,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #37
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #38 prn
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,40,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #39
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #40 num
    [0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #41 end
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,43,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #42
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #43 gym
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,44,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #44 NUMEROS
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,0 ,0 ,0 ,0 ,0 ], #45 IDENTIFICADORES
    [46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,45,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46], #46 IIGNORER
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,48,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #47 gym
    [0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #47 gym
]

Nombres = []
Tipo = []
Tamano = []
Dimension = []
DeclarationLine = []
UsageLine = []




def openjax() :
    analize_again = True
    with open('pruebas.txt', 'r', encoding='utf-8') as file:
        contents = file.read()
        #print(contents) 
        analizador(contents)
        print("\n")
        print(" NOMBRE   TIPO   TAMANO   DIMENSION   DECLARATIONLINE   USAGELINE")
        for variable in range(len(Nombres)):
           # print("tabla de valores")
            print(Nombres[variable], Tipo[variable], Tamano[variable],Dimension[variable], DeclarationLine[variable], UsageLine[variable] )
        
        #print(len(contents))
       # print(contents[2])
   # if(analize_again):
        #print("Analizar palabras reservadas")
        #analizadorreservada(contents) = analize_again

def analizador(contents):
    Await_type = " "
    ignorer_mode = False
    linea_codigo = 1
    parentesisabiertos = 0
    llavesabiertos = 0
    cadena = ""
    cadenabuena = ""
    fila = 0
    columnainicial = 0
    contador = 0
    codigo = len(contents)
    print (codigo)
    while contador < codigo:
        #difference = codigo - contador
        #for caracter in contents: 
        caracter = contents[contador]
        print(linea_codigo)
       # print(caracter)
       # if caracter in [' ', '\n', '\t']:
        if caracter in [ '\n', '\t']:
            if caracter == '\n':
                #print("space")
                linea_codigo = linea_codigo + 1
                ignorer_mode = False
            contador = contador + 1
            continue
        if ignorer_mode:
            if caracter == '\n':
                linea_codigo = linea_codigo + 1
            if caracter == '%':
                ignorer_mode = False
                contador = contador + 1
            contador = contador + 1
            continue
        match caracter: #KEYWORDS
                case '%': 
                    columnainicial = 59
                    print("ignorer")
                    #cadena += ''
                    contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    #linea_codigo = linea_codigo + 1
                    ignorer_mode = True
                case 'a':
                    columnainicial = 0
                    #print("a aceptado")
                    cadena += 'a'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                        
                case 'b':
                    columnainicial = 1
                    #print("b aceptado")
                    cadena += 'b'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case 'c':
                    columnainicial = 2
                    #print("c aceptado")
                    cadena += 'c'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case 'd':
                    columnainicial = 3
                    #print("d aceptado")
                    cadena += 'd'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case 'e':
                    columnainicial = 4
                    #print("e aceptado")
                    cadena += 'e'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case  'f':
                    columnainicial = 5
                    #print("f aceptado")
                    cadena += 'f'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case  'g':
                    columnainicial = 6
                    #print("g aceptado")
                    cadena += 'g'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case  'h':
                    columnainicial = 7
                    #print("h aceptado")
                    cadena += 'h'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case  'i':
                    columnainicial = 8
                    #print("i aceptado")
                    cadena += 'i'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case  'j':
                    columnainicial = 9
                   # print("j aceptado")
                    cadena += 'j'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case 'k':
                    columnainicial = 10
                    #print("k aceptado")
                    cadena += 'k'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case 'l':
                    columnainicial = 11
                    #print("l aceptado")
                    cadena += 'l'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case  'm':
                    columnainicial = 12
                    #print("m aceptado")
                    cadena += 'm'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case 'n':
                    columnainicial = 13
                    #print("n aceptado")
                    cadena += 'n'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                case 'o':
                    columnainicial = 14
                    #print("0 aceptado")
                    cadena += 'o'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                case 'p':
                    columnainicial = 15
                    #print("p aceptado")
                    cadena += 'p'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                case 'q':
                    columnainicial = 16
                   # print("q aceptado")
                    cadena += 'q'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case 'r':
                    columnainicial = 17
                    #print("r aceptado")
                    cadena += 'r'
                    
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case 's':
                    columnainicial = 18
                    #print("s aceptado")
                    cadena += 's'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case 't':
                    columnainicial = 19
                    #print("t aceptado")
                    cadena += 't'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case  'u':
                    columnainicial = 20
                   # print("u aceptado")
                    cadena += 'u'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case 'v':
                    columnainicial = 21
                    #print("v aceptado")
                    cadena += 'v'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case 'w':
                    columnainicial = 22
                    #print("w aceptado")
                    cadena += 'w'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case 'x':
                    columnainicial = 23
                    #print("x aceptado")
                    cadena += 'x'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case  'y':
                    columnainicial = 24
                    #print("y aceptado")
                    cadena += 'y'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case  'z':
                    columnainicial = 25
                    #print ("z aceptado")
                    cadena += 'z'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        if cadena in Variable_Types:
                            Await_type = cadena
                        print("<KEYWORD, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case  '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
                    columnainicial = 26
                   # print ("# aceptado")
                    cadena += caracter
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if(contents[contador + 1].isdigit()):
                        #print("siguiente cracter es numero, volver a dar vuelta")
                        pass
                    else:
                        #print("numero terminado")
                        print("<NUMERO, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case '{':
                    columnainicial = 27
                    #print ("{ aceptado")
                    cadena += '{'
                    fila = palabra_reservada[fila][columnainicial]
                    if(fila == 99):
                        print("<PUNCTUATION, " +cadena+ ">") #<IF, "if"
                        llavesabiertos = llavesabiertos + 1
                        cadena = ""
                        fila = 0
                case '}': #  {  }  (  )  =  ,
                    columnainicial = 28
                    #print("} aceptado")
                    cadena += '}'
                    fila = palabra_reservada[fila][columnainicial]
                    if (fila == 99):
                        print("<PUNCTUATION, " +cadena+ ">") #<IF, "if"
                        llavesabiertos = llavesabiertos - 1
                        cadena = ""
                        fila = 0
                case '(': #  {  }  (  )  =  ,
                    columnainicial = 29
                    #print("( aceptado")
                    cadena += '('
                    fila = palabra_reservada[fila][columnainicial]
                    if (fila == 99):
                        print("<PUNCTUATION, " +cadena+ ">") #<IF, "if"
                        parentesisabiertos = parentesisabiertos + 1
                        cadena = ""
                        fila = 0
                case ')':
                    columnainicial = 30
                    #print(") aceptado")
                    cadena += ')'
                    fila = palabra_reservada[fila][columnainicial]
                    if (fila == 99):
                        print("<PUNCTUATION, " +cadena+ ">") #<IF, "if"
                        parentesisabiertos = parentesisabiertos - 1
                        cadena = ""
                        fila = 0
                case '=':
                    columnainicial = 31
                    #print("= aceptado")
                    cadena += '='
                    fila = palabra_reservada[fila][columnainicial]
                    if (fila == 99):
                        print("<OPERATOR, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case ',':
                    columnainicial = 32
                    #print(", aceptado")
                    cadena += ','
                    fila = palabra_reservada[fila][columnainicial]
                    if (fila == 99):
                        print("<PUNCTUATION, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case 'A':
                    columnainicial = 33
                   # print("A aceptado")
                    cadena += 'A'
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        #print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'B':
                    columnainicial = 34
                   # print("B aceptado")
                    cadena += 'B'
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                       # print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'C':
                    columnainicial = 35
                    #print("C aceptado")
                    cadena += 'C'
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                       # print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"´
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'D':
                    columnainicial = 36
                   # print("D aceptado")
                    cadena += 'D'
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        #print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'E':
                    columnainicial = 37
                   # print("E aceptado")
                    cadena += 'E'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                       pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case  'F':
                    columnainicial = 38
                   # print("F aceptado")
                    cadena += 'F'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                       pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case  'G':
                    columnainicial = 39
                   # print("G aceptado")
                    cadena += 'G'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                       pass
                    else:
                       # print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case  'H':
                    columnainicial = 40
                   # print("H aceptado")
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta") 
                       pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if" o
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case  'I':
                    columnainicial = 41
                    #print("I aceptado")
                    cadena += 'I'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        #print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case  'J':
                    columnainicial = 42
                    #print("J aceptado")
                    cadena += 'J'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        #print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'K':
                    columnainicial = 43
                    #print("K aceptado")
                    cadena += 'K'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        #print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'L':
                    columnainicial = 44
                   # print("L aceptado")
                    cadena += 'L'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        #print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case  'M':
                    columnainicial = 45
                    #print("M aceptado")
                    cadena += 'M'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                       pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'N':
                    columnainicial = 46
                   # print("N aceptado")
                    cadena += 'N'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        #print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                       # print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'O':
                    columnainicial = 47
                    #print("O aceptado")
                    cadena += 'O'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        #print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                       # print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'P':
                    columnainicial = 48
                    #print("P aceptado")
                    cadena += 'P'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                       # print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'Q':
                    columnainicial = 49
                    #print("Q aceptado")
                    cadena += 'Q'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        #print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'R':
                    columnainicial = 50
                   # print("R aceptado")
                    cadena += 'R'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        #print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'S':
                    columnainicial = 51
                    #print("S aceptado")
                    cadena += 'S'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'T':
                    columnainicial = 52
                   # print("T aceptado")
                    cadena += 'T'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case  'U':
                    columnainicial = 53
                    #print("U aceptado")
                    cadena += 'U'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'V':
                    columnainicial = 54
                    #print("V aceptado")
                    cadena += 'V'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'W':
                    columnainicial = 55
                    #print("W aceptado")
                    cadena += 'W'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        #print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                       # print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case 'X':
                    columnainicial = 56
                    #print("X aceptado")
                    cadena += 'X'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                        #print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case  'Y':
                    columnainicial = 57
                   # print("Y aceptado")
                    cadena += 'Y'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                       # print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case  'Z':
                    columnainicial = 58
                    #print ("Z aceptado")
                    cadena += 'Z'
                    #contador = contador + 1
                    fila = palabra_reservada[fila][columnainicial]
                    if contents[contador + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                       # print("siguiente cracter es LETRA MAYUSCULA, volver a dar vuelta")
                        pass
                    else:
                       # print("identificador terminado")
                        print("<IDENTIFICATOR, " +cadena+ ">") #<IF, "if"
                        if Await_type != " ":
                            Nombres.append(cadena)
                            Tipo.append(Await_type)
                            Tamano.append(len(cadena))
                            if Await_type == "word":
                                Dimension.append(1)
                            else:
                                Dimension.append(0)
                            DeclarationLine.append(linea_codigo)
                            UsageLine.append(linea_codigo)
                        else:
                            # print("Imposible utilizar identificador sin asignarle un tipo de variable")
                            # return
                            if cadena in Nombres:
                                posicionidentificador = Nombres.index(cadena)
                                UsageLine[posicionidentificador].append(linea_codigo)
                            else:
                                print("Imposible utilizar identificador sin asignarle un tipo de variable")
                                return
                        cadena = ""
                        fila = 0
                case '+':
                    columnainicial = 60
                   # print("+ aceptado")
                    cadena += '+'
                    fila = palabra_reservada[fila][columnainicial]
                    if (fila == 99):
                        print("<OPERATOR, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case '-':
                    columnainicial = 61
                   # print("+ aceptado")
                    cadena += '-'
                    fila = palabra_reservada[fila][columnainicial]
                    if (fila == 99):
                        print("<OPERATOR, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case '<':
                    columnainicial = 62
                    #print("< aceptado")
                    cadena += '-'
                    fila = palabra_reservada[fila][columnainicial]
                    if (fila == 99):
                        print("<OPERATOR, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case '>':
                    columnainicial = 63
                   # print("> aceptado")
                    cadena += '>'
                    fila = palabra_reservada[fila][columnainicial]
                    if (fila == 99):
                        print("<OPERATOR, " +cadena+ ">") #<IF, "if"
                        cadena = ""
                        fila = 0
                case default:
                    if(caracter != " "):
                        print("Error lexico")
                        return 
                    #print("space")
                    fila = 0
                    
                    # if (caracter != " "):
                    #     #columnainicial = 26
                    #     #analizadorpunctuation(caracter,cadena) 
                    #     print("caracter: " +caracter)  
                    #     #print("algo que no es palabra unica")
                    #     fila = analizadorpunctuation(caracter)
                    # else: 
                    #     print("espacio")
        #palabra_reservada[fila][columnainicial] = fila
        #fila = palabra_reservada[fila][columnainicial]
        #print("fila: " +fila)
        #print(contador)
        
       ### print(cadena)
        if fila == 0: 
            cadena = ""
            fila = 0
            columnainicial = 0
            #print("Error Lexico")

        # if fila == 99:
        #     print("<KEYWORD, " +cadena+ ">") #<IF, "if">
        #     #cadena = " "
        #     cadenabuena += " "
        #     cadenabuena += cadena
        #     print("cadenabuena: " +cadenabuena)
        #     fila = fila
        #     columnainicial = 0
        contador = contador + 1   
    if(llavesabiertos != 0):
        print("Error Lexico: llaves desbalanceadas")
        return
    if(parentesisabiertos != 0):
        print("Error Lexico: parentesis desbalanceados") 
        return
            
# def analizadorpunctuation(caracter):
#     #fila = 0
#     columnainicial = 0
#     bracket = []
#     match caracter:
#         case '{':
#             columnainicial = 0
#             #cadena += '{'
#             print("Llego al analizadorpuntuacion")
#             fila = 1
#         case '}':
#             columnainicial = 1
#             #cadena += '}'
#             fila = 0
#         case '(':
#             columnainicial = 2
#             #cadena += '('
#             fila = 0
#         case ')':
#             columnainicial = 3
#             #cadena += ')'
            
#         case '=':
#             columnainicial = 4
#             #cadena += '='
#         case ',':
#             columnainicial = 5
#             #cadena += ','
#         case _: 
#             print("hasta punctuation")
#     #fila = Punctuation[fila][columnainicial]
#     if (fila == 99):
#         print("<PUNCTUATION, " +caracter)
    
#     return fila
        

            
            
                
            
openjax()

#lexemas = []
#print (lexemas)