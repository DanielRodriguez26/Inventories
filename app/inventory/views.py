from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
from .models import Inventory


#importar el archivo csv y guardarlo en la base de datos con metodo serializer

class ImportCSV(APIView):
    def post(self, request, format=None):
        file_obj = request.FILES.get('file')
        if file_obj:
            with open(file_obj.name, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    Inventory.objects.create(
                        inv_date=row['inv_date'],
                        inv_product=row['inv_product'],
                        inv_client=row['inv_client'],
                        inv_branch_office=row['inv_branch_office'],
                        inv_quantity=row['inv_quantity'],
                        inv_price=row['inv_price']
                    )
            return Response({"message": "File uploaded successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "File not found"}, status=status.HTTP_400_BAD_REQUEST)


