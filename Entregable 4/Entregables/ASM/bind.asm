; =============================================================
; Te piede 2 entrada string, las concatena y te desplega el resultado
; =============================================================
datos segment
    concat  db 127          ; longitud máxima (hasta 127 caracteres)
    countconcat   db 0            ; número de caracteres realmente leídos
    cadenaconcat  db 128 dup(?)  

    buffer  db 63          ; longitud máxima (hasta 127 caracteres)
    count   db ?            ; número de caracteres realmente leídos
    cadena  db 64 dup(?)   ; espacio para la cadena
    
    buffer2  db 63          ; longitud máxima (hasta 127 caracteres)
    count2   db ?            ; número de caracteres realmente leídos
    cadena2  db 64 dup(?) 

    
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

    lea dx, buffer2
    mov ah, 0Ah
    int 21h

    pop dx
    pop ax
    ret
EtdString endp

EtdString2 proc
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
EtdString2 endp





Bind proc
    pop ax
    pop bx
    pop di
    push ax
    xor cx,cx
    mov cl, count2    ; número de caracteres leídos
    lea di, cadena2
    lea si, cadenaconcat    ; SI apunta al inicio de la cadena
    mov byte ptr [concat+1],cl
    xor ax,ax
    contar:
        cmp cx, 0
        je finPush

        ;inc ax           ; limpia AX
        ;mov al, [si]            ; mueve carácter actual a AL
        mov al, [di]
        mov [si], al
        ;mov byte ptr [si],[di]
        inc si
        inc di
        dec cx
        jmp contar

    finPush:
    xor cx,cx
    mov cl, count    ; número de caracteres leídos
    lea di, cadena
    add byte ptr [concat+1],cl
    xor ax,ax
    contar2:
        cmp cx, 0
        je finPush2

        ;inc ax           ; limpia AX
        ;mov al, [si]            ; mueve carácter actual a AL
        mov al, [di]
        mov [si], al
        ;mov byte ptr [si],[di]
        inc si
        inc di
        dec cx
        jmp contar2

    finPush2:
    mov byte ptr [si],"$"

        
    ret



Bind endp





SalString proc
    push ax
    push bx
    push cx
    push dx
    push si

    ; Imprimir carácter por carácter
    lea si, cadenaconcat
    mov cl, countconcat
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
    call EtdString2
    push offset buffer2
    push offset buffer
    call Bind
    push ax
    call CamLin
    mov ah, 09h
    lea dx, msg_result
    int 21h
    pop ax

    call SalString

    mov ax, 4C00h
    int 21h
codigo ends
end main
