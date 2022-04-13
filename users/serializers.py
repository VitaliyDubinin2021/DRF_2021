from rest_framework.serializers import HyperlinkedModelSerializer
from users.models import User


class UserModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'user_name', 'first_name', 'last_name', 'email']

class UserModelSerializerExtended(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff']