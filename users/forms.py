from django.contrib.auth.forms import UserCreationForm

"""
1.Extends #extends UserCreationForm
2.Meta keeps additional information about the form
3.Also extends UserCreationForm.Meta, so almost everything from django form is reused.
4.fields - determines the field to be included in the form.
5.this custom form will use all fields from UserCreationForm add will
    add the email field.
"""
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
