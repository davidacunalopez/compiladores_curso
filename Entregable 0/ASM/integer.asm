; =============================================================
; Lee un número entero desde la entrada estándar y mostrarlo en pantalla.
; =============================================================

datos segment
    msg_in db 'Ingrese un numero entero: $'
    buffer db 6, ?, 6 dup(0)  ; Buffer para entrada (máx 5 dígitos + null)
    msg_out db 'Numero ingresado: $'
    new_line db 0Dh, 0Ah, '$'  ; Salto de línea
datos ends

pila segment stack 'stack'
    dw 256 dup(?)
pila ends

codigo segment
    assume cs: codigo, ds: datos, ss: pila

main:
    ; Inicialización de segmentos
    mov ax, datos
    mov ds, ax
    mov ax, pila
    mov ss, ax
    mov sp, 256

    ; Mostrar mensaje de entrada
    mov ah, 09h
    lea dx, msg_in
    int 21h

    ; Leer número desde teclado
    mov ah, 0Ah
    lea dx, buffer
    int 21h

    ; Agregar fin de cadena al buffer para impresión
    mov al, buffer+1   ; AL contiene la cantidad de caracteres ingresados
    add al, 2          ; Ajustar la posición correcta dentro del buffer
    mov si, ax         ; Mover a SI para indexar correctamente
    mov byte ptr buffer[si], '$'  ; Colocar fin de cadena

    ; Imprimir mensaje de salida
    mov ah, 09h
    lea dx, msg_out
    int 21h

    ; Imprimir el número ingresado
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
