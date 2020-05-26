from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    """
    """

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'
