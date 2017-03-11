#coding: utf-8
import json, sys, datetime
from django.db import models

class FinancialOperation(models.Model):
    positionNumber = models.BigIntegerField()
    whoPayed = models.TextField(max_length=1000)
    fileLink = models.FileField(upload_to='documents/%Y/%m/%d')
    datetime = models.DateTimeField(u'Дата')
    amount = models.FloatField(u'Сумма')
    alreadyPayed = models.FloatField(u'Оплачено')
    isClosed = models.BooleanField(u'Полностью оплачено')
    
    def __unicode__(self):
        return self.datetime.isoformat() + ' -> ' + str(self.amount) + '. ' + self.comment
    
    def toJSON(self):
        try:
            dictForJson = {
                "positionNumber":self.positionNumber,
                "whoPayed":self.whoPayed,
                "fileLink": self.fileLink,
                "datetime":self.datetime.isoformat(), 
                "amount":self.amount, 
                "alreadyPayed":self.alreadyPayed,
                "isClosed":self.isClosed
                }
        except Exception as e:
            print(e.message)
            print(e.__doc__)
            
        return json.dumps(dictForJson)
    
    def toDict(self):
        try:
            dictForJson = {
                "positionNumber":self.positionNumber,
                "whoPayed":self.whoPayed,
                "fileLink": self.fileLink,
                "datetime":self.datetime.isoformat(), 
                "amount":self.amount, 
                "alreadyPayed":self.alreadyPayed,
                "isClosed":self.isClosed
                }
        except Exception as e:
            print(e.message)
            print(e.__doc__)
            
        return dictForJson
        
        