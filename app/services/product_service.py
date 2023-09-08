from app.models import Product

class ProductService:
    def get_all():
        list = []
        product = Product.objects.all()
# FALTA