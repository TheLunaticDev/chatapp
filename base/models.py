from django.db import models


class BTCPayClientModel(models.Model):
    client_data = models.BinaryField()
