; =============================================================
; Lee un booleano (0 o 1) desde la línea de comandos y mostrarlo en pantalla.
; =============================================================

datos segment
    buffer db 128 dup(?)  ; Buffer para almacenar la entrada
    msg_true db 'Encendido', 0Dh, 0Ah, '$'  ; Mensaje si el valor es 1
    msg_false db 'Apagado', 0Dh, 0Ah, '$'   ; Mensaje si el valor es 0
    msg_invalid db 'Valor inválido', 0Dh, 0Ah, '$'  ; Mensaje si no es 0 o 1
datos ends

pila segment stack 'stack'
    dw 256 dup(?)
pila ends

codigo segment
    assume cs:codigo, ds:datos, ss:pila

inicio:
    mov ax, datos  ; Inicializar segmento de datos
    mov ds, ax
    mov ax, pila   ; Inicializar pila
    mov ss, ax

    ; Acceder a la PSP (Program Segment Prefix) para obtener argumentos
    mov es, ax
    mov si, 80h
    xor ch, ch
    mov cl, byte ptr es:[si]  ; Obtener la cantidad de caracteres ingresados
    cmp cl, 0
    je fin                    ; Si no hay entrada, salir

    dec cx
    inc si
    xor di, di

ciclo:
    inc si
    mov al, byte ptr es:[si]
    mov byte ptr buffer[di], al
    inc di
    loop ciclo

    ; Agregar fin de cadena
    mov byte ptr buffer[di], '$'

    ; Validar si el valor ingresado es '0' o '1'
    mov al, buffer[0]
    cmp al, '0'
    je es_falso
    cmp al, '1'
    je es_verdadero
    jmp invalido

es_verdadero:
    mov ah, 09h
    lea dx, msg_true
    int 21h
    jmp fin

es_falso:
    mov ah, 09h
    lea dx, msg_false
    int 21h
    jmp fin

invalido:
    mov ah, 09h
    lea dx, msg_invalid
    int 21h

fin:
    ; Salida del programa
    mov ax, 4C00h
    int 21h

codigo ends
end inicio
