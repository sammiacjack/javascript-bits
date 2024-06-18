# Generated by Django 5.0.6 on 2024-06-16 18:40

import common.utils.helpers
import crm.utils.ticketproc
import datetime
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('alternative_names', models.CharField(blank=True, default='', help_text='Separate them with commas.', max_length=100, verbose_name='Alternative names')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('alternative_names', models.CharField(blank=True, default='', help_text='Separate them with commas.', max_length=100, verbose_name='Alternative names')),
                ('url_name', models.SlugField()),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Alphabetic Code for the Representation of Currencies.', max_length=3)),
                ('rate_to_state_currency', models.DecimalField(decimal_places=8, default=1, help_text='Exchange rate against the state currency.', max_digits=13, verbose_name='Rate to state currency')),
                ('rate_to_marketing_currency', models.DecimalField(decimal_places=8, default=1, help_text='Exchange rate against the state currency.', max_digits=13, verbose_name='Rate to marketing currency')),
                ('is_state_currency', models.BooleanField(default=False, verbose_name='Is it the state currency?')),
                ('is_marketing_currency', models.BooleanField(default=False, verbose_name='Is it the marketing currency?')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Update date')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('name', models.CharField(help_text='Deal name', max_length=250, verbose_name='Name')),
                ('next_step', models.CharField(help_text='Describe briefly what needs to be done in the next step.', max_length=250, verbose_name='Next step')),
                ('next_step_date', models.DateField(help_text='Date to which the next step should be taken.', verbose_name='Step date')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('workflow', models.TextField(blank=True, default='', verbose_name='Workflow')),
                ('stages_dates', models.TextField(blank=True, default='', help_text='Dates of passing the stages', verbose_name='Dates of the stages')),
                ('closing_date', models.DateField(blank=True, null=True, verbose_name='Date of deal closing')),
                ('win_closing_date', models.DateTimeField(blank=True, null=True, verbose_name='Date of won deal closing')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Total deal amount without VAT', max_digits=10, null=True, verbose_name='Amount')),
                ('probability', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Probability (%)')),
                ('ticket', models.CharField(default='', max_length=16, unique=True)),
                ('relevant', models.BooleanField(default=True, verbose_name='Relevant')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('important', models.BooleanField(default=False, verbose_name='Important')),
                ('is_new', models.BooleanField(default=True)),
                ('remind_me', models.BooleanField(default=False, verbose_name='Remind me.')),
            ],
            options={
                'verbose_name': 'Deal',
                'verbose_name_plural': 'Deals',
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name': 'Industry of Clients',
                'verbose_name_plural': 'Industries of Clients',
            },
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('first_name', models.CharField(help_text='The name of the contact person (one word).', max_length=100, verbose_name='First name')),
                ('middle_name', models.CharField(blank=True, default='', help_text='The middle name of the contact person.', max_length=100, verbose_name='Middle name')),
                ('last_name', models.CharField(blank=True, default='', help_text='The last name of the contact person (one word).', max_length=100, verbose_name='Last name')),
                ('title', models.CharField(blank=True, help_text='The title (position) of the contact person.', max_length=100, null=True, verbose_name='Title / Position')),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1, null=True, verbose_name='Sex')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('was_in_touch', models.DateField(blank=True, null=True, verbose_name='Last contact date')),
                ('email', models.CharField(help_text='Use comma to separate Emails.', max_length=200, verbose_name='Email')),
                ('secondary_email', models.EmailField(blank=True, default='', max_length=254, verbose_name='Secondary email')),
                ('phone', models.CharField(blank=True, default='', max_length=100, verbose_name='Phone')),
                ('other_phone', models.CharField(blank=True, default='', max_length=100)),
                ('mobile', models.CharField(blank=True, default='', max_length=100, verbose_name='Mobile phone')),
                ('skype', models.CharField(blank=True, default='', max_length=50)),
                ('city_name', models.CharField(blank=True, default='', max_length=50, verbose_name='City')),
                ('disqualified', models.BooleanField(default=False, verbose_name='Disqualified')),
                ('address', models.TextField(blank=True, default='', verbose_name='Address')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('company_name', models.CharField(blank=True, default='', max_length=200, verbose_name='Company name')),
                ('website', models.URLField(blank=True, default='')),
                ('company_phone', models.CharField(blank=True, default='', max_length=20, verbose_name='Company phone')),
                ('company_address', models.TextField(blank=True, default='', verbose_name='Company address')),
                ('company_email', models.EmailField(blank=True, default='', max_length=254, verbose_name='Company email')),
                ('token', models.CharField(default=common.utils.helpers.token_default, max_length=11, unique=True)),
            ],
            options={
                'verbose_name': 'Lead',
                'verbose_name_plural': 'Leads',
            },
        ),
        migrations.CreateModel(
            name='LeadSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('form_template', models.CharField(blank=True, default='', help_text='The name of the html template file if needed.', max_length=70, verbose_name='form template name')),
                ('success_template', models.CharField(blank=True, default='', help_text='The name of the html template file if needed.', max_length=70, verbose_name='success page template name')),
            ],
            options={
                'verbose_name': 'Lead Source',
                'verbose_name_plural': 'Lead Sources',
            },
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, help_text='without VAT', max_digits=10, verbose_name='Amount')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Quantity')),
                ('shipping_date', models.DateField(blank=True, help_text='Shipment date as per contract', null=True, verbose_name='Shipping date')),
                ('planned_shipping_date', models.DateField(blank=True, null=True, verbose_name='Planned shipping date')),
                ('actual_shipping_date', models.DateField(blank=True, help_text='Date when the product was shipped', null=True, verbose_name='Actual shipping date')),
                ('product_is_shipped', models.BooleanField(default=False, help_text='Product is shipped', verbose_name='Shipped')),
                ('serial_number', models.CharField(blank=True, default='', max_length=50, verbose_name='serial number')),
            ],
            options={
                'verbose_name': 'Output',
                'verbose_name_plural': 'Outputs',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, help_text='without VAT', max_digits=10, verbose_name='Amount')),
                ('payment_date', models.DateField(default=datetime.date.today, verbose_name='Payment date')),
                ('status', models.CharField(choices=[('r', 'received'), ('g', 'guaranteed'), ('h', 'high probability'), ('l', 'low probability')], default='r', max_length=1, verbose_name='Payment status')),
                ('contract_number', models.CharField(blank=True, default='', max_length=40, verbose_name='contract number')),
                ('invoice_number', models.CharField(blank=True, default='', max_length=40, verbose_name='invoice number')),
                ('order_number', models.CharField(blank=True, default='', max_length=40, verbose_name='order number')),
                ('through_representation', models.BooleanField(default=False, verbose_name='Payment through representative office')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('name', models.CharField(default='', max_length=70, verbose_name='Name')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price')),
                ('on_sale', models.BooleanField(default=True, verbose_name='On sale')),
                ('type', models.CharField(choices=[('G', 'Goods'), ('S', 'Service')], default='G', max_length=1, null=True, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('name', models.CharField(default='', max_length=70, verbose_name='Name')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(default=datetime.date.today, verbose_name='Currency rate date')),
                ('rate_to_state_currency', models.DecimalField(decimal_places=8, help_text='Exchange rate against the state currency.', max_digits=13, verbose_name='Rate to state currency')),
                ('rate_to_marketing_currency', models.DecimalField(decimal_places=8, help_text='Exchange rate against the state currency.', max_digits=13, verbose_name='Rate to marketing currency')),
                ('rate_type', models.CharField(choices=[('A', 'approximate currency rate'), ('O', 'official currency rate')], default='A', max_length=1, verbose_name='Exchange rate type')),
            ],
            options={
                'verbose_name': 'Currency rate',
                'verbose_name_plural': 'Currency rates',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('request_for', models.CharField(max_length=250, verbose_name='Request for')),
                ('first_name', models.CharField(help_text='The name of the contact person (one word).', max_length=100, verbose_name='First name')),
                ('middle_name', models.CharField(blank=True, default='', help_text='The middle name of the contact person.', max_length=100, verbose_name='Middle name')),
                ('last_name', models.CharField(blank=True, default='', help_text='The last name of the contact person (one word).', max_length=100, verbose_name='Last name')),
                ('email', models.CharField(blank=True, default='', max_length=250)),
                ('phone', models.CharField(blank=True, default='', max_length=200)),
                ('website', models.URLField(blank=True, default='')),
                ('company_name', models.CharField(blank=True, default='', max_length=200, verbose_name='Company name')),
                ('receipt_date', models.DateField(blank=True, help_text='Date of receipt of the request.', null=True, verbose_name='Date of receipt')),
                ('city_name', models.CharField(blank=True, default='', max_length=100, verbose_name='City')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('translation', models.TextField(blank=True, default='', verbose_name='Translation')),
                ('remark', models.TextField(blank=True, default='', verbose_name='Remark')),
                ('pending', models.BooleanField(default=True, help_text='Waiting for validation of fields filling', verbose_name='Pending')),
                ('subsequent', models.BooleanField(default=False, help_text='Received from the client with whom you are already cooperate', verbose_name='Subsequent')),
                ('duplicate', models.BooleanField(default=False, help_text='Duplicate request. The deal will not be created.', verbose_name='Duplicate')),
                ('verification_required', models.BooleanField(default=False, help_text='Links are set automatically and require verification.', verbose_name='Verification required')),
                ('ticket', models.CharField(default=crm.utils.ticketproc.new_ticket, max_length=16)),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('default', models.BooleanField(default=False, help_text='Will be selected by default when creating a new task', verbose_name='Default')),
                ('index_number', models.SmallIntegerField(default=1, help_text='The sequence number of the stage.         The indices of other instances will be sorted automatically.')),
                ('second_default', models.BooleanField(default=False, help_text='Will be selected next after the default stage.', verbose_name='Second default')),
                ('success_stage', models.BooleanField(default=False, verbose_name='success stage')),
                ('conditional_success_stage', models.BooleanField(default=False, help_text='For example, receiving the first payment', verbose_name='conditional success stage')),
                ('goods_shipped', models.BooleanField(default=False, help_text='Have the goods been shipped at this stage already?', verbose_name='goods shipped')),
            ],
            options={
                'verbose_name': 'Stage',
                'verbose_name_plural': 'Stages',
                'ordering': ['index_number'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('name', models.CharField(default='', max_length=70, verbose_name='Tag name')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='ClientType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
            options={
                'verbose_name': 'Type of Clients',
                'verbose_name_plural': 'Types of Clients',
            },
        ),
        migrations.CreateModel(
            name='ClosingReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('index_number', models.SmallIntegerField(help_text='Reason rating.         The indices of other instances will be sorted automatically.')),
                ('success_reason', models.BooleanField(default=False, verbose_name='success reason')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
            options={
                'verbose_name': 'Closing reason',
                'verbose_name_plural': 'Closing reasons',
                'ordering': ['index_number'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('full_name', models.CharField(max_length=200, verbose_name='Company name')),
                ('alternative_names', models.CharField(blank=True, default='', help_text='Separate them with commas.', max_length=100, verbose_name='Alternative names')),
                ('website', models.CharField(blank=True, default='', max_length=200, verbose_name='Website')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('phone', models.CharField(blank=True, default='', max_length=100, verbose_name='Phone')),
                ('city_name', models.CharField(blank=True, default='', max_length=100, verbose_name='City name')),
                ('address', models.TextField(blank=True, default='', verbose_name='Address')),
                ('email', models.CharField(help_text='Use comma to separate Emails.', max_length=200, verbose_name='Email')),
                ('registration_number', models.CharField(blank=True, default='', help_text='Registration number of Company', max_length=30, verbose_name='Registration number')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('was_in_touch', models.DateField(blank=True, help_text='Last contact date', null=True, verbose_name='Last contact date')),
                ('token', models.CharField(default=common.utils.helpers.token_default, max_length=11, unique=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.city', verbose_name='City')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_department_related', to='auth.group', verbose_name='Department')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modified_by_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_owner_related', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.clienttype', verbose_name='Type of company')),
                ('country', models.ForeignKey(blank=True, help_text='Company Country', null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.country', verbose_name='country')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('first_name', models.CharField(help_text='The name of the contact person (one word).', max_length=100, verbose_name='First name')),
                ('middle_name', models.CharField(blank=True, default='', help_text='The middle name of the contact person.', max_length=100, verbose_name='Middle name')),
                ('last_name', models.CharField(blank=True, default='', help_text='The last name of the contact person (one word).', max_length=100, verbose_name='Last name')),
                ('title', models.CharField(blank=True, help_text='The title (position) of the contact person.', max_length=100, null=True, verbose_name='Title / Position')),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1, null=True, verbose_name='Sex')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('was_in_touch', models.DateField(blank=True, null=True, verbose_name='Last contact date')),
                ('email', models.CharField(help_text='Use comma to separate Emails.', max_length=200, verbose_name='Email')),
                ('secondary_email', models.EmailField(blank=True, default='', max_length=254, verbose_name='Secondary email')),
                ('phone', models.CharField(blank=True, default='', max_length=100, verbose_name='Phone')),
                ('other_phone', models.CharField(blank=True, default='', max_length=100)),
                ('mobile', models.CharField(blank=True, default='', max_length=100, verbose_name='Mobile phone')),
                ('skype', models.CharField(blank=True, default='', max_length=50)),
                ('city_name', models.CharField(blank=True, default='', max_length=50, verbose_name='City')),
                ('address', models.TextField(blank=True, default='')),
                ('description', models.TextField(blank=True, default='')),
                ('token', models.CharField(default=common.utils.helpers.token_default, max_length=11, unique=True)),
                ('city', models.ForeignKey(blank=True, help_text='Object of City in database', null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.city', verbose_name='Company city')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='crm.company', verbose_name='Company of contact')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_department_related', to='auth.group', verbose_name='Department')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modified_by_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_owner_related', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.country', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Contact person',
                'verbose_name_plural': 'Contact persons',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.country', verbose_name='Country'),
        ),
        migrations.CreateModel(
            name='CrmEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('subject', models.CharField(help_text='The subject of the message. You can use {{first_name}}, {{last_name}}, {{first_middle_name}} or {{full_name}}', max_length=250, verbose_name='Subject')),
                ('content', models.TextField()),
                ('prev_corr', models.TextField(blank=True, default='', help_text='Previous correspondence. Will be added after signature', verbose_name='Previous correspondence')),
                ('is_html', models.BooleanField(default=True)),
                ('to', models.TextField(help_text='You can specify multiple addresses, separated by commas', null=True, verbose_name='To')),
                ('from_field', models.CharField(blank=True, help_text='The Email address of sender', max_length=200, null=True, verbose_name='From')),
                ('cc', models.TextField(blank=True, help_text='You can specify multiple addresses, separated by commas', null=True)),
                ('bcc', models.TextField(blank=True, help_text='You can specify multiple addresses, separated by commas', null=True)),
                ('sent', models.BooleanField(default=False)),
                ('incoming', models.BooleanField(default=False)),
                ('trash', models.BooleanField(default=False)),
                ('inquiry', models.BooleanField(default=False)),
                ('read_receipt', models.BooleanField(default=False, help_text='Not supported by all mail services.', verbose_name='Request a read receipt')),
                ('uid', models.PositiveIntegerField(blank=True, null=True)),
                ('imap_host', models.CharField(blank=True, default='', max_length=100)),
                ('email_host_user', models.CharField(blank=True, default='', max_length=100)),
                ('ticket', models.CharField(blank=True, default='', max_length=16)),
                ('message_id', models.CharField(blank=True, default='', max_length=200)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_emails', to='crm.company', verbose_name='Company')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_emails', to='crm.contact', verbose_name='Contact')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_department_related', to='auth.group', verbose_name='Department')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modified_by_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_owner_related', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails in CRM',
            },
        ),
    ]
