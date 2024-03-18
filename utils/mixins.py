from django.shortcuts import get_object_or_404
from rest_framework.views import Response, Request, status
class CreateModelMixin:
    queryset = None
    serializer_class = None
    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exceptions=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class RetriveModelMixin:
    queryset = None
    serializer_class = None

    def retrieve(self, request: Request, pk : int) -> Response:
        instance = get_object_or_404(self.queryset.all(), pk=pk)
        return Response(self.serializer_class(instance).data)

class DestroyModelMixin:
    queryset = None
    serializer_class = None

    def destroy(self, request, pk:int) -> Response:
        instance = get_object_or_404(self.queryset.all(), pk=pk)
        #self.check_object_permissions(request, instance)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UpdateModelMixin:
    queryset = None
    serializer_class = None
    def update(self, request, pk:int):
        instance = get_object_or_404(self.queryset.all(), pk=pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)