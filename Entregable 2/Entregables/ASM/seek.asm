; =============================================================
; Te piede 2 entrada string, comprueba si la segunda esta dentro de la primera y te desplega un booleano
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
    noesta db 'no esta $'
    siesta db 'si esta $'

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





Seek proc
    pop ax
    pop bx
    pop di
    push ax
    buscar_subcadena:
        ; DI = dirección de cadena
        ; SI = dirección de cadena2
        ; CL = longitud de cadena
        ; DL = longitud de cadena2

        lea di, cadena+2          ; inicio de cadena
        lea si, cadena2+2         ; inicio de cadena2
        mov cl, [cadena+1]        ; longitud de cadena
        mov dl, [cadena2+1]       ; longitud de cadena2

        xor bx, bx                ; índice en cadena (BX)
    buscar_loop:
        cmp bx, cx
        jae no_encontrado         ; si índice >= longitud cadena, termina

        push bx                   ; guardar índice actual
        push di
        push si

        mov dh, dl                ; contador interno de comparación
        lea si, cadena2+2
        lea di, [cadena+2+bx]     ; empieza desde BX en cadena

        comparar:
            cmp dh, 0
            je encontrado             ; si terminó de comparar, encontró

            mov al, [si]
            cmp al, [di]
            jne no_match              ; si no coinciden, salir

            inc si
            inc di
            dec dh
            jmp comparar

        no_match:
            pop si
            pop di
            pop bx
            inc bx
        jmp buscar_loop

    encontrado:
        ; Subcadena encontrada
        ; Aquí puedes hacer lo que quieras, por ejemplo mostrar mensaje
        pop si
        pop di
        pop bx
        mov ax,1
        jmp fin_busqueda

    no_encontrado:
        ; No se encontró
        mov ax,0
        ; Aquí puedes poner otro mensaje
    fin_busqueda:
    ret


Seek endp



SalBool proc
    
        mov dl, al
        add dl,'0'
        mov ah, 02h
        int 21h

        ret
SalBool endp

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
    call Seek
    push ax
    call CamLin
    mov ah, 09h
    lea dx, msg_result
    int 21h
    pop ax

    call SalBool

    mov ax, 4C00h
    int 21h
codigo ends
end main
