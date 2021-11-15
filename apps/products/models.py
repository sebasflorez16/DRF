from django.urls import reverse
from django.db import models
from django.db.models.base import Model
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords



class MeasureUnit(BaseModel):

    description = models.CharField('Descripción', max_length=50,blank = False,null = False,unique = True)
    historical = HistoricalRecords()


    #Maneja el historial de los usuarions que han hecho cambios
    @property
    def _history_user(self):  #Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value



    class Meta:
        verbose_name ='Undada de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):

        return self.description



class CategoryProduct(BaseModel):
    description = models.CharField('Descripcion',max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):  #Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value


    class Meta:
        verbose_name = 'Categoria de Producto'
    verbose_name_plural = 'Categorias de Productos'

    def __str__(self):
        return self.description



class Indicator(BaseModel):
    
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete = models.CASCADE, verbose_name='Indicador de Oferta' )
    historical = HistoricalRecords()

    @property
    def _history_user(self):  #Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = ("Inidicador de Oferta")
        verbose_name_plural = ("Inidicadores de Ofertas")

    def __str__(self):
        return f'Oferta de la categoria{self.category_product} : {self.descount_value}%'


class Product(BaseModel):
    
    name = models.CharField('Nombre del Prodcuto', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripcion del producto', blank = False, null=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete = models.CASCADE, verbose_name = 'Unidad de medida', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoria del producto',null=True)
    image = models.ImageField('Imagen del Producto', upload_to='product/', null=True)
    #quatity = models
    historical = HistoricalRecords()

    @property
    def _history_user(self):  #Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value
    

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.name

    """def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})"""
