; =============================================================
; Lee una cadena de caracteres desde la entrada estándar y mostrarla en pantalla.
; =============================================================

datos segment
    msg_in db 'Ingrese una cadena: $'
    buffer db 30, ?, 30 dup(0)  ; Buffer para entrada (máx 29 caracteres + null)
    msg_out db 'Cadena ingresada: $'
    new_line db 0Dh, 0Ah, '$'  ; Salto de línea
datos ends

pila segment stack 'stack'
    dw 256 dup(?)
pila ends

codigo segment
    assume cs: codigo, ds: datos, ss: pila

main:
    ; Inicializar segmentos
    mov ax, datos
    mov ds, ax
    mov ax, pila
    mov ss, ax
    mov sp, 256

    ; Mostrar mensaje de entrada
    mov ah, 09h
    lea dx, msg_in
    int 21h

    ; Leer cadena de caracteres
    mov ah, 0Ah
    lea dx, buffer
    int 21h

    ; Agregar fin de cadena al buffer para impresión
    mov al, buffer+1   ; AL contiene la cantidad de caracteres ingresados
    add al, 2          ; Ajustar la posición correcta dentro del buffer
    mov si, ax         ; Mover a SI para indexar correctamente
    mov byte ptr buffer[si], '$'  ; Colocar fin de cadena

    ; Salto de línea
    lea dx, new_line
    int 21h

    ; Imprimir mensaje de salida
    mov ah, 09h
    lea dx, msg_out
    int 21h

    ; Imprimir la cadena ingresada
    mov ah, 09h
    lea dx, buffer+2
    int 21h

    ; Salto de línea
    lea dx, new_line
    int 21h

    ; Salida del programa
    mov ax, 4C00h
    int 21h  

codigo ends
end main
