; =============================================================
; Lee un numero natural desde la línea de comandos y mostrarlo en pantalla.
; =============================================================
datos segment
  buffer db 128 dup(?)

  numero    dw 0
  Base dw 10
  msg_error db 'No es un  numero valido', 0Dh, 0Ah, '$'
  
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


EtdInt Proc

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
        xor cx, cx    ; mov cx, 0
        mov si, 80h
        xor ch, ch
        mov cl, byte ptr es:[si]  ; Obtener la cantidad de caracteres ingresados

        dec cx
        inc si
        xor di, di

        

       
        cicloLectura:

            mov dx, cx
            dec dx
            xor ax, ax
            
            inc si
            mov bl, byte ptr es:[si]

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


            
            add numero, ax
            mov ax,numero
            mov byte ptr buffer[di], bl
            inc di
            
            loop cicloLectura

       

       

    
    pop DX  
    pop CX
    pop BX
    pop AX
    ret

EtdInt EndP

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


    ;--------------------------
    ;pedir dato
    

    call EtdInt
    xor cx, cx    ; mov cx, 0
    
    mov ax,numero
    call SalInt    



    salir: mov ax, 4C00h   ; Protocolo de finalizaci�n del programa
        int 21h 

codigo ends

end main