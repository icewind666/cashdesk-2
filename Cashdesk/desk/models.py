#coding: utf-8
import json, sys, datetime
from django.db import models


class FinancialOperation(models.Model):
    positionNumber = models.BigIntegerField()
    whoPayed = models.TextField(max_length=1000)
    fileLink = models.FileField(upload_to='documents/%Y/%m/%d', blank=True)
    datetime = models.DateTimeField(u'Дата')
    amount = models.FloatField(u'Сумма')
    alreadyPayed = models.FloatField(u'Оплачено')
    isClosed = models.BooleanField(u'Полностью оплачено')
    company = models.IntegerField(u'Компания')
    
    def __unicode__(self):
        return self.datetime.isoformat() + ' -> ' + str(self.amount)
    
    def to_json(self):
        try:
            dict_for_json = {
                "positionNumber": self.positionNumber,
                "whoPayed": self.whoPayed,
                "fileLink": self.fileLink,
                "datetime": self.datetime.isoformat(),
                "amount": self.amount,
                "alreadyPayed": self.alreadyPayed,
                "isClosed": self.isClosed,
                "company": self.company
                }
            return json.dumps(dict_for_json)
        except Exception as e:
            print(e.message)
            print(e.__doc__)
            
        return {}
    
    def to_dict(self):
        try:
            dict_for_json = {
                "positionNumber": self.positionNumber,
                "whoPayed": self.whoPayed,
                "fileLink": self.fileLink,
                "datetime": self.datetime.isoformat(),
                "amount": self.amount,
                "alreadyPayed": self.alreadyPayed,
                "isClosed": self.isClosed,
                "company": self.company
                }
            return dict_for_json
        except Exception as e:
            print(e.message)
            print(e.__doc__)
            
        return {}
