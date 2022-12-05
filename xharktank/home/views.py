
import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render , HttpResponse
from home.models import *

# for home 
def home(request):
    return HttpResponse("You are on the home page")


# # API to post and get all the pitches
class PostPitchesAPI(APIView):
    
    def post(self, request, *args, **kwargs):

        response = {}
        try:
            keys = ["entrepreneur" , "pitchTitle" , "pitchIdea" , "askAmount" , "equity"]
            
            # if body is empty 
            if(len(request.data) == 0):
                return Response(status = status.HTTP_400_BAD_REQUEST)

            keysList = list(request.data.keys())
            
            # if some key is not there 
            for key in keys:
                if key not in keysList:
                    return Response(status = status.HTTP_400_BAD_REQUEST)
            
            # value format check 
            for key in request.data:
                if request.data.get(key) == None:
                    return Response(status = status.HTTP_400_BAD_REQUEST)
                else:
                   print(key)
                   if key == keys[4] :
                    equity = int(request.data.get(key))
                    if equity > 100:
                        return Response(status = status.HTTP_400_BAD_REQUEST)

            xharktank = pitche.objects.create(
                                        pitcherName =  request.data["entrepreneur"],
                                        pitchTitle =  request.data["pitchTitle"],
                                        pitchIdea =  request.data["pitchIdea"],
                                        askAmount =  request.data["askAmount"],
                                        equity = request.data["equity"])
            xharktank.save()
            response["id"] = str(xharktank.id)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        return Response(data = response , status = status.HTTP_201_CREATED)
    
   
    def get(self, request):
        data =  pitche.objects.all().order_by('-created')
        response = []
        try:
            for item in data:
                response.append({
                "id" : str(item.id),
                "entrepreneur" : item.pitcherName,
                "pitchTitle" : item.pitchTitle,
                "pitchIdea" : item.pitchIdea,
                "askAmount" : item.askAmount,
                "equity" : item.equity,
                "offers" : list(pitche.objects.get(pk = item.id).offers_set.all().values("id" ,"investor" , "amount" , "equity" , "comment"))
                })
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data = response , status= status.HTTP_200_OK)

PostPitches = PostPitchesAPI.as_view()

#API to get a particular pitch
class GetAPI(APIView):
    
    def get(self, request , pk):
        response = {}
        pitch = pitche.objects.filter(pk = pk)
       
        try:
            if(len(list(pitch)) == 0):
                return Response(status=status.HTTP_404_NOT_FOUND)
            if(pitch == None):
                return Response(status=status.HTTP_404_NOT_FOUND)
            for item in pitch:
                response = {
                "id" : str(item.id),
                "entrepreneur" : item.pitcherName,
                "pitchTitle" : item.pitchTitle,
                "pitchIdea" : item.pitchIdea,
                "askAmount" : item.askAmount,
                "equity" : item.equity,
                "offers" : list(pitche.objects.get(pk = item.id).offers_set.all().values("id" ,"investor" , "amount" , "equity" , "comment"))
                }
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(data = response , status= status.HTTP_200_OK)

Get = GetAPI.as_view()


#API to make offer
class MakeOfferAPI(APIView):
    
    def post(self , request , pk , *args , **kwargs):
        response = {}
        try:
            keys = ["investor" , "amount" , "equity" , "comment"] 
            obj = pitche.objects.filter(pk = pk)[0]

            # if pitch id is wrong 
            if obj == None:
                return Response(status= status.HTTP_404_NOT_FOUND)
            
            # if request body is empty 
            if (len(request.body) == 0):
                return Response(status= status.HTTP_400_BAD_REQUEST)
            
            # if keys are name uncorrectly 
            keysList = list(request.data.keys())
            
            for key in keys:
                if key not in keysList:
                    return Response(status = status.HTTP_400_BAD_REQUEST)

            # value format check 
            for key in request.data:
                if request.data.get(key) == None:
                    return Response(status = status.HTTP_400_BAD_REQUEST)
                else:
                   if key == keys[2] :
                    equity = int(request.data.get(key))
                    if equity > 100:
                        return Response(status = status.HTTP_400_BAD_REQUEST)

            offer = offers(id = None , pitche = obj , investor = request.data["investor"] , amount = request.data["amount"] , equity = request.data["equity"] , comment = request.data["comment"])
            offer.save()
            response["id"] = str(offer.id)
        except:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        return Response(data = response)

