def leer_datos(datos: list):
    assert len(datos) == 2, 'Cantidad incorrecta de datos'
    datos[0] = float(input('Ingrese precio: '))
    datos[1] = float(input('Ingrese cantidad: '))

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

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
    print(f'- precio: {precio}')
    print(f'- cantidad: {cantidad}')

    subtotal = calcular_subtotal(precio, cantidad)

    print('\nResultados:')
    print(f'+ subtotal: {subtotal}\n')