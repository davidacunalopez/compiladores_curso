; =============================================================
; Te piede 1 entrada entero y te lo desplega
; =============================================================

datos segment
  buffer db 128 dup(?)

  numero    dw 0
  numero2    dw 0
  Base dw 10
  msg_error db 'No es un  numero valido', 0Dh, 0Ah, '$'
  msg_soldato db 'Ingresa un numero', 0Dh, 0Ah, '$'
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


EtdInt Proc
    push ax
    push bx
    push cx
    push dx
    push si
    mov signo,0
    ; Mostrar mensaje
    mov ah, 09h
    lea dx, msg_soldato
    int 21h

    ; Leer cadena
    lea dx, buffer
    mov byte ptr buffer, 5         ; Tamaño máximo de entrada
    mov ah, 0Ah
    int 21h

    xor ax, ax
    xor bx, bx
    xor cx, cx
    xor dx, dx
    xor si, si

    lea si, buffer+2               ; Primer carácter ingresado
    mov cl, byte ptr buffer+1      ; Número de caracteres ingresados

    ; Verificar si hay signo
    mov bl, byte ptr [si]
    cmp bl, '-'
    jne check_positive
    mov signo, 1                      ; bl = 1 indica negativo
    
    
    inc si
    dec cl
    jmp next_char

    check_positive:
        cmp bl, '+'
        jne next_char
        inc si
        dec cl

    next_char:
        xor ax, ax
        mov numero, 0

    convertirEtd:
        cmp cl, 0
        je done
        mov bl, [si]
        cmp bl, '0'
        jb salirerror
        cmp bl, '9'
        ja salirerror

        sub bl, '0'            ; Convertir de ASCII a número
        mov ax, numero
        push cx
        mov cx, 10
        mul cx                 ; ax = numero * 10
        pop cx
        mov bh,0
        add ax, bx             ; + nuevo dígito
        mov numero, ax

        inc si
        dec cl
        jmp convertirEtd

    done:
       
        cmp signo, 1
        jne exit
        ; Si era negativo
        mov ax, numero
        neg ax
        mov numero, ax

    exit:
        pop si
        pop dx
        pop cx
        pop bx
        pop ax
        mov ax,numero
        ret

    salirerror:
        lea dx, msg_error
        mov ah, 09h
        int 21h
        mov ax, 4C00h
        int 21h

EtdInt EndP


SalInt Proc

    push AX
    push BX
    push CX
    push DX


    
    ; Guardar el signo
    mov cx, ax           ; Copiar AX a CX para no perderlo
    cmp ax, 0
    jge positivo

    ; Número negativo
    mov dl, '-'          ; Imprimir el signo negativo
    mov ah, 02h
    int 21h

    neg cx               ; Tomar el valor absoluto (CX = -CX)
    jmp convertir

    positivo:
        mov dl, '+'          ; Si querés mostrar el signo positivo, dejalo. Si no, omitilo esta línea y las siguientes dos.
        mov ah, 02h
        int 21h

    convertir:
        mov ax, cx           ; Poner el valor absoluto en AX
        xor cx, cx
        mov bx, Base

        ; Convertir el número a ASCII (como antes)
    ciclo1PAX:
        xor dx, dx
        div bx
        push dx
        inc cx
        cmp ax, 0
        jne ciclo1PAX

        mov ah, 02h
    ciclo2PAX:
        pop DX
        add dl, 30h
        int 21h
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
    





    
    

    push ax
    call CamLin
    mov ah, 09h
    lea dx, msg_result
    int 21h
    pop ax
    
    call SalInt    





    salir: mov ax, 4C00h   ; Protocolo de finalizaci�n del programa
        int 21h 

codigo ends

end main