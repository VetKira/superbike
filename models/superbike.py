from mongoengine import *

class Bike(Document):
    bikename= StringField()
    hangxe = StringField()
    image = StringField()
    dongco = StringField()
    maluc = StringField()
    congsuat = StringField()
    hopso = StringField()
    chieucaoyenxe = StringField()
    dacdiemkhac = StringField()
    giaxe = StringField()
