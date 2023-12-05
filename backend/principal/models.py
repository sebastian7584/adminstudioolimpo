from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Country(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=128)
    id_country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class User(models.Model):
    code = models.IntegerField(unique=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth = models.DateField(null=True)
    account_bank = models.CharField(max_length=128, null=True)
    id_bank = models.ForeignKey(Bank, null=True, on_delete=models.SET_NULL)
    admin = models.BooleanField(default=False)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return f'{self.code}'

class TypePage(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    name = models.CharField(max_length=128, unique=True)
    id_type = models.ForeignKey(TypePage, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=128, unique=True)
    document = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    
class Payment(models.Model):
    name = models.CharField(max_length=128, unique=True)
    id_owner = models.ForeignKey(Owner, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Master(models.Model):
    username = models.CharField(max_length=128, unique=True)
    id_page = models.ForeignKey(Page, null=True, on_delete=models.SET_NULL)
    id_payment = models.ForeignKey(Payment, null=True, on_delete=models.SET_NULL)
    id_owner = models.ForeignKey(Owner, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id_page.name} - {self.username}'

class Account(models.Model):
    id_master = models.ForeignKey(Master, null=True, on_delete=models.SET_NULL)
    username = models.CharField(max_length=128)
    percentage_studio = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    code_studio = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='studio_accounts')
    percentage_user = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    code_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='user_accounts')
    percentage_substudio = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    code_substudio = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='substudio_accounts')
    percentage_referred = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    code_referred = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='referred_accounts')
    percentage_other = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    code_other = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='other_accounts')

    def __str__(self):
        return f'{self.id_master}-{self.username}'

class Period(models.Model):
    trm = models.DecimalField(max_digits=8, decimal_places=2)
    year = models.IntegerField()
    mount = models.IntegerField()
    period = models.IntegerField()

    def __str__(self):
        return f'{self.year}-{self.mount}-{self.period}'

class Earning(models.Model):
    date = models.IntegerField()
    id_account = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    id_period = models.ForeignKey(Period, null=True, on_delete=models.SET_NULL)
    percentage_studio = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    code_studio = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='studio_earning')
    percentage_user = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    code_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='user_earning')
    percentage_substudio = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    code_substudio = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='substudio_earning')
    percentage_referred = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    code_referred = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='referred_earning')
    percentage_other = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    code_other = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='other_earning')

class Document(models.Model):
    id_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    link = models.URLField()
    type = models.CharField(max_length=128)
    number = models.CharField(max_length=128)
    expiration = models.DateField()

class Advance(models.Model):
    id_period = models.ForeignKey(Period, null=True, on_delete=models.SET_NULL)
    day = models.IntegerField()
    value = models.IntegerField()
    id_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    state = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    id_bank = models.ForeignKey(Bank, null=True, on_delete=models.SET_NULL)