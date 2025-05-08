; =============================================================
; Lee un char desde la línea de comandos y mostrarlo en pantalla.
; =============================================================

datos segment
    buffer db 128 dup(?)
    
    char    dw 0
    Base dw 10
    msg_invalid db 'Valor inválido', 0Dh, 0Ah, '$'  ; Mensaje si no es 0 o 1
    msg_error_len db 'El valor es muy largo', 0Dh, 0Ah, '$' ; Mensaje si es muy largo
    msg_no_value db 'Ingresa un valor', 0Dh, 0Ah, '$' ;Mensaje si no se envia un dato
  
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


EtdChar Proc

    push AX
    push BX
    push CX                           
    push DX

    mov si, 80h
    xor ch, ch
    mov cl, byte ptr es:[si]  ; Obtener la cantidad de caracteres ingresados
    cmp cl, 0
    je no_value                    ; Si no hay entrada, salir

    cmp cl, 2
    jne error_len                    ; Si no es largo 2, se manda el error


    dec cx
    inc si
    xor di, di

    inc si
    mov al, byte ptr es:[si]
    inc di

    mov char,ax
    jmp seguir


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
    seguir:


    
    pop DX  
    pop CX
    pop BX
    pop AX
    ret

EtdChar EndP

SalChar Proc

    push AX
    push BX
    push CX                           
    push DX


    mov bx, ax
    xor ax,ax
    mov ah, 02h
    mov dl, bl
    int 21h


    pop DX  
    pop CX
    pop BX
    pop AX
    ret

SalChar EndP

main: 

    mov ax, ds    ; ponemos al ES a apuntar al inicio del PSP
    mov es, ax

    mov ax, datos  ; El DS que apuntaba al PSP se debe poner a apuntar al segmento de datos para 
    mov ds, ax     ; poder usar las variables.

    mov ax, pila
    mov ss, ax


    ;--------------------------
    ;pedir dato
    

    call EtdChar
    xor cx, cx    ; mov cx, 0
    
    mov ax,char
    call SalChar    



    salir: mov ax, 4C00h   ; Protocolo de finalizaci�n del programa
        int 21h 

codigo ends

end main