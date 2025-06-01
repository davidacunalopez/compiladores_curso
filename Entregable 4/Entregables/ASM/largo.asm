; =============================================================
; Te piede 1 entrada string,cacula el largo y te lo desplega
; =============================================================

datos segment
    buffer  db 127          ; longitud máxima (hasta 127 caracteres)
    count   db ?            ; número de caracteres realmente leídos
    cadena  db 128 dup(?)   ; espacio para la cadena
    Base dw 10
    msg_error   db 'No es un numero valido', 0Dh, 0Ah, '$'
    msg_soldato db 'Ingresa una cadena: $'
    msg_result  db 13,10,'Resultado: $'

datos ends

pila segment stack 'stack'
    dw 256 dup(?)
pila ends

codigo segment
    assume cs:codigo, ds:datos, ss:pila

CamLin proc
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
CamLin endp

EtdString proc
    push ax
    push dx

    mov ah, 09h
    lea dx, msg_soldato
    int 21h

    lea dx, buffer
    mov ah, 0Ah
    int 21h

    pop dx
    pop ax
    ret
EtdString endp







largo proc

    
    mov cl, [bx + 1]    ; número de caracteres leídos
    mov ch, 0               ; CX = número de caracteres
    lea si, [bx + 2]    ; SI apunta al inicio de la cadena
    xor ax,ax
    contar:
        cmp cx, 0
        je finPush

        inc ax           ; limpia AX
        ;mov al, [si]            ; mueve carácter actual a AL
                         ; lo pone en la pila (16 bits)
        inc si
        dec cx
        jmp contar

    finPush:

        
    ret



largo endp





SalString proc
    push ax
    push bx
    push cx
    push dx
    push si

    ; Imprimir carácter por carácter
    lea si, cadena
    mov cl, count
    mov ch, 0

    imprimir:
        cmp cx, 0
        je fin
        mov dl, [si]
        mov ah, 02h
        int 21h
        inc si
        dec cx
        jmp imprimir

    fin:
        pop si
        pop dx
        pop cx
        pop bx
        pop ax
        ret
SalString endp

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
    mov ax, datos
    mov ds, ax
    mov ax, pila
    mov ss, ax

    call EtdString
    mov bx,offset buffer


    call CamLin
    call largo
    push ax
    call CamLin
    mov ah, 09h
    lea dx, msg_result
    int 21h
    pop ax

    call SalInt

    mov ax, 4C00h
    int 21h
codigo ends
end main
