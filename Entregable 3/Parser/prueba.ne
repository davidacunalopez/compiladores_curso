worldname MiEjemplo : 

Bedrock           $$Seccion de constantes
    obsidian stack x2 = 2 ; 
resourcepack      $$Seccion de tipo
    anvil Edad -> stack ; 
    anvil Nombre -> spider ; 

inventory         $$Seccion de variables
    stack nombre = "David" ; 

recipe            $$Seccion de prototipos
    spell imprimir2 ( stack :: nombre ) -> spider ; 
    ritual imprimir ( stack :: Num ) ; 
craftingtable     $$Seccion de rutinas

spawnpoint        $$Punto de entrada del programa

worldsave 

