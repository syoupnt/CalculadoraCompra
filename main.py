def leer_datos(datos: list):
    assert len(datos) == 2, 'Cantidad incorrecta de datos'
    datos[0] = float(input('Ingrese precio (S/): '))
    datos[1] = float(input('Ingrese cantidad:    '))

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_descuento(subtotal):
    return .1 * subtotal

if __name__ == '__main__':
    print('Bienvenido!\n')

    datos = [
        0, # Precio
        0  # Cantidad
    ]

    leer_datos(datos)

    precio = datos[0]
    cantidad = datos[1]

    print('\nComprobando:')
    print(f'- precio:   S/{precio}')
    print(f'- cantidad: {cantidad}')

    subtotal = calcular_subtotal(precio, cantidad)
    descuento = calcular_descuento(subtotal)
    total = subtotal - descuento

    print('\nResultados:')
    print(s1:=f'+ subtotal:  +S/{subtotal}')
    print(s2:=f'- descuento: -S/{descuento}')
    print('-' * max(len(s1), len(s2)))
    print(f'* Total:        {total}')
    print()