from rest_framework import  serializers

from temporary.models import  AddOrCancelRequest


""" Worked on 23.03.2021 """

class AddOrCancelRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddOrCancelRequest
        fields=('RequestId', 'RequestDate', 'SubscriptionID', 'CustomerId', 'PlanId', 'ExistingUser', 'AddReduceuser', 'AfterNoofUsers', 'InvoicegeneratedFlg', 'InvoiceNo', 'PaymentId', 'MailSentFlg', 'PaymentDoneFlg', 'ActivatedFlg', 'ActivatedDate', 'CreatedDate', 'ModifiedDate', 'CreatedBy', 'ModifiedBy')
