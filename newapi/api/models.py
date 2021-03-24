# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.mail import send_mail


class Athletes(models.Model):
    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(unique=True, max_length=100)
    distance = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    bonus_beds = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)

    class Meta:
        db_table = 'athletes'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def send_mail(self, link):
        send_mail(
            'Балкан Ултра Регистрация',
            f"""Благодарим Ви за регистрацията. Вашите детайли са:

            Две имена: {self.__str__()}
            Дистанция: {self.distance}
            Линкове(само за 78км): {link}.
            
            В срок от 2-3 дни вашата регистрация ще бъде прегледана и одобрена, ако отговаряте на посочените изисквания.

            За 78км:
            В случай че не сте изпратили линкове към резултати, моля изпратете ни такива на balkanultra@abv.bg""",
            'balkanultra.noreply@gmail.com',
            [self.email, 'ivan.gotchev94@gmail.com'],
            fail_silently=False,
        )


class Racelinks(models.Model):
    athlete = models.ForeignKey(Athletes, on_delete=models.SET_NULL, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    athlete_name = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'racelinks'

    def __str__(self):
        return str(self.athlete_name)