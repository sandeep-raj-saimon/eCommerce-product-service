from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import *

@registry.register_document
class ProductDocument(Document):
    class Index:
        name = "products"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    class Django:
        model = Product
        fields = [
            "id",
            "price",
            "quantity",
            "description"
        ]

@registry.register_document
class CategoryDocument(Document):
    class Index:
        name = "categories"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    class Django:
        model = Category
        fields = [
            "description"
        ]

@registry.register_document
class ProductCategoryDocument(Document):
    product = fields.ObjectField(properties = {
        "id": fields.IntegerField(),
        "price": fields.FloatField(),
        "quantity": fields.IntegerField(),
        "description": fields.TextField()
    })

    category = fields.ObjectField(properties = {
        "id": fields.IntegerField(),
        "description": fields.TextField()
    })

    class Index:
        name = "productcategories"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    class Django:
        model = ProductCategory
        fields = []