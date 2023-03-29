from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
from rest_framework import generics, permissions

from .models import Track
from .serializers import TrackSerializer

# Create your views here.
class GetTrackAPIView(APIView):
    def get(self, request , pk):
        try:
            states = Track.objects.filter(pk=pk)
            serializer = TrackSerializer(states, many=True)
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

class CreateTrackAPIView(APIView):
    def post(self, request):
        try:
            serializer = TrackSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'message':str(e)
            })

class DeleteTrackAPIView(APIView):
    def delete(self, request, pk):
        try:
            state = Track.objects.get(pk=pk)
            state.save()
            return Response({
                'message':'your data is deleted successfully !',
                'success': True,
                'status':status.HTTP_301_MOVED_PERMANENTLY
            })            
        except Track.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# as tutorial step , just consider on this later #
#                                                #
# #########################          ######      #

# # DJango RestFrameWork Using generic view with various pre-implemented actions such as list
# # and create.
# class TrackList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Track.objects.all()
#     serializer_class = TrackSerializer


# # DJango RestFrameWork Using generic view with various pre-implemented actions such as update
# # and get_object
# class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Track.objects.all()
#     serializer_class = TrackSerializer
