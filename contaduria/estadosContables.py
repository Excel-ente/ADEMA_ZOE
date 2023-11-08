from .models import AsientoContable,cuentasContables
from django.db import models

def estado_de_resultados(desde, hasta):
    ingresos = AsientoContable.objects.filter(fecha__range=(desde, hasta), cuenta__tipo='Ingresos').aggregate(total_ingresos=models.Sum('importe'))
    costos = AsientoContable.objects.filter(fecha__range=(desde, hasta), cuenta__tipo='Costos de Ventas').aggregate(total_costos=models.Sum('importe'))
    gastos = AsientoContable.objects.filter(fecha__range=(desde, hasta), cuenta__tipo='Gastos Operativos').aggregate(total_gastos=models.Sum('importe'))
    
    resultado_neto = (ingresos['total_ingresos'] or 0) - (costos['total_costos'] or 0) - (gastos['total_gastos'] or 0)
    
    return {
        "Ingresos": ingresos['total_ingresos'] or 0,
        "Costos": costos['total_costos'] or 0,
        "Gastos": gastos['total_gastos'] or 0,
        "Resultado Neto": resultado_neto,
    }


def balance_general(fecha):
    cuentas = cuentasContables.objects.all()
    saldo_total_activo = 0
    saldo_total_pasivo = 0
    saldo_total_patrimonio = 0
    
    for cuenta in cuentas:
        if cuenta.tipo == 'Activo':
            saldo_total_activo += obtener_saldo_cuenta(cuenta, fecha)
        elif cuenta.tipo == 'Pasivo':
            saldo_total_pasivo += obtener_saldo_cuenta(cuenta, fecha)
        elif cuenta.tipo == 'Patrimonio Neto':
            saldo_total_patrimonio += obtener_saldo_cuenta(cuenta, fecha)
    
    return {
        "Activo": saldo_total_activo,
        "Pasivo": saldo_total_pasivo,
        "Patrimonio Neto": saldo_total_patrimonio,
    }

def obtener_saldo_cuenta(cuenta, fecha):
    asientos = AsientoContable.objects.filter(cuenta=cuenta, fecha__lte=fecha)
    saldo = sum(asiento.importe for asiento in asientos)
    return saldo
