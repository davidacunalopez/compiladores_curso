; =============================================================
; Lee un booleano (0 o 1) desde la línea de comandos y mostrarlo en pantalla.
; =============================================================

datos segment
  buffer db 128 dup(?)

  boolean    dw 0
  Base dw 10

  
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


EtdBool Proc

    push AX
    push BX
    push CX                           
    push DX

    mov si, 80h
    xor ch, ch
    mov cl, byte ptr es:[si]  ; Obtener la cantidad de caracteres ingresados
    cmp cl, 0
    je es_falso                    ; Si no hay entrada, salir



    dec cx
    inc si
    xor di, di

    cicloLectura:
        inc si
        mov al, byte ptr es:[si]
        cmp al,'0'
        jne es_verdadero
        inc di
        loop cicloLectura
             
    es_falso:
        mov boolean, 0
        jmp fin

    es_verdadero:
        mov boolean, 1
        jmp fin

    


       

    fin:  

    
    pop DX  
    pop CX
    pop BX
    pop AX
    ret

EtdBool EndP

SalBool Proc

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

SalBool EndP

main: 

    mov ax, ds    ; ponemos al ES a apuntar al inicio del PSP
    mov es, ax

    mov ax, datos  ; El DS que apuntaba al PSP se debe poner a apuntar al segmento de datos para 
    mov ds, ax     ; poder usar las variables.

    mov ax, pila
    mov ss, ax


    ;--------------------------
    ;pedir dato
    

    call EtdBool
    xor cx, cx    ; mov cx, 0
    
    mov ax,boolean
    call SalBool    



    salir: mov ax, 4C00h   ; Protocolo de finalizaci�n del programa
        int 21h 

codigo ends

end main