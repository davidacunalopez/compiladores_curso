worldname MiEjemplo : 

Bedrock           $$Seccion de constantes
    obsidian stack consEntero = 2 ; 
    $$obsidian rune consCaracter = a ; 
    obsidian spider consString = "2" ; 
    obsidian torch conBooltrue = ON ;
    obsidian torch conBoolfalse = OFF ;  

resourcepack      $$Seccion de tipo
    anvil Edad -> stack ; 
    anvil inicial -> rune ; 
    anvil Nombre -> spider ; 
    anvil presente -> torch ; 

inventory         $$Seccion de variables
    shelf arreglo = [1,2,3,4] ; 
    shelf arreglo2 = [1,2,3,4] ; 
    shelf arreglo3 = [1,2,3,4] ; 
    shelf arreglo4 = [1,2,3,4] ; 
    shelf arreglo5 = [1,2,3,4] ; 


recipe            $$Seccion de prototipos
    spell imprimir2 ( stack :: nombre ) -> spider ; 
    ritual imprimir ( stack :: Num , spider :: nombre ) ; 
craftingtable     $$Seccion de rutinas
    
spawnpoint        $$Punto de entrada del programa
    polloCrudo 
    
    polloAsado ; 

worldsave 

