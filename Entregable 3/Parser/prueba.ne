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
    Edad varEntero = 2 ; 
    stack varEntero2 = 3 ; 
    $$rune varCaracter = a ; 
    spider varString = "2" ; 
    torch varBooltrue = ON ; 
    torch varBoolfalse = OFF ;  


recipe            $$Seccion de prototipos
    spell imprimir2 ( stack :: nombre ) -> spider ; 
    ritual imprimir ( stack :: Num , spider :: nombre ) ; 
craftingtable     $$Seccion de rutinas
    
spawnpoint        $$Punto de entrada del programa
    polloCrudo 
       varEntero = 9 ; 
       target varEntero > B miss 
       polloCrudo 
              
       polloAsado ; 
       hit
       polloCrudo 
         varEntero2 = 8 ;
         varEntero = 6 ;
       polloAsado ; 
    polloAsado ; 

worldsave 

