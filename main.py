def leer_datos(datos: list):
    assert len(datos) == 2, 'Cantidad incorrecta de datos'
    datos[0] = input('Ingrese precio: ')
    datos[1] = input('Ingrese cantidad: ')

if __name__ == '__main__':
    print('Bienvenido!')

    datos = [
        0, # Precio
        0  # Cantidad
    ]

    leer_datos(datos)

    precio = datos[0]
    cantidad = datos[1]

    print('Comprobando:')
    print(f'- precio: {precio}')
    print(f'- cantidad: {cantidad}')