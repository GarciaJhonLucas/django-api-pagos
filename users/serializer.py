from .models import Users


def validate(self, attrs):
    email_exists = Users.object.filter(email=attrs['email']).exists()
    if email_exists:
        raise ValidationError('The mail already exists')
    return super().validate(attrs)


def create(self, validated_data):
    password = validated_data.pop('password')
    user = super().create(validated_data)
    user.set_password(password)
    user.save()
    Token.objects().create(user=user)