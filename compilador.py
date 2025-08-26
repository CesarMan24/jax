

palabra_reservada = [ # leg,day,back,bic,tric,sho,ex,repeat,si,chest,sets, reps, weight, remaining, prn,num,end, gym 🗑️
#    A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z   
#    a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z   
    [0 ,5 ,20,3 ,14,0 ,42,0 ,0 ,0 ,0 ,1 ,0 ,39,0 ,37,0 ,15,12,9 ,0 ,0 ,26,0 ,0 ,0 ,0 ], #0
    [0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #1
    [0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #2 leg
    [4 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #3
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ], #4 day
    [6 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,8 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #5 
    [0 ,0 ,7 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #6 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #7 back
    [0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #8 bic
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,10,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #9 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,11,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #10 
    [0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #11 tric
    [0 ,0 ,0 ,0 ,24,0 ,0 ,13,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #12 si
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #13 sho
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,41,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ], #14 ex
    [0 ,0 ,0 ,0 ,16,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #15
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,31,0 ,0 ,17,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #16  
    [0 ,0 ,0 ,0 ,18,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #17  reps
    [19,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #18 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #19 repeat
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,21,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #20 
    [0 ,0 ,0 ,0 ,22,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #21    
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,23,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #22  
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #23  chest
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,25,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #24  
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #25 sets  
    [0 ,0 ,0 ,0 ,27,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #26  
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,28,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #27 
    [0 ,0 ,0 ,0 ,0 ,0 ,29,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #28
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,30,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #29     
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #30 weight  
    [32,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #31 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,33,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #32   
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,34,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #33  
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,35,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #34 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,36,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #35   
    [0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #36  remaining
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,38,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #37
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #38 prn
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,40,0 ,0 ,0 ,0 ,0 ,0 ], #39
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #40 num
    [0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #41 end
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,43,0 ,0 ], #42
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,99,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ], #43 gym
]

Identificators = [
#     A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  # 
    [99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99, 0,  0],
    [99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,  0],
]
Operators =[[
#     +  -  =  <  > 
    [99,99,99,99,99, 0],
]]
Numbers = [
#    0-9
    [99,0]
]
Punctuation = [
# {   }  (  )  =  ,
[ 99,99,99,99,99,99]
]
Identificators = [
    []
]
def openjax() :
    analize_again = True
    with open('jax.txt', 'r', encoding='utf-8') as file:
        contents = file.read()
        #print(contents) 
        analizadorreservada(contents)
        #print(len(contents))
       # print(contents[2])
   # if(analize_again):
        #print("Analizar palabras reservadas")
        #analizadorreservada(contents) = analize_again
def analizadorlexico(contents):
    caracteres = len(contents)
    #lexemas.clear()
    contador = 0
    
def analizadornumeros(caracter,cadena):
     fila = 0
     columnainicial = 0
     #cadena = ''
     match caracter: #KEYWORDS
        case  '1':
            columnainicial = 0
            cadena += '1'
                    #contador = contador + 1
        case '2':
            columnainicial = 0
            cadena += '2'
        case '3':
            columnainicial = 0
            cadena += '3'
        case '4':
            columnainicial = 0
            cadena += '4'
        case '5':
            columnainicial = 0
            cadena += '5'
        case '6':
            columnainicial = 0
            cadena += '6'
        case '7':
            columnainicial = 0
            cadena += '7'
        case '8':
            columnainicial = 0
            cadena += '8'
        case '9':
            columnainicial = 0
            cadena += '9'
        case _  :
            columnainicial = 1
            if(cadena == ""):
                print("soy otra cosa que no sea numero")
            else:
                print("<NUMBER," +cadena+ ">") #<IF, "if">
        #palabra_reservada[fila][columnainicial] = fila
     fila = Numbers[fila][columnainicial] 
     #print("fila: " +fila)
     #print(contador)
     if fila == 0: 
            cadena = ""
            fila = 0
            columnainicial = 0

     if fila == 99:
            print("<NUMBER," +cadena+ ">") #<IF, "if">
            cadena = ""
            fila = 0
            columnainicial = 0
            
            
        

def analizadorreservada(contents):
    cadena = ""
    fila = 0
    columnainicial = 0
    contador = 0
    codigo = len(contents)
    while contador < codigo:
        #difference = codigo - contador
        #for caracter in contents: 
        caracter = contents[contador]
       # print(caracter)
        match caracter: #KEYWORDS
                case 'a':
                    columnainicial = 0
                    print("a aceptado")
                    cadena += 'a'
                    #contador = contador + 1
                case 'b':
                    columnainicial = 1
                    print("b aceptado")
                    cadena += 'b'
                    #contador = contador + 1
                case 'c':
                    columnainicial = 2
                    print("c aceptado")
                    cadena += 'c'
                    #contador = contador + 1
                case 'd':
                    columnainicial = 3
                    print("d aceptado")
                    cadena += 'd'
                    #contador = contador + 1
                case 'e':
                    columnainicial = 4
                    print("e aceptado")
                    cadena += 'e'
                    #contador = contador + 1
                case  'f':
                    columnainicial = 5
                    print("f aceptado")
                    cadena += 'f'
                    #contador = contador + 1
                case  'g':
                    columnainicial = 6
                    print("g aceptado")
                    cadena += 'g'
                    #contador = contador + 1
                case  'h':
                    columnainicial = 7
                    print("h aceptado")
                    #contador = contador + 1
                case  'i':
                    columnainicial = 8
                    print("i aceptado")
                    cadena += 'i'
                    #contador = contador + 1
                case  'j':
                    columnainicial = 9
                    print("j aceptado")
                    cadena += 'j'
                    #contador = contador + 1
                case 'k':
                    columnainicial = 10
                    print("k aceptado")
                    cadena += 'k'
                    #contador = contador + 1
                case 'l':
                    columnainicial = 11
                    print("l aceptado")
                    cadena += 'l'
                    #contador = contador + 1
                case  'm':
                    columnainicial = 12
                    print("m aceptado")
                    cadena += 'm'
                    #contador = contador + 1
                case 'n':
                    columnainicial = 13
                    print("n aceptado")
                    cadena += 'n'
                    #contador = contador + 1
                case 'o':
                    columnainicial = 14
                    print("0 aceptado")
                    cadena += 'o'
                    #contador = contador + 1
                case 'p':
                    columnainicial = 15
                    print("p aceptado")
                    cadena += 'p'
                    #contador = contador + 1
                case 'q':
                    columnainicial = 16
                    print("q aceptado")
                    cadena += 'q'
                    #contador = contador + 1
                case 'r':
                    columnainicial = 17
                    print("r aceptado")
                    cadena += 'r'
                    #contador = contador + 1
                case 's':
                    columnainicial = 18
                    print("s aceptado")
                    cadena += 's'
                    #contador = contador + 1
                case 't':
                    columnainicial = 19
                    print("t aceptado")
                    cadena += 't'
                    #contador = contador + 1
                case  'u':
                    columnainicial = 20
                    print("u aceptado")
                    cadena += 'u'
                    #contador = contador + 1
                case 'v':
                    columnainicial = 21
                    print("v aceptado")
                    cadena += 'v'
                    #contador = contador + 1
                case 'w':
                    columnainicial = 22
                    print("w aceptado")
                    cadena += 'w'
                    #contador = contador + 1
                case 'x':
                    columnainicial = 23
                    print("x aceptado")
                    cadena += 'x'
                    #contador = contador + 1
                case  'y':
                    columnainicial = 24
                    print("y aceptado")
                    cadena += 'y'
                    #contador = contador + 1
                case  'z':
                    columnainicial = 25
                    print ()
                    cadena += 'z'
                    #contador = contador + 1
                case _:
                    #columnainicial = 26
                    analizadornumeros(caracter,cadena)   
                    
            #palabra_reservada[fila][columnainicial] = fila
        fila = palabra_reservada[fila][columnainicial]
        #print("fila: " +fila)
        #print(contador)
        if fila == 0: 
            cadena = ""
            fila = 0
            columnainicial = 0

        if fila == 99:
            print("<KEYWORD," +cadena+ ">") #<IF, "if">
            cadena = ""
            fila = 0
            columnainicial = 0
        contador = contador + 1    
            
            
            
openjax()
#lexemas = []
#print (lexemas)