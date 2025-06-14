from rest_framework import serializers

from apps.user.models import GDUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GDUser
        fields = (
            "first_name",
            "email",
            "allow_sms_notifications",
            "allow_email_notifications",
            "subscribe_to_newsletter",
            "phone_number",
            "account_type",
            "profile_photo",
        )
