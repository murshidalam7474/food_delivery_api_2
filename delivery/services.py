# delivery/services.py
from decimal import Decimal
class PriceCalculator:
    @staticmethod
    def calculate_price(base_distance, km_price, fix_price, total_distance):
        base_distance = Decimal(base_distance)
        km_price = Decimal(km_price)
        fix_price = Decimal(fix_price)
        total_distance = Decimal(total_distance)

        # Perform the calculation with Decimal values
        total_price = fix_price + (total_distance - base_distance) * km_price

        return total_price
