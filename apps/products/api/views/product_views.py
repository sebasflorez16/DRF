
from rest_framework import generics
from rest_framework import status  #codigos de estado para enviar luego del response
from rest_framework.response import Response

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializer import ProductSerializer

#List
class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer

#Create
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Producto creado correctamente'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST)

#Detail
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)


#Delete 
class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

#Eliminacion directa
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

#Eliminacion logica
    def delete(self, request, pk = None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'message':'El producto no fue encontrado'}, status = status.HTTP_400_BAD_REQUEST)


#Update
class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    """def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)


    def patch(self, request, pk = None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product_serializer = self.serializer_class(product) #No se pasa el modelo o la instancia. Se pasa es el serializador para ver la instancia
            return Response(product_serializer.data, status = status.HTTP_200_OK) # Esto devuelve la data de la instancia a la interfaz


        return Response({'message':'El producto no fue encontrado'}, status = status.HTTP_400_BAD_REQUEST)"""


#Version refactorizada del codigoanterior y y redefiniendo el metodo put
    
    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()

    #El PATCH obtiene la instancia
    def patch(self, request, pk = None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status = status.HTTP_200_OK)
        
        return Response({'error':'El producto no fue encontrado'}, status = status.HTTP_400_BAD_REQUEST)

    #El PUT actualiza la instancia
    def put(self, request, pk = None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response (product_serializer.data, status = status.HTTP_200_OK)

            return Response({'message':'El producto no fue encontrado'}, status = status.HTTP_400_BAD_REQUEST)

        

