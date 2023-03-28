from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import State, City, Area
from .serializers import AreaSerializer, CitySerializer, StateSerializer


# Create your views here.
class GetStateAPIView(APIView):
    def get(self, request):
        try:
            states = State.objects.filter(is_del=False)
            serializer = StateSerializer(states, many=True)
            return Response({
            'status':status.HTTP_302_FOUND,
            'success':True,
            'responce':serializer.data
            })
        except Exception as e:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'message':str(e)
            })

class CreateStateAPIView(APIView):
    def post(self, request):
        try:
            serializer = StateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'message':str(e)
            })

class DeleteStateAPIView(APIView):
    def delete(self, request, pk):
        try:
            state = State.objects.get(pk=pk)
            if state.is_del == False:
                state.is_del = True
                state.save()
                return Response({
                    'message':'your data is deleted successfully !',
                    'success': True,
                    'status':status.HTTP_301_MOVED_PERMANENTLY
                })
            else:
                return Response({
                    'message':'Already deleted !',
                    'success': False,
                    'status':status.HTTP_404_NOT_FOUND
                })            
        except State.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class GetCityAPIView(APIView):
    def get(request,*args,**kwargs):
        try:
            city = City.objects.filter(is_del = False)
            serializer = CitySerializer(city ,many =True)
            return Response({
                'message':'Data found!',
                'status':status.HTTP_302_FOUND,
                'responce':serializer.data
            })
        except Exception as e:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'message':str(e)
            })


class CreateCityAPIView(APIView):
    def post(self, request):
        try:
            serializer = CitySerializer(data=request.data)
            state = State.objects.get(pk=request.data['state'])
            isdel = state.is_del == False
            print(isdel)
            if serializer.is_valid() and isdel:
                serializer.save()
                return Response({
                    'message':'your data is created successfully !',
                    'success': True,
                    'status':status.HTTP_201_CREATED,
                    'responce':serializer.data
                })
            elif isdel == False:
                return Response({  
                    'message':'State is deleted!',
                    'status':status.HTTP_404_NOT_FOUND,
                    'success':False
                })
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
        except Exception as e:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'message':str(e)
            })

class DeleteCityAPIView(APIView):
    def delete(self, request, pk):
        try:
            city = City.objects.get(pk=pk)
            if city.is_del == False:
                city.is_del = True
                city.save()
                return Response({
                    'message':'your data is deleted successfully !',
                    'success': True,
                    'status':status.HTTP_301_MOVED_PERMANENTLY
                })
            else:
                return Response({
                    'message':'Already deleted !',
                    'success': False,
                    'status':status.HTTP_404_NOT_FOUND
                })            
        except City.DoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'City not found!',
                'success':False
            })



class GetAreaAPIView(APIView):
    def get(self, request):
        try:
            area = Area.objects.filter(is_del=False)
            serializer = AreaSerializer(area, many=True)
            return Response({
                'message':'Data found!',
                'status':status.HTTP_302_FOUND,
                'responce':serializer.data
            })
        except Exception as e:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'message':str(e)
            })


class CreateAreaAPIView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            serializer = AreaSerializer(data=request.data)
            city = City.objects.get(pk=request.data['city'])
            isdel = city.is_del == False
            if serializer.is_valid() and isdel:
                serializer.save()
                return Response({
                    'message':'your data is created successfully !',
                    'success': True,
                    'status':status.HTTP_201_CREATED,
                    'responce':serializer.data
                })
            elif isdel == False:
                return Response({  
                    'message':'City is deleted!',
                    'status':status.HTTP_404_NOT_FOUND,
                    'success':False
                })
            else:
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'message':'City not found!',
                    'success':False
                })
        except Exception as e:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'success':False,
                'message':str(e)
            })

class DeleteAreaAPIView(APIView):
    def delete(self, request, pk):
        try:
            area = Area.objects.get(pk=pk)
            if area.is_del == False:
                area.is_del = True
                area.save()
                return Response({
                    'message':'your data is deleted successfully !',
                    'success': True,
                    'status':status.HTTP_301_MOVED_PERMANENTLY
                })
            else:
                return Response({
                    'message':'Already deleted !',
                    'success': False,
                    'status':status.HTTP_404_NOT_FOUND
                })            
        except Area.DoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'Area not found!',
                'success':False})