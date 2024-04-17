from django.db import models

class HorasExtras(models.Model):
    year = models.IntegerField()
    mes = models.IntegerField()
    id_sonda_plus = models.IntegerField()
    numero_documento = models.CharField(max_length=30)
    nombre_colaborador = models.CharField(max_length=70)
    monto = models.IntegerField()
    cantidad_horas = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    moneda = models.CharField(max_length=3, null=True, blank=True)
    centro_costos = models.CharField(max_length=20, null=True, blank=True)
    pais = models.CharField(max_length=15)
    empresa = models.CharField(max_length=20,null=True, blank=True)
    concepto = models.CharField(max_length=50,null=True, blank=True)



class Disponibilidad(models.Model):

    year = models.IntegerField()
    mes = models.IntegerField()
    id_sonda_plus = models.IntegerField()
    numero_documento = models.CharField(max_length=25)
    nombre_colaborador = models.CharField(max_length=70)
    monto = models.IntegerField()
    cantidad_horas = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    moneda = models.CharField(max_length=3, null=True, blank=True)
    centro_costos = models.CharField(max_length=20, null=True, blank=True)
    pais = models.CharField(max_length=15)
    empresa = models.CharField(max_length=20,null=True, blank=True)
    concepto = models.CharField(max_length=50,null=True, blank=True)

class HorasCompensadas(models.Model):

    year = models.IntegerField()
    mes = models.IntegerField()
    id_sonda_plus = models.IntegerField()
    numero_documento = models.CharField(max_length=25)
    nombre_colaborador = models.CharField(max_length=70)
    monto = models.IntegerField()
    cantidad_horas = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    moneda = models.CharField(max_length=3, null=True, blank=True)
    centro_costos = models.CharField(max_length=20, null=True, blank=True)
    pais = models.CharField(max_length=15)
    empresa = models.CharField(max_length=20,null=True, blank=True)
    concepto = models.CharField(max_length=50,null=True, blank=True)


class Provision(models.Model):
    pais = models.CharField(max_length=15)
    year = models.IntegerField()
    mes = models.IntegerField()
    empresa = models.CharField(max_length=20)
    id_sonda_plus = models.IntegerField()
    numero_documento = models.CharField(max_length=25)
    nombre  = models.CharField(max_length=25)
    primer_apellido = models.CharField(max_length=25)
    segundo_apellido = models.CharField(max_length=25)
    centro_costos = models.CharField(max_length=25)
    cantidad_dias = models.IntegerField()
    saldo_monto = models.IntegerField()
    moneda = models.CharField(max_length=3)

class Pais(models.Model):
    nombre_pais = models.CharField(max_length=15)
    def __str__(self):
        return self.nombre_pais