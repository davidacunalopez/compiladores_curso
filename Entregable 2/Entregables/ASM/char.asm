; =============================================================
; Te piede 1 entrada char y te lo desplega
; =============================================================

datos segment
  buffer db 128 dup(?)

  numero    dw 0
  numero2    dw 0
  Base dw 10
  msg_error db 'No es un  numero valido', 0Dh, 0Ah, '$'
  msg_soldato db 'Ingresa un caracter', 0Dh, 0Ah, '$'
  msg_result db 'Resultado', 0Dh, 0Ah, '$'
  signo dw 0

  
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
    push ax
    push bx
    push cx
    push dx
    
    mov signo,0
    ; Mostrar mensaje
    mov ah, 09h
    lea dx, msg_soldato
    int 21h

    ; Leer cadena
    lea dx, buffer
    mov byte ptr buffer, 2         ; Tamaño máximo de entrada
    mov ah, 0Ah
    int 21h

    xor ax, ax
    xor bx, bx
    xor cx, cx
    xor dx, dx
    xor si, si

    lea si, buffer+2               
    mov cl, byte ptr buffer+1      


    
   

    exit:
        
        pop dx
        pop cx
        pop bx
        pop ax
        xor ax,ax
        mov al, byte ptr [si]
        ret


EtdChar EndP


SalChar Proc

    push AX
    push BX
    push CX
    push DX


    
    
    
    mov ah, 02h     
    mov dl,al
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
    





    
    

    push ax
    call CamLin
    mov ah, 09h
    lea dx, msg_result
    int 21h
    pop ax
    
    call SalChar   





    salir: mov ax, 4C00h   ; Protocolo de finalizaci�n del programa
        int 21h 

codigo ends

end main