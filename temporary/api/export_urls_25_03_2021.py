#ENDPOINTS and payloads for invoice
# https://homeurl/api/invoice/
# https://homeurl/api/detailed/invoice/(key for process(InvoiceId))
# https://homeurl/api/create/invoice/
# https://homeurl/api/update/invoice/(key for process(InvoiceId))
# https://homeurl/api/delete/invoice/(key for process(InvoiceId))

"""
{
    "InvoiceId": 37483,
    "InvoiceDate": "2021-03-20",
    "SubscriptionId": 374834,
    "CustomerId": 3874,
    "PlanId": 3847,
    "InvoiceType": "`kfdjfk",
    "AdditionalUsers": "dfidfj",
    "UpgradePlanId": 38473,
    "CreatedDate": "2021-03-25",
    "ModifiedDate": "2021-03-25",
    "CreatedBy": "kumar",
    "ModifiedBy": "isravel"
}
"""

#ENDPOINTS and payloads for payment
# https://homeurl/api/payment/
# https://homeurl/api/detailed/payment/(key for process(PaymentId))
# https://homeurl/api/create/payment/
# https://homeurl/api/update/payment/(key for process(PaymentId))
# https://homeurl/api/delete/payment/(key for process(PaymentId))
"""
{
    "PaymentId": 2398743,
    "PaymentDate": "2021-03-25",
    "SubscriptionCode": 3874,
    "InvoiceNo": 374,
    "InvoiceType": "dkfj",
    "CustomerId": 3874,
    "SalesOrderId": 3874,
    "PaymentMode": "23874",
    "PayemntAmt": "3874.00",
    "CreatedDate": "2021-03-27",
    "ModifiedDate": "2021-03-27",
    "CreatedBy": "kumar",
    "ModifiedBy": "ISRAVEL"
}
"""

#ENDPOINTS and payloads for plan

# https://homeurl/api/plan/
# https://homeurl/api/detailed/plan/(key for process(PlanId))
# https://homeurl/api/create/plan/
# https://homeurl/api/update/plan/(key for process(PlanId))
# https://homeurl/api/delete/plan/(key for process(PlanId))
"""
{
    "PlanId": 832743,
    "PlanType": "fkjdf",
    "PlanName": "dkfj",
    "PlanEffectiveDate": "2021-03-27",
    "NoOfDays": 34,
    "CreatedBy": "kumar",
    "CreatedDate": "2021-03-27",
    "ModifiedBy": "kumar",
    "ModifiedDate": "2021-03-25",
    "ActiveFlag": true
}
"""