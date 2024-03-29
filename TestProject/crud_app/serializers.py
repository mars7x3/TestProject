from rest_framework import serializers

from crud_app.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category, context=self.context).data
        rep['colors'] = ColorSerializer(instance.colors.all(), many=True, context=self.context).data
        rep['data'] = ProductDataSerializer(instance.data, context=self.context).data
        rep['image'] = ProductImageSerializer(instance.images.first(), context=self.context).data
        return rep


class ProductDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductData
        exclude = ('product', 'id')


class ProductDetailSerializer(serializers.ModelSerializer):
    data = ProductDataSerializer(required=True)

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category_title'] = instance.category.title
        rep['colors'] = ColorSerializer(instance.colors.all(), many=True, context=self.context).data
        rep['images'] = ProductImageSerializer(instance.images.all(), many=True, context=self.context).data
        return rep

    def create(self, validated_data):
        data = validated_data.pop('data')
        colors = validated_data.pop('colors')
        product = Product.objects.create(**validated_data)
        product.colors.set(colors)
        data['product'] = product
        ProductData.objects.create(**data)
        return product

    def update(self, instance, validated_data):
        data = validated_data.pop('data')
        colors = validated_data.pop('colors')
        data['product'] = instance

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        instance.colors.set(colors)

        for key, value in data.items():
            setattr(instance.data, key, value)
        instance.data.save()
        return instance


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ('product',)

