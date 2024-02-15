from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Pricing
from .serializers import DeliveryRequestSerializer
from .services import PriceCalculator

@api_view(['POST'])
def calculate_delivery_price(request):
    serializer = DeliveryRequestSerializer(data=request.data)
    
    if serializer.is_valid():
        organization_id = serializer.validated_data['organization_id']
        zone = serializer.validated_data['zone']
        total_distance = serializer.validated_data['total_distance']
        item_type = serializer.validated_data['item_type']

        try:
            pricing = Pricing.objects.get(organization_id=organization_id, zone=zone, item__type=item_type)
        except Pricing.DoesNotExist:
            return Response({'error': 'Pricing not found'}, status=status.HTTP_404_NOT_FOUND)

        price_calculator = PriceCalculator()

        try:
            price = price_calculator.calculate_price(pricing.base_distance_in_km, pricing.km_price, pricing.fix_price, total_distance)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        response_data = {'total_price': price / 100}  # Convert back to euros
        return Response(response_data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