MakeOffer = MakeOfferAPI.as_view()




# import json
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from django.shortcuts import render , HttpResponse
# from home.models import *

# # API to post and get all the pitches
# class PostPitchesAPI(APIView):
    
#     def post(self, request, *args, **kwargs):

#         response = {}
#         try:
#             keys = ["entrepreneur" , "pitchTitle" , "pitchIdea" , "askAmount" , "equity"]

         
#             data = request.data["body"]
#             print(data)
#             for key in data:
#                 if data.get(key) == None:
#                     return Response(status = status.HTTP_400_BAD_REQUEST)
#                 else:
#                    print(key)
#                    if key ==  keys[4]:
#                     equity = int(data.get(key))
#                     if equity > 100:
#                         return Response(status = status.HTTP_400_BAD_REQUEST)
    
#             xharktank = pitche.objects.create(
#                                         pitcherName =  data["entrepreneur"],
#                                         pitchTitle =  data["pitchTitle"],
#                                         pitchIdea =  data["pitchIdea"],
#                                         askAmount =  data["askAmount"],
#                                         equity = data["equity"])
#             xharktank.save()
#             response["id"] = str(xharktank.id)
#         except:
#             return Response(status = status.HTTP_400_BAD_REQUEST)
#         return Response(data = response , status = status.HTTP_201_CREATED)
    
   
#     def get(self, request):
#         data =  pitche.objects.all().order_by('-created')
#         response = []
#         try:
#             for item in data:
#                 response.append({
#                 "id" : str(item.id),
#                 "entrepreneur" : item.pitcherName,
#                 "pitchTitle" : item.pitchTitle,
#                 "pitchIdea" : item.pitchIdea,
#                 "askAmount" : item.askAmount,
#                 "equity" : item.equity,
#                 "offers" : list(pitche.objects.get(pk = item.id).offers_set.all().values("id" ,"investor" , "amount" , "equity" , "comment"))
#                 })
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         return Response(data = response , status= status.HTTP_200_OK)

# PostPitches = PostPitchesAPI.as_view()
# # end


# #API to get a particular pitch
# class GetAPI(APIView):
    
#     def get(self, request , pk):
#         response = {}
#         pitch = pitche.objects.filter(pk = pk).first()
#         if(pitch == None):
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         try:
#             for item in pitch:
#                 response = {
#                 "id" : str(item.id),
#                 "entrepreneur" : item.pitcherName,
#                 "pitchTitle" : item.pitchTitle,
#                 "pitchIdea" : item.pitchIdea,
#                 "askAmount" : item.askAmount,
#                 "equity" : item.equity,
#                 "offers" : list(pitche.objects.get(pk = item.id).offers_set.all().values("id" ,"investor" , "amount" , "equity" , "comment"))
#                 }
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         return Response(data = response)

# Get = GetAPI.as_view()
# # end

# #API to make offer
# class MakeOfferAPI(APIView):
    
#     def post(self , request , pk , *args , **kwargs):
#         response = {}
#         try:
#             keys = ["investor" , "amount" , "equity" , "comment"] 
#             obj = pitche.objects.filter(pk = pk)[0]

#             # if pitch id is wrong 
#             if obj == None:
#                 return Response(status= status.HTTP_404_NOT_FOUND)
            
#             data = request.data["body"]
            
#             offer = offers(id = None , pitche = obj , investor = data["investor"] , amount = data["amount"] , equity = data["equity"] , comment = data["comment"])
#             offer.save()
#             response["id"] = str(offer.id)
#         except:
#             return Response(status= status.HTTP_400_BAD_REQUEST)
#         return Response(data = response , status=status.HTTP_201_CREATED)

# MakeOffer = MakeOfferAPI.as_view()
# # end