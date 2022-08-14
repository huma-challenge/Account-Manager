from django.db import models

# Using for saving logouted tokens and etc ...
class BlackListToken(models.Model):
    token = models.CharField(204, unique=True, blank=False, null=False)
