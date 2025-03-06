from decimal import Decimal

def import_total_shopping(request):
    total = Decimal('0.0')
    shopping = request.session.get('shopping', {})
    for key, value in shopping.items():
        total += Decimal(value['price'])
    return {'import_total_shopping': total}