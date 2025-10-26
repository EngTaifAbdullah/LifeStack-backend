from rest_framework.views import APIView
from rest_framework.response import Response

# ______________________________________________________________________________________________________________

class Home(APIView):
    
    def get(self, request):
        return Response({"message": "Welcome to LifeStack App 🍓🌺 "})


    def post(self, request):
        data = request.data
        return Response({
            "message": "You just posted to LifeStack",
            "data": data
        })
# ______________________________________________________________________________________________________________
