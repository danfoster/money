from money.models import Account
from rest_framework import serializers

class AccountSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Account
    fields = ('id', 'account', 'sortcode', 'name', 'accounttype', 'currency')

