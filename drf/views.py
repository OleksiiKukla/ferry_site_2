from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from timetable.models import Ferry, Port
from .seryalizers import FerrySerializer, PortSerializer
from datetime import datetime
# Create your views here.

class FerryViewSet(viewsets.ModelViewSet):
    queryset = Ferry.objects.all()
    serializer_class = FerrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



# class FerryApiView(APIView):
#
#     def get(self, request):
#         all_ferry = Ferry.objects.all().values()
#        return Response({'ferries': list(all_ferry)})




class PortViewsSet(viewsets.ModelViewSet):
    #queryset = Port.objects.all()  # если не определен меод get_queryset и обязательно при регистрации в urls определить basename
    serializer_class = PortSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        '''
        для более сложного поведения  отдачи Кверисет
        '''
        pk = self.kwargs.get('pk')

        if not pk:
            return Port.objects.all()[:3]

        return Port.objects.filter(pk=pk)


# class PortApiView(generics.ListCreateAPIView):  # заменяется ModelViwesSet
#     queryset = Port.objects.all()
#     serializer_class = PortSerializer

# class PortUpdateDeleteRetrieve(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Port.objects.all()
#     serializer_class = PortSerializer




# class PortApiView(APIView):  # если нужно определить в ручную
#
#     def get(self, request):
#         ports_all = Port.objects.all()
#         return Response({'ports': PortSerializer(ports_all, many=True).data})
#
#     def post(self,request):
#         serializer = PortSerializer(data=request.data) #проверка валидности данных согласно сериализатору
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # port_new = Port.objects.create(
#         #     name=request.data['name'],
#         #     country=request.data['country']
#         # )
#         return Response({'ports': serializer.data})
#
#     def put(self,request,*args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'pk':'pk not found'})
#         try:
#             instance = Port.objects.get(pk=pk)
#         except:
#             return Response({'pk':'Objects does not exist'})
#
#         serializer = PortSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'ports': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'pk':'pk not found'})
#         try:
#             port_delete = Port.objects.get(pk=pk)
#             port_delete.delete()
#
#         except:
#             return Response({'pk':'Method Put not alowed'})
#
#         return Response({'ports': 'deleted'+str(pk)})
#
# class TimetableApiView(generics.ListAPIView):
#     queryset = Ferry.objects.all()
#     serializer_class = FerrySeryalizer
