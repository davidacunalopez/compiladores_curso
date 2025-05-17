; =============================================================
; Te pide un string, un char y un booleano, para devolverte el dato convertido en entero
; =============================================================
datos segment
  string db 128 dup(?)
  char  dw 0
  buffer db 6, ?, 6 dup(0)
  str_int dw 0
  Base dw 10
  msg_in_char db 'Ingrese un Char: $'
  msg_in_string db 'Ingrese un String: $'
  msg_in_bool db 'Ingrese un booleano: $'
  msg_int db 'Dato como entero: $'
  msg_error db 'No es un  numero valido', 0Dh, 0Ah, '$'
  msg_error_len db 'El valor es muy largo', 0Dh, 0Ah, '$' ; Mensaje si es muy largo
    msg_no_value db 'Ingresa un valor', 0Dh, 0Ah, '$' ;Mensaje si no se envia un dato
  
 boolean    dw 0

  
datos endS

pila segment stack 'stack'
   dw 256 dup(?)
pila endS


codigo segment
   Assume CS:codigo, DS:datos, SS:pila

CamLin Proc
   push ax
   push dx

   mov dl, 13
   mov ah, 02h
   int 21h

   mov dl, 10
   int 21h

   pop dx
   pop ax
   ret
CamLin EndP

SolDato Proc

    push AX
    push BX
    push CX                           
    push DX

    mov ah, 0Ah
    lea dx, buffer
    int 21h


    ; Agregar fin de cadena al buffer para impresión
    mov al, buffer+1   ; AL contiene la cantidad de caracteres ingresados
    add al, 2          ; Ajustar la posición correcta dentro del buffer
    mov si, ax         ; Mover a SI para indexar correctamente
    mov byte ptr buffer[si], '$'  ; Colocar fin de cadena



    



    pop DX  
    pop CX
    pop BX
    pop AX
    ret

SolDato EndP

EtdString Proc

    push AX
    push BX
    push CX                           
    push DX

    mov cl, [buffer+1]    ; CL = número de caracteres escritos
    lea si, [buffer+2]    ; SI apunta al primer carácter escrito

    xor di, di

    cicloRecorrer:
        mov dl, [si]      ; DL = carácter actual
        mov byte ptr string[di], dl
        inc di

        inc si            ; Avanzar al siguiente carácter
        loop cicloRecorrer
             
    mov byte ptr string[di], '$'

    
    pop DX  
    pop CX
    pop BX
    pop AX
    ret

EtdString EndP

EtdChar Proc

    push AX
    push BX
    push CX                           
    push DX
    xor ch, ch
    xor dx,dx
    lea si, [buffer+2]
    mov cl, [buffer+1]  ; Obtener la cantidad de caracteres ingresados
    cmp cl, 0
    je no_value                    ; Si no hay entrada, salir

    cmp cl, 1
    jne error_len                    ; Si no es largo 2, se manda el error

    
    mov dl, [si]

    mov char,dx
    jmp seguirchar


    error_len:
        mov ah, 09h
        lea dx, msg_error_len
        int 21h
        jmp fin

    no_value:
        mov ah, 09h
        lea dx, msg_no_value
        int 21h
        jmp fin

       

    fin:
        mov ax, 4C00h
        int 21h
    seguirchar:


    
    pop DX  
    pop CX
    pop BX
    pop AX
    ret

EtdChar EndP

EtdBool Proc

    push AX
    push BX
    push CX                           
    push DX

    lea si, [buffer+2]
    xor ch, ch
    mov cl, [buffer+1]  ; Obtener la cantidad de caracteres ingresados
    cmp cl, 0
    je es_falso                    ; Si no hay entrada, salir

    xor di, di

    cicloLectura_bool:
        
        mov al, [si]
        cmp al,'0'
        jne es_verdadero
        inc di
        inc si
        loop cicloLectura_bool
             
    es_falso:
        mov boolean, 0
        jmp fin_bool

    es_verdadero:
        mov boolean, 1
        jmp fin_bool

    

    
       

    fin_bool:  

    
    pop DX  
    pop CX
    pop BX
    pop AX
    ret

EtdBool EndP

converStringInt Proc
    push AX
    push BX
    push CX                           
    push DX

    jmp curso
    no_es_digito:
        mov ah, 09h
        lea dx, msg_error
        int 21h

        mov ax, 4C00h
        int 21h

    curso:
        xor cx, cx
        lea si, [string]     ; SI apunta al primer carácter
        ciclo_recorrer:
            mov dl, [si]  
            cmp dl, '$'
            je salir_recorrer
            inc si             ; Avanzar al siguiente carácter
            inc cx
            jmp ciclo_recorrer ; Repetir hasta que CL=0
        salir_recorrer:


        lea si, [string]
        xor di, di

        cicloLectura:
            xor ax,ax
            mov dx, cx
            dec dx
            mov bl, [si]

            ; Comparar si AL >= '0'
            cmp bl, '0'
            jl no_es_digito         ; Si es menor que '0', no es un dígito

            ; Comparar si AL <= '9'
            cmp bl, '9'
            jg no_es_digito         ; Si es mayor que '9', no es un dígito

            sub bl, '0'
            
           mov ax,1
            potencia:
                cmp dx, 0
                je salir_potencia
                push dx
                mov dx,10
                mul dx

                pop dx
                dec dx
                jmp potencia
            salir_potencia:
            cmp ax, 1
            je sumar



            multiplicar:
                mul bx 
                jmp seguir
            sumar:
                mov ax,bx 
            seguir:


            
            add str_int, ax
            mov ax,str_int
            
            inc di
            inc si
            
            loop cicloLectura



    pop DX  
    pop CX
    pop BX
    pop AX
    ret

converStringInt EndP
SalInt Proc

    push AX
    push BX
    push CX                           
    push DX


    xor cx, cx
        mov bx, Base
    ciclo1PAX: xor dx, dx
        div bx
        push dx
        inc cx
        cmp ax, 0
        jne ciclo1PAX
        mov ah, 02h
    ciclo2PAX: pop DX
        add dl, 30h
        cmp dl, 39h
        jbe prnPAX
        add dl, 7
    prnPAX: int 21h
        loop ciclo2PAX 



    pop DX  
    pop CX
    pop BX
    pop AX
    ret

SalInt EndP
main: 

    mov ax, ds    ; ponemos al ES a apuntar al inicio del PSP
    mov es, ax

    mov ax, datos  ; El DS que apuntaba al PSP se debe poner a apuntar al segmento de datos para 
    mov ds, ax     ; poder usar las variables.

    mov ax, pila
    mov ss, ax


    ;-------------------------------

    mov ah, 09h
    lea dx, msg_in_string
    int 21h
    call soldato  

    call EtdString
    call CamLin
    xor cx, cx    ; mov cx, 0

    call converStringInt 
    
    mov ah, 09h
    lea dx, msg_int
    int 21h
    mov ax, str_int
    call SalInt
    

    ;----------------------------------------
    call CamLin
    mov ah, 09h
    lea dx, msg_in_char
    int 21h
    call soldato  
    call EtdChar
    call CamLin
    mov ah, 09h
    lea dx, msg_int
    int 21h
    
    lea si, [char]
    xor ax,ax
    mov ax, [si]
    call SalInt


    ;----------------------------------------
     call CamLin
    mov ah, 09h
    lea dx, msg_in_bool
    int 21h
    call soldato 
    call EtdBool
    call CamLin
    lea dx, msg_int
    int 21h
    lea si, [boolean]
    mov ax, [si]
    call SalInt


    salir: mov ax, 4C00h   ; Protocolo de finalizaci�n del programa
    int 21h 

codigo ends

end main