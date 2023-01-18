from allauth.account.adapter import DefaultAccountAdapter
from django.utils.crypto import get_random_string


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        RANDOM_STRING_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.nickname = data.get('nickname')
        # user.created_at = data.get('created_at')
        # user.updated_at = data.get('updated_at')
        # user.deleted_at = data.get('updated_at')
        user.url_value=get_random_string(length=10, allowed_chars=RANDOM_STRING_CHARS)
        user.save()
        return user