from .serializers import AccountSerializer
from rest_framework import viewsets
from money.models import Account

class AccountViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = Account.objects.all()
  serializer_class = AccountSerializer
