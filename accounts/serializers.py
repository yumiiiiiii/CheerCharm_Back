from rest_framework import serializers

from accounts.models import User

from rest_auth.registration.serializers import RegisterSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'nickname','create_at','delete_at', 'updated_at']

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(
        required=True,
        max_length=8,
    )
    # created_at=serializers.DateTimeField()
    # updated_at=serializers.DateTimeField()
    # deleted_at=serializers.DateTimeField(required=False)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        # data_dict['created_at'] = self.validated_data.get('created_at', '')
        # data_dict['updated_at'] = self.validated_data.get('created_at', '')
        # data_dict['deleted_at'] = self.validated_data.get('deleted_at', '')
        return data_dict