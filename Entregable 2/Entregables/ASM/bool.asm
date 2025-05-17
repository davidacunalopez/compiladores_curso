; =============================================================
; Te piede 1 entrada booleana y te lo desplega
; =============================================================
datos segment
    buffer  db 127          ; longitud máxima (hasta 127 caracteres)
    count   db ?            ; número de caracteres realmente leídos
    cadena  db 128 dup(?)   ; espacio para la cadena

    msg_error   db 'No es un numero valido', 0Dh, 0Ah, '$'
    msg_soldato db 'Ingresa un dato: $'
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

EtdBool proc


    mov ah, 09h
    lea dx, msg_soldato
    int 21h

    lea dx, buffer
    mov ah, 0Ah
    int 21h



    lea si, buffer+2
    xor ch, ch
    mov cl, [buffer+1]  ; Obtener la cantidad de caracteres ingresados
    cmp cl, 0
    je es_falso                    ; Si no hay entrada, salir



    
    xor di, di

    cicloLectura:
        
        mov al, [si]
        cmp al,'0'
        jne es_verdadero
        inc si
        loop cicloLectura
    jmp es_falso        
    es_verdadero:
        mov ax, 1
        jmp finEtd

    es_falso:
        mov ax, 0
        jmp finEtd

    


       

    finEtd:  


    ret
EtdBool endp

SalBool proc
    
        mov dl, al
        add dl,'0'
        mov ah, 02h
        int 21h

        ret
SalBool endp

main:
    mov ax, datos
    mov ds, ax
    mov ax, pila
    mov ss, ax

    call EtdBool

    call CamLin
    mov ah, 09h
    lea dx, msg_result
    int 21h

    call SalBool

    mov ax, 4C00h
    int 21h
codigo ends
end main
