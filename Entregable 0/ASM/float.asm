; =============================================================
; Lee un número flotante desde la línea de comandos y mostrarlo en pantalla.
; ==========================================================

datos segment
    buffer db 20 dup(?)  ; Buffer para almacenar la entrada (máx 19 caracteres + null)
    msg_invalid db 'Valor inválido', 0Dh, 0Ah, '$'  ; Mensaje si la entrada no es válida
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

    ; Acceder a PSP (Program Segment Prefix) para obtener argumentos
    mov es, ax
    mov si, 80h
    xor ch, ch
    mov cl, byte ptr es:[si]  ; Obtener la cantidad de caracteres ingresados
    cmp cl, 0
    je invalido               ; Si no hay entrada, error

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

    ; Imprimir el número flotante ingresado
    mov ah, 09h
    lea dx, buffer
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
