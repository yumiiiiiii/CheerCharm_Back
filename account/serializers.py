from rest_framework import serializers
from account.models import User

from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password','nickname','create_time','delete_time']

    def create(slef, validate_data):
        user=User.objects.create(
            nickname=validate_data['nickname'],
            username=validate_data['username'],
        )
        user.set_password(validate_data['password'])
        token = RefreshToken.for_user(user)
        user.refreshtoken = token
        user.save()

        return user

class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=64)
    password=serializers.CharField(max_length=64, write_only=True)

    def validate(self, data):
        username=data.get("username", None)
        password=data.get("password", None)


        if User.objects.filter(username=username).exists():
            user=User.objects.get(username=username)

            if not user.check_password(password):
                raise serializers.ValidationError()
        else:
            raise serializers.ValidationError("User does not exist")
        token = RefreshToken.for_user(user=user)
        data = {
            'id': user.id,
            'nickname' : user.nickname,
            'refresh_token' : str(token),
            'access_token' : str(token.access_token)
        }
        return data