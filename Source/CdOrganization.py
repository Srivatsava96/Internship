# -----------------------------------------------------------------------------
# Description: Data model for Organisation
# Author: Srivatsava
# Date: 22-05-2017
#------------------------------------------------------------------------------

from mongoengine import *

class Contact(EmbeddedDocument):
	title = StringField(db_field='title', max_length=15, verbose_name='title')
	first_name = StringField(db_field = 'fname', max_length=100, required = True, verbose_name = 'first name')
	last_name = StringField(db_field='lname', required=True, verbose_name='last name')
	phone = StringField(db_field='phone', required = True, verbose_name='contact telephone number')
	email = StringField(db_field='email', verbose_name='email address')
	
class Physician(EmbeddedDocument):
	title = StringField(db_field='title', max_length=15, verbose_name='title')
	first_name = StringField(db_field = 'fname', max_length=100, required = True, verbose_name = 'first name')
	last_name = StringField(db_field='lname', required=True, verbose_name='last name')
	middle_initial = StringField(db_field='mi', max_length=10, verbose_name='middle name')
	suffix = StringField(db_field='suffix', verbose_name='suffix')
	type = StringField(db_field='type', required=True, verbose_name='Type of medical practitioner')
	is_admin = BooleanField(db_field='isadmin', required=True, verbose_name='Is the personal an administrator')
	phone = StringField(db_field='phone', required = True, verbose_name='contact telephone number')
	ext = StringField(db_field='ext', required = True, verbose_name='phone extension')
	pager = StringField(db_field='pager', verbose_name='contact pager number')
	pager_id = StringField(db_field='pager_id', verbose_name='pager id number')
	mobile = StringField(db_field='mobile', verbose_name='contact personal number'
	email = StringField(db_field='email', verbose_name='email address')
	npi = StringField(db_field='npi', max_length=10,required = True, verbose_name='national identifier')
	#username = 
	taxonomy = ListField(StringField(max_length=10))

class Organisation(Document):
	name = StringField(db_field='name', max_length=100, required=True, verbose_name='organisation name')
	npi = StringField(db_field='npi', max_length=10,required = True, verbose_name='national identifier')
	address_line1 = StringField(db_field='add', verbose_name='address')
	city = StringField(db_field='city', verbose_name='city')
	state = StringField(db_field='state', max_length=2, verbose_name='state')
	zipCode = StringField(db_field='zip', max_length=10, verbose_name='zipCode')
	telephoneNumber = StringField(db_field='tel', verbose_name='contact telphone number')
	fax = StringField(db_field='fax', verbose_name='contact fax number')
	contact = EmbeddedDocumentField(Contact)
	physicians = ListField(EmbeddedDocumentField(Physician))