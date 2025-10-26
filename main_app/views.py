from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Certificate
from .serializers import CertificateSerializer

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


# Certificates CRUD (( Read | Create ))

class CertificatesIndex(APIView):

    def get(self, request):
        queryset = Certificate.objects.all()
        serializer = CertificateSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):
        serializer = CertificateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# ____________________________________

# Certificates CRUD (( Read | Update | Delete ))

class CertificateDetail(APIView):

    def get(self, request, cert_id):
        certificate = get_object_or_404(Certificate, id=cert_id)
        serializer = CertificateSerializer(certificate)

        return Response(serializer.data)


    def put(self, request, cert_id):
        certificate = get_object_or_404(Certificate, id=cert_id)
        serializer = CertificateSerializer(certificate, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, cert_id):
        certificate = get_object_or_404(Certificate, id=cert_id)
        certificate.delete()

        return Response({"message": f"Certificate {cert_id} deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)

# ______________________________________________________________________________________________________________









    
# ______________________________________________________________________________________________________________