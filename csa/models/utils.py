from functools import partial
from django.db import models


# wrap CharField to our own class that defaults to max_length 512
# for ease of use and consistency
CSACharField = partial(models.CharField, max_length=512)
