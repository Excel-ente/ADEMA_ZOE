from django.contrib import admin
from .models import Categoria,Familia,Cliente,Proveedor,MedioDeCompra,MedioDePago
from inventario.models import Producto
from contaduria.models import cuentasContables
from recursos_humanos.models import Empleado
from django.contrib.auth.models import User

@admin.action(description="Crear datos de ejemplo")
def CrearDataEjemplo(modeladmin, request, queryset):
        # ------------------------------------------------------ CREACION DE MODELOS ADMINISTRACION
        # CREACION DE CATEGORIAS
        ALMACEN = Categoria.objects.create(nombre='ALMACEN',)
        BEBIDAS_SIN_ALCOHOL = Categoria.objects.create(nombre='BEBIDAS SIN ALCOHOL',)
        BEBIDAS_CON_ALCOHOL = Categoria.objects.create(nombre='BEBIDAS CON ALCOHOL',)
        LIMPIEZA = Categoria.objects.create(nombre='LIMPIEZA',)
        PERFUMERIA = Categoria.objects.create(nombre='PERFUMERIA',)
        CARNICERIA = Categoria.objects.create(nombre='CARNICERIA',)
        PANADERIA = Categoria.objects.create(nombre='PANADERIA',)

        # CREACION DE CATEGORIAS
        Familia.objects.create(categoria=ALMACEN, nombre='YERBA',)
        Familia.objects.create(categoria=ALMACEN, nombre='AZUCAR',)
        Familia.objects.create(categoria=ALMACEN, nombre='FIDEOS',)
        Familia.objects.create(categoria=ALMACEN, nombre='LEGUMBRES',)
        Familia.objects.create(categoria=ALMACEN, nombre='SALSAS',)
        Familia.objects.create(categoria=ALMACEN, nombre='HARINAS',)
        Familia.objects.create(categoria=ALMACEN, nombre='ARROZ',)
        Familia.objects.create(categoria=ALMACEN, nombre='LACTEOS',)
        Familia.objects.create(categoria=ALMACEN, nombre='ACEITES',)
        Familia.objects.create(categoria=ALMACEN, nombre='CEREALES',)

        Familia.objects.create(categoria=BEBIDAS_SIN_ALCOHOL, nombre='GASEOSAS',)
        Familia.objects.create(categoria=BEBIDAS_SIN_ALCOHOL, nombre='AGUAS MINERALES',)
        Familia.objects.create(categoria=BEBIDAS_SIN_ALCOHOL, nombre='CERVEZAS',)

        Familia.objects.create(categoria=BEBIDAS_CON_ALCOHOL, nombre='GASEOSAS',)
        Familia.objects.create(categoria=BEBIDAS_CON_ALCOHOL, nombre='AGUAS MINERALES',)
        Familia.objects.create(categoria=BEBIDAS_CON_ALCOHOL, nombre='CERVEZAS',)

        Familia.objects.create(categoria=LIMPIEZA, nombre='PAPELES',)
        Familia.objects.create(categoria=LIMPIEZA, nombre='LIMPIADORES',)
        Familia.objects.create(categoria=LIMPIEZA, nombre='BOLSAS',)
        Familia.objects.create(categoria=LIMPIEZA, nombre='ARTEFACTOS DE LIMPIEZA',)

        Familia.objects.create(categoria=PERFUMERIA, nombre='CREMAS',)
        Familia.objects.create(categoria=PERFUMERIA, nombre='PERFUMES',)
        Familia.objects.create(categoria=PERFUMERIA, nombre='LIMPIEZA INTIMA',)
        Familia.objects.create(categoria=PERFUMERIA, nombre='HIGIENE BUCAL',)
        
        Familia.objects.create(categoria=CARNICERIA, nombre='CORTES',)

        Familia.objects.create(categoria=PANADERIA, nombre='PAN',)

        # Creacion de clientes
        Cliente.objects.create(nombre='Juan', apellido='Perez',direccion='Trunvirato 123, buenos aires',telefono='+54 11 1234 5678')
        Cliente.objects.create(nombre='Jeremias', apellido='Jera',direccion='Zumbique 123, buenos aires',telefono='+54 11 1234 5678')
        Cliente.objects.create(nombre='Andrea', apellido='Palmito',direccion='Esmeraldas 123, buenos aires',telefono='+54 11 1234 5678')

        # Creacion de proveedores
        Proveedor.objects.create(empresa='VyA Concentrados', nombre='David',direccion='Trunvirato 123, buenos aires',telefono='+54 11 1234 5678')
        Proveedor.objects.create(empresa='Tienda el Imbatible', nombre='Kevin',direccion='Zumbique 123, buenos aires',telefono='+54 11 1234 5678')
        Proveedor.objects.create(empresa='Bella Maga', nombre='Lucia',direccion='Esmeraldas 123, buenos aires',telefono='+54 11 1234 5678')

        # Creacion de plan de cuentas contable
        plan_de_cuentas = [
            # Cuenta, Tipo, Descripción, Activo
            (101, 'ACTIVO', 'CAJA', True),
            (102, 'ACTIVO', 'BANCOS', True),
            (103, 'ACTIVO', 'CUENTAS POR COBRAR (CLIENTES)', True),
            (104, 'ACTIVO', 'INVENTARIO DE MERCADERiA', True),
            (105, 'ACTIVO', 'OTROS ACTIVOS', True),
            (201, 'PASIVO', 'CUENTAS POR PAGAR (PROVEEDORES)', True),
            (202, 'PASIVO', 'DEUDAS POR CUENTAS CORRIENTES', True),
            (203, 'PASIVO', 'PRESTAMOS A CORTO PLAZO', True),
            (204, 'PASIVO', 'PRESTAMOS A LARGO PLAZO', True),
            (205, 'PASIVO', 'OTROS PASIVOS', True),
            (301, 'PATRIMONIO NETO', 'CAPITAL SOCIAL', True),
            (302, 'PATRIMONIO NETO', 'RESULTADOS ACUMULADOS', True),
            (401, 'INGRESOS', 'VENTAS DE MERCADERIAS', True),
            (501, 'COSTOS DE VENTAS', 'COMPRAS DE MERCADERIAS', True),
            (601, 'GASTOS OPERATIVOS', 'GASTOS DE SUELDOS', True),
            (602, 'GASTOS OPERATIVOS', 'GASTOS DE ALQUILER', True),
            (603, 'GASTOS OPERATIVOS', 'GASTOS DE PUBLICIDAD', True),
            (604, 'GASTOS OPERATIVOS', 'OTROS GASTOS OPERATIVOS', True),
            (701, 'OTROS INGRESOS', 'INTERESES GANADOS', True),
            (702, 'OTROS INGRESOS', 'OTROS INGRESOS', True),
            (801, 'OTROS GASTOS', 'INTERESES PAGADOS', True),
            (802, 'OTROS GASTOS', 'OTROS GASTOS FINANCIEROS', True),
            (901, 'RETIROS DE EFECTIVO', 'RETIROS DE EFECTIVO', True),
        ]
        for cuenta, tipo, descripcion, activo in plan_de_cuentas:
            cuentasContables.objects.create(cuenta=cuenta, tipo=tipo, descripcion=descripcion, estado=activo)


        # Creación de medios de compra (medios con los que pagarás las compras)
        MedioDeCompra.objects.create(cuenta=cuentasContables.objects.get(cuenta=101), nombre='Efectivo prove')
        MedioDeCompra.objects.create(cuenta=cuentasContables.objects.get(cuenta=102), nombre='Transferencia prove')
        MedioDeCompra.objects.create(cuenta=cuentasContables.objects.get(cuenta=102), nombre='Cuenta Corriente prove')

        # Creación de medios de pago (medios con los que tus clientes te pagarán)
        MedioDePago.objects.create(cuenta=cuentasContables.objects.get(cuenta=103), nombre='Efectivo cliente')
        MedioDePago.objects.create(cuenta=cuentasContables.objects.get(cuenta=103), nombre='Transferencia cliente')
        MedioDePago.objects.create(cuenta=cuentasContables.objects.get(cuenta=103), nombre='Cuenta Corriente cliente')

       # for producto in productos_ejemplo:
        Producto.objects.create(codigo='001', nombre='Yerba Mate Clásica', descripcion='Yerba para mate, 500g', en_stock=100, costo=5.99, categoria=Categoria.objects.get(nombre='ALMACEN'), Proveedor=Proveedor.objects.get(empresa='VyA Concentrados'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='ALMACEN'), nombre='YERBA'), unidades_por_caja=12, habilitar_caja=True)
        Producto.objects.create(codigo='002', nombre='Gaseosa de Naranja', descripcion='Bebida refrescante de naranja, 2L', en_stock=50, costo=2.49, categoria=Categoria.objects.get(nombre='BEBIDAS SIN ALCOHOL'), Proveedor=Proveedor.objects.get(empresa='Tienda el Imbatible'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='BEBIDAS SIN ALCOHOL'), nombre='GASEOSAS'), unidades_por_caja=6, habilitar_caja=False)
        Producto.objects.create(codigo='003', nombre='Cerveza Artesanal IPA', descripcion='Cerveza artesanal estilo IPA, 330ml', en_stock=30, costo=4.99, categoria=Categoria.objects.get(nombre='BEBIDAS CON ALCOHOL'), Proveedor=Proveedor.objects.get(empresa='Bella Maga'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='BEBIDAS CON ALCOHOL'), nombre='CERVEZAS'), unidades_por_caja=6, habilitar_caja=False)
        Producto.objects.create(codigo='004', nombre='Limpiador Multiusos', descripcion='Limpiador multiusos, 1L', en_stock=60, costo=3.99, categoria=Categoria.objects.get(nombre='LIMPIEZA'), Proveedor=Proveedor.objects.get(empresa='VyA Concentrados'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='LIMPIEZA'), nombre='LIMPIADORES'), unidades_por_caja=3, habilitar_caja=True)
        Producto.objects.create(codigo='005', nombre='Perfume Floral', descripcion='Perfume floral en aerosol, 50ml', en_stock=80, costo=12.99, categoria=Categoria.objects.get(nombre='PERFUMERIA'), Proveedor=Proveedor.objects.get(empresa='Bella Maga'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='PERFUMERIA'), nombre='PERFUMES'), unidades_por_caja=6, habilitar_caja=True)
        Producto.objects.create(codigo='006', nombre='Filete de Ternera', descripcion='Filete de ternera, 200g', en_stock=40, costo=7.49, categoria=Categoria.objects.get(nombre='CARNICERIA'), Proveedor=Proveedor.objects.get(empresa='VyA Concentrados'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='CARNICERIA'), nombre='CORTES'), unidades_por_caja=1, habilitar_caja=False)
        Producto.objects.create(codigo='007', nombre='Pan Integral', descripcion='Pan integral fresco, 500g', en_stock=120, costo=2.99, categoria=Categoria.objects.get(nombre='PANADERIA'), Proveedor=Proveedor.objects.get(empresa='Tienda el Imbatible'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='PANADERIA'), nombre='PAN'), unidades_por_caja=3, habilitar_caja=True)
        Producto.objects.create(codigo='008', nombre='Papel Higiénico Suave', descripcion='Rollo de papel higiénico suave, 4 unidades', en_stock=150, costo=6.99, categoria=Categoria.objects.get(nombre='LIMPIEZA'), Proveedor=Proveedor.objects.get(empresa='VyA Concentrados'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='LIMPIEZA'), nombre='PAPELES'), unidades_por_caja=4, habilitar_caja=False)
        Producto.objects.create(codigo='009', nombre='Shampoo Revitalizante', descripcion='Shampoo revitalizante para cabello, 300ml', en_stock=70, costo=8.49, categoria=Categoria.objects.get(nombre='PERFUMERIA'), Proveedor=Proveedor.objects.get(empresa='VyA Concentrados'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='PERFUMERIA'), nombre='CREMAS'), unidades_por_caja=3, habilitar_caja=True)
        Producto.objects.create(codigo='010', nombre='Jabón de Lavandería', descripcion='Jabón para lavandería, 1kg', en_stock=90, costo=4.29, categoria=Categoria.objects.get(nombre='LIMPIEZA'), Proveedor=Proveedor.objects.get(empresa='Bella Maga'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='LIMPIEZA'), nombre='ARTEFACTOS DE LIMPIEZA'), unidades_por_caja=1, habilitar_caja=False)
        Producto.objects.create(codigo='011', nombre='Leche Desnatada', descripcion='Leche desnatada, 1L', en_stock=110, costo=2.99, categoria=Categoria.objects.get(nombre='ALMACEN'), Proveedor=Proveedor.objects.get(empresa='VyA Concentrados'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='ALMACEN'), nombre='LACTEOS'), unidades_por_caja=6, habilitar_caja=True)
        Producto.objects.create(codigo='012', nombre='Cereal de Avena', descripcion='Cereal de avena, 500g', en_stock=65, costo=3.79, categoria=Categoria.objects.get(nombre='ALMACEN'), Proveedor=Proveedor.objects.get(empresa='Bella Maga'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='ALMACEN'), nombre='CEREALES'), unidades_por_caja=3, habilitar_caja=False)
        Producto.objects.create(codigo='013', nombre='Cepillo de Dientes', descripcion='Cepillo de dientes suave', en_stock=200, costo=1.49, categoria=Categoria.objects.get(nombre='PERFUMERIA'), Proveedor=Proveedor.objects.get(empresa='VyA Concentrados'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='PERFUMERIA'), nombre='HIGIENE BUCAL'), unidades_por_caja=12, habilitar_caja=True)
        Producto.objects.create(codigo='014', nombre='Detergente Líquido', descripcion='Detergente líquido concentrado, 1L', en_stock=85, costo=3.99, categoria=Categoria.objects.get(nombre='LIMPIEZA'), Proveedor=Proveedor.objects.get(empresa='Tienda el Imbatible'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='LIMPIEZA'), nombre='LIMPIADORES'), unidades_por_caja=6, habilitar_caja=True)
        Producto.objects.create(codigo='015', nombre='Loción Corporal', descripcion='Loción corporal hidratante, 250ml', en_stock=75, costo=5.49, categoria=Categoria.objects.get(nombre='PERFUMERIA'), Proveedor=Proveedor.objects.get(empresa='Bella Maga'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='PERFUMERIA'), nombre='CREMAS'), unidades_por_caja=1, habilitar_caja=False)
        Producto.objects.create(codigo='016', nombre='Pasta de Dientes', descripcion='Pasta de dientes con flúor, 150g', en_stock=120, costo=2.99, categoria=Categoria.objects.get(nombre='PERFUMERIA'), Proveedor=Proveedor.objects.get(empresa='VyA Concentrados'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='PERFUMERIA'), nombre='HIGIENE BUCAL'), unidades_por_caja=6, habilitar_caja=False)
        Producto.objects.create(codigo='017', nombre='Aceite de Oliva Extra Virgen', descripcion='Aceite de oliva extra virgen, 500ml', en_stock=50, costo=7.99, categoria=Categoria.objects.get(nombre='ALMACEN'), Proveedor=Proveedor.objects.get(empresa='Tienda el Imbatible'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='ALMACEN'), nombre='ACEITES'), unidades_por_caja=1, habilitar_caja=False)
        Producto.objects.create(codigo='018', nombre='Detergente en Polvo', descripcion='Detergente en polvo, 2kg', en_stock=90, costo=5.99, categoria=Categoria.objects.get(nombre='LIMPIEZA'), Proveedor=Proveedor.objects.get(empresa='VyA Concentrados'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='LIMPIEZA'), nombre='LIMPIADORES'), unidades_por_caja=3, habilitar_caja=True)
        Producto.objects.create(codigo='019', nombre='Champú Anticaspa', descripcion='Champú anticaspa, 400ml', en_stock=70, costo=4.49, categoria=Categoria.objects.get(nombre='PERFUMERIA'), Proveedor=Proveedor.objects.get(empresa='Bella Maga'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='PERFUMERIA'), nombre='CREMAS'), unidades_por_caja=6, habilitar_caja=True)
        Producto.objects.create(codigo='020', nombre='Jabón de Tocador', descripcion='Jabón de tocador, paquete de 4 unidades', en_stock=130, costo=2.79, categoria=Categoria.objects.get(nombre='PERFUMERIA'), Proveedor=Proveedor.objects.get(empresa='Tienda el Imbatible'), familia=Familia.objects.get(categoria=Categoria.objects.get(nombre='PERFUMERIA'), nombre='HIGIENE BUCAL'), unidades_por_caja=12, habilitar_caja=False)

        # Crear 5 empleados/usuarios
        empleados = [
            {
                'legajo': '001',
                'user': User.objects.create_user(username='AlanG', ),
                'nombre': 'Alan',
                'apellido': 'Gomez',
                'email': 'Alan.Gomez@adema.com',
            },
            {
                'legajo': '002',
                'user': User.objects.create_user(username='SofiaP', ),
                'nombre': 'Sofia',
                'apellido': 'Perez',
                'email': 'Sofia.Perez@adema.com',
            },
            {
                'legajo': '003',
                'user': User.objects.create_user(username='MarielL', ),
                'nombre': 'Mariel',
                'apellido': 'Lester',
                'email': 'Mariel.Lester@adema.com',
            },
            {
                'legajo': '004',
                'user': User.objects.create_user(username='LucianoO', ),
                'nombre': 'Luciano',
                'apellido': 'Ortiz',
                'email': 'Luciano.Ortiz@adema.com',
            },
            {
                'legajo': '005',
                'user': User.objects.create_user(username='MaxiF', ),
                'nombre': 'Maxi',
                'apellido': 'Franquez',
                'email': 'Maxi.Franquez@adema.com',
            },
        ]
        for empleado_data in empleados:
            Empleado.objects.create(**empleado_data)




