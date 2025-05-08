; Este es un programa que imprime los numeros naturales del 0 a N

datos segment
  string db 128 dup(?)


  
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


EtdString Proc

    push AX
    push BX
    push CX                           
    push DX

    mov si, 80h
    xor ch, ch
    mov cl, byte ptr es:[si]  ; Obtener la cantidad de caracteres ingresados

    dec cx
    inc si
    xor di, di

    cicloLectura:
        inc si
        mov al, byte ptr es:[si]
        mov byte ptr string[di], al
        inc di
        loop cicloLectura
             
    mov byte ptr string[di], '$'

    
    pop DX  
    pop CX
    pop BX
    pop AX
    ret

EtdString EndP

SalString Proc

    push AX
    push BX
    push CX                           
    push DX


    mov ah, 09h
    lea dx, string
    int 21h



    pop DX  
    pop CX
    pop BX
    pop AX
    ret

SalString EndP

main: 

    mov ax, ds    ; ponemos al ES a apuntar al inicio del PSP
    mov es, ax

    mov ax, datos  ; El DS que apuntaba al PSP se debe poner a apuntar al segmento de datos para 
    mov ds, ax     ; poder usar las variables.

    mov ax, pila
    mov ss, ax


    ;--------------------------
    ;pedir dato
    

    call EtdString
    xor cx, cx    ; mov cx, 0
    
    call SalString



    salir: mov ax, 4C00h   ; Protocolo de finalizaci�n del programa
        int 21h 

codigo ends

end main





