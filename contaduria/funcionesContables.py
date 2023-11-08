# Módulo de registracion contable
# ADEMA

from .models import CuentaContable, AsientoContable


def registrar_compra(monto, proveedor, fecha):

    cuenta_compras = CuentaContable.objects.get(cuenta="501")
    cuenta_caja = CuentaContable.objects.get(cuenta="101")

    # Generar asiento contable
    asiento = AsientoContable.objects.create(
        fecha=fecha,
        cuenta=cuenta_compras,
        descripcion="Compra de mercaderías",
        importe=monto,
    )
    asiento.save()

    # Generar segundo asiento contable para el pago en efectivo
    asiento_caja = AsientoContable.objects.create(
        fecha=fecha,
        cuenta=cuenta_caja,
        descripcion=f"Pago en efectivo a {proveedor}",
        importe=-monto,
    )
    asiento_caja.save()

def registrar_venta(monto, cliente, fecha):
    cuenta_ventas = CuentaContable.objects.get(cuenta="401")
    cuenta_caja = CuentaContable.objects.get(cuenta="101")

    # Generar asiento contable
    asiento = AsientoContable.objects.create(
        fecha=fecha,
        cuenta=cuenta_ventas,
        descripcion="Venta de mercaderías",
        importe=monto,
    )
    asiento.save()

    # Generar segundo asiento contable para el pago en efectivo
    asiento_caja = AsientoContable.objects.create(
        fecha=fecha,
        cuenta=cuenta_caja,
        descripcion=f"Venta a {cliente}",
        importe=monto,
    )
    asiento_caja.save()

def registrar_gasto(monto, descripcion, fecha, cuenta_de_gasto):
    cuenta_gasto = CuentaContable.objects.get(cuenta=cuenta_de_gasto)
    cuenta_caja = CuentaContable.objects.get(cuenta="101")

    # Generar asiento contable
    asiento_gasto = AsientoContable.objects.create(
        fecha=fecha,
        cuenta=cuenta_gasto,
        descripcion=descripcion,
        importe=monto,
    )
    asiento_gasto.save()

    # Generar segundo asiento contable para el pago en efectivo
    asiento_caja = AsientoContable.objects.create(
        fecha=fecha,
        cuenta=cuenta_caja,
        descripcion=f"Pago de {descripcion}",
        importe=-monto,
    )
    asiento_caja.save()

def registrar_retiro_efectivo(monto, fecha):
    cuenta_retiros = CuentaContable.objects.get(cuenta="901")
    cuenta_caja = CuentaContable.objects.get(cuenta="101")

    # Generar asiento contable de retiro de efectivo
    asiento_retiro = AsientoContable.objects.create(
        fecha=fecha,
        cuenta=cuenta_retiros,
        descripcion="Retiro de efectivo para uso personal",
        importe=-monto,
    )
    asiento_retiro.save()

    # Generar segundo asiento contable para la disminución de caja
    asiento_caja = AsientoContable.objects.create(
        fecha=fecha,
        cuenta=cuenta_caja,
        descripcion="Retiro de efectivo para uso personal",
        importe=-monto,
    )
    asiento_caja.save()

def registrar_intereses(monto, descripcion, fecha, cuenta_de_ingreso):
    cuenta_ingreso = CuentaContable.objects.get(cuenta=cuenta_de_ingreso)
    cuenta_caja = CuentaContable.objects.get(cuenta="101")

    # Generar asiento contable de ingreso por intereses
    asiento_ingreso = AsientoContable.objects.create(
        fecha=fecha,
        cuenta=cuenta_ingreso,
        descripcion=descripcion,
        importe=monto,
    )
    asiento_ingreso.save()

    # Generar segundo asiento contable para el aumento de caja
    asiento_caja = AsientoContable.objects.create(
        fecha=fecha,
        cuenta=cuenta_caja,
        descripcion=f"Recepción de ingresos por {descripcion}",
        importe=monto,
    )
    asiento_caja.save()
