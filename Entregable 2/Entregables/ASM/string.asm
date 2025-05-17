; =============================================================
; Te piede 1 entrada string y te lo desplega
; =============================================================

datos segment
    buffer  db 127          ; longitud máxima (hasta 127 caracteres)
    count   db ?            ; número de caracteres realmente leídos
    cadena  db 128 dup(?)   ; espacio para la cadena

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

main:
    mov ax, datos
    mov ds, ax
    mov ax, pila
    mov ss, ax

    call EtdString

    call CamLin
    mov ah, 09h
    lea dx, msg_result
    int 21h

    call SalString

    mov ax, 4C00h
    int 21h
codigo ends
end main
