; =============================================================
; Te piede 1 entrada string,2 entradas enteros, calcula el string entre el rango y te desplega el resultado
; =============================================================
datos segment
    concat  db 127          ; longitud máxima (hasta 127 caracteres)
    countconcat   db 0            ; número de caracteres realmente leídos
    cadenaconcat  db 128 dup(?)  

    buffer  db 127          ; longitud máxima (hasta 127 caracteres)
    count   db ?            ; número de caracteres realmente leídos
    cadena  db 128 dup(?)   ; espacio para la cadena

    buffer2 db 128 dup(?)
    numero    dw 0

    signo dw 0

    
    Base dw 10
    msg_error   db 'No es un numero valido', 0Dh, 0Ah, '$'
    msg_soldato db 'Ingresa una cadena: $'
    msg_soldato_num db 'Ingresa una numero: $'
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

EtdInt Proc
    push ax
    push bx
    push cx
    push dx
    push si
    mov signo,0
    ; Mostrar mensaje
    mov ah, 09h
    lea dx, msg_soldato_num
    int 21h

    ; Leer cadena
    lea dx, buffer2
    mov byte ptr buffer2, 5         ; Tamaño máximo de entrada
    mov ah, 0Ah
    int 21h

    xor ax, ax
    xor bx, bx
    xor cx, cx
    xor dx, dx
    xor si, si

    lea si, buffer2+2               ; Primer carácter ingresado
    mov cl, byte ptr buffer2+1      ; Número de caracteres ingresados

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





From proc
    pop di
    pop bx
    pop ax
    push di
    xor cx,cx
    mov cl, count    ; número de caracteres leídos
    lea di, cadena
    lea si, cadenaconcat    ; SI apunta al inicio de la cadena
    mov byte ptr [concat+1],0
    
    
    xor cx,cx
 
    contar:
        cmp cl, count
        jg finPush

        ;inc ax           ; limpia AX
        ;mov al, [si]            ; mueve carácter actual a AL
        cmp cx, ax          ; ¿CX >= min?
            jl ignorar      ; si es menor, salta

        cmp cx, bx          ; ¿CX <= max?
            jg ignorar      ; si es mayor, salta
        push ax
        mov al, [di]
        mov [si], al
        inc byte ptr [concat+1]
        pop ax

        
        ;mov byte ptr [si],[di]
        
        inc si
        ignorar: 
        inc di
        
        inc cx
        jmp contar

    finPush:
    
    mov byte ptr [si],"$"

        
    ret



From endp





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
    call EtdInt
    push ax
    call CamLin
    call EtdInt
    push ax
    call From
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
