; =============================================================
; Lee una temperatura desde la línea de comandos y mostrarla en pantalla
; Ejemplo: temperat 12C
; =============================================================

datos segment
    buffer db 10 dup(?)  ; Buffer para almacenar la entrada (máx 9 caracteres + NULL)
    new_line db 0Dh, 0Ah, '$'  ; Salto de línea
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
    mov sp, 256

    ; Acceder a PSP (Program Segment Prefix) para obtener argumentos
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
    mov al, byte ptr es:[si]
    cmp al, 20h  ; Verifica si es un espacio
    je fin       ; Si encuentra un espacio extra, termina
    mov byte ptr buffer[di], al
    inc si
    inc di
    loop ciclo

    ; Agregar fin de cadena
    mov byte ptr buffer[di], '$'

    ; Imprimir la temperatura ingresada
    mov ah, 09h
    lea dx, buffer
    int 21h

    ; Salto de línea
    lea dx, new_line
    int 21h

fin:
    ; Salida del programa
    mov ax, 4C00h
    int 21h

codigo ends
end inicio
