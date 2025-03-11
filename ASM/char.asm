; =============================================================
; Lee un carácter desde la entrada estándar y mostrarlo en pantalla.
; =============================================================

datos segment
    msg_in db 'Ingrese un caracter: $'
    char db ?  ; Espacio para almacenar el carácter
    msg_out db 'Caracter ingresado: $'
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

    ; Leer un solo carácter
    mov ah, 01h
    int 21h
    mov char, al  ; Almacenar el carácter leído

    ; Salto de línea
    lea dx, new_line
    int 21h

    ; Imprimir mensaje de salida
    mov ah, 09h
    lea dx, msg_out
    int 21h

    ; Imprimir el carácter ingresado
    mov ah, 02h
    mov dl, char
    int 21h

    ; Salto de línea
    lea dx, new_line
    int 21h

    ; Salida del programa
    mov ax, 4C00h
    int 21h  

codigo ends
end main
