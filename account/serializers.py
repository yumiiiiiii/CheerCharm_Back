from rest_framework import serializers
from account.models import User

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password','nickname','create_time','delete_time']

    def create(slef, validate_data):
        user=User.objects.create(
            nickname=validate_data['nickname'],
            username=validate_data['username'],
        )
        user.set_password(validate_data['password'])
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
                return user