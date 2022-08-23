from rest_framework import serializers
from timetable.models import Ferry, Port

class FerrySerializer(serializers.ModelSerializer):
    """
    Преобразуем данные в Json формат и обратно
    """
    class Meta:
        model = Ferry
        fields = ('__all__')


class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ('name', 'country')

# class PortSerializer(serializers.Serializer):
#     """
#     Преобразуем данные в Json формат и обратно
#     """
#     name = serializers.CharField(max_length=50)
#     country = serializers.CharField(max_length=50)
#     boat = serializers.CharField(read_only=True)  # read_only для того чтобы при Пост запросе не требовало заполнения
#
#     def create(self, validated_data):
#         return Port.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.country = validated_data.get('country', instance.country)
#         instance.save()
#         return instance
