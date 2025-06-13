; --------------------------------------------------------
; C�digo generado por el compilador Notch Engine
; Fecha de generaci�n: 2025-06-13
; Este archivo ha sido generado autom�ticamente por el compilador.
; Autores: David Acu�a y Deylan Sandoval
; Materia: Compiladores e int�rpretes
; --------------------------------------------------------


pila segment stack 'stack'
    dw 4096 dup(?)  ; Espacio para la pila
pila ends

datos segment para public
    ; Variables globales
    VG_varEntero dw 2  ; Declaraci�n de la variable varEntero
datos ends

codigo segment
    assume cs:codigo, ds:datos
    ; Inicio del programa
    ; Operaci�n de suma varEntero = 9 + 2
    mov ax, VG_varEntero  ; Cargar la variable varEntero
    add ax, 9             ; Sumar 9
    add ax, 2             ; Sumar 2
    mov VG_varEntero, ax  ; Guardar el resultado en varEntero
    mov ah, 4Ch
    int 21h               ; Fin del programa
codigo ends
end etiqueta

