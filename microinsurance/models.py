from django.db import models
from django.core.validators import RegexValidator
from django.db.models.functions import Concat 
from django.contrib.auth.models import Group, User
import datetime


class Validators(models.Model):
	name_validator = RegexValidator(regex=r'^\S+[a-zA-Z0-9\s]+[^~\`\!\#\$\%\^\&\*\(\)\+\=\{\}\?\/\>\;\:\<\,\[\]\|\\]*$')
	email_validator = RegexValidator(regex=r'^[a-zA-Z0-9@_\-.][^~\`\!\#\$\%\^\&\*\(\)\+\=\{\}\?\/\>\;\:\<\,\[\]\|\\\s]*$')
	#add contact_number_validator = 

class Underwriter(models.Model):
	
	underwriter_name = models.CharField(validators=[Validators.name_validator], max_length=500,  unique=True)
	underwriter_email = models.CharField(validators=[Validators.email_validator], max_length=200, unique=True)
	head_office_address = models.TextField(max_length=500, blank=False)
	underwriter_contact_number = models.CharField(max_length=200)
	contact_person = models.CharField(max_length=200, blank=False)
	username = models.CharField(max_length=200, unique=True)
	password = models.CharField(max_length=200, unique=True)
	created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
	underwriter_status_active =  models.BooleanField(default=True)


	REQUIRED_FIELDS = [
		'underwriter_name', 'underwriter_email', 
	 	'underwriter_contact_number', 'contact_person',
		'username', 'password'
	]

	def __str__(self):
		return self.underwriter_name


class Branch(models.Model):
	branch_name = models.CharField(validators=[Validators.name_validator], max_length=200, blank=False, unique=True)
	branch_manager = models.OneToOneField(User, primary_key=True)
	branch_contact_number = models.CharField(max_length=200, blank=False)
	branch_created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
	branch_status_active =  models.BooleanField(default=True)

	class Meta:
		verbose_name = 'Branch'
		verbose_name_plural = 'Branches'

	def __str__(self):
		return self.branch_name


class Product(models.Model):
	product_name = models.CharField(validators=[Validators.name_validator], max_length=200, blank=False, unique=True)
	base_price = models.DecimalField(max_digits=9, decimal_places=2)
	selling_price = models.DecimalField(max_digits=9, decimal_places=2)
	limit_per_head = models.IntegerField(max_length=None, blank=False)
	insurance_provider_name = models.ForeignKey(Underwriter)
	date_created = models.DateTimeField(default=datetime.datetime.now, editable=False)
	effectivity_date = models.DateTimeField(default=datetime.datetime.now, editable=True)
	validity_period_in_days = models.IntegerField(max_length=None, blank=False)
	age_limit_from = models.IntegerField(max_length=None, blank=False)
	age_limit_to = models.IntegerField(max_length=None, blank=False)
	product_status_active = models.BooleanField(default=True)



	def __str__ (self):
		return self.product_name


class Applicant(models.Model):
	first_name = models.CharField(max_length=200, blank=False)
	middle_name = models.CharField(max_length=200, blank=True)
	last_name = models.CharField(max_length=200, blank=False)
	contact_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
	contact_number = models.CharField(validators=[contact_regex], max_length=15)
	created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
	applicant_status_active =  models.BooleanField(default=True)
	product_name = models.ForeignKey(Product, null=True)
	number_of_pieces = models.IntegerField(max_length=None, blank=False)


	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)

