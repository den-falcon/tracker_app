from django.core.validators import MinLengthValidator

from django.utils.deconstruct import deconstructible


@deconstructible
class MinLengthValidator(MinLengthValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)
