from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from roulette.roulette_select import Roulette


characters = [{'name' : "viper"}, {'name' : "breach"}, {'name' : "jett"}]
# Create your views here.
class RouletteGetView(APIView):
    def get(self, request):
        # Your logic for the "roulette get" endpoint goes here
        # For example, you can retrieve data from the database or perform some calculations
        game_name = request.GET.get('game_name') or 'valorant'
        allowed_roles = request.GET.get('allowed_roles') or None
        num_characters = request.GET.get('num_characters') or 1
        
        
        characters = Roulette(game_name, roles=allowed_roles, num_characters=num_characters)
        
        # Assuming you have some data to return as a response
        data = {
            'message': "Characters generated successfully!",
            'data': 
                [character["name"] for character in characters]
            ,
            "response": "200 OK"
        }
        
        return JsonResponse(data, safe=False, status=200)