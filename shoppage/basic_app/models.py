# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BillDetail(models.Model):
    id_bill = models.ForeignKey('Bills', models.DO_NOTHING, db_column='id_bill')
    id_product = models.ForeignKey('Products', models.DO_NOTHING, db_column='id_product')
    quantity = models.IntegerField()
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_detail'
        get_latest_by = ['id']

class Bills(models.Model):
    id_customer = models.ForeignKey('Customers', models.DO_NOTHING, db_column='id_customer')
    date_order = models.DateField(auto_now_add = True)
    total = models.FloatField()
    promt_price = models.FloatField()
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True)
    token_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bills'
        get_latest_by = ['id']

class Categories(models.Model):
    name = models.CharField(max_length=200)
    id_url = models.ForeignKey('PageUrl', models.DO_NOTHING, db_column='id_url', blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categories'


class Customers(models.Model):
    male = 'male'
    female = 'female'
    other = 'other'
    GENDER_CHOICE = [
        (male , 'male'),
        (female , 'female'),
        (other , 'other'),
    ]
    name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices = GENDER_CHOICE,
        default = other,
        )
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    # def __str__(self):
    #     return '%s %s' % (self.name,self.email)

    class Meta:
        managed = False
        db_table = 'customers'
        get_latest_by = ['id']



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PageUrl(models.Model):
    url = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'page_url'


class Products(models.Model):
    id_type = models.ForeignKey(Categories, models.DO_NOTHING, db_column='id_type')
    id_url = models.ForeignKey(PageUrl, models.DO_NOTHING, db_column='id_url', blank=True, null=True)
    name = models.CharField(max_length=100)
    detail = models.TextField(blank=True, null=True)
    price = models.FloatField()
    promotion_price = models.FloatField()
    promotion = models.CharField(max_length=500, blank=True, null=True)
    image = models.CharField(max_length=100)
    status = models.IntegerField()
    new = models.IntegerField()
    update_at = models.DateField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products'


class Role(models.Model):
    role = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'role'


class RoleUser(models.Model):
    role = models.ForeignKey(Role, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_user'


class Slide(models.Model):
    image = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'slide'


class SocialProvider(models.Model):
    provider_id = models.CharField(unique=True, max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    provider = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_provider'


class Users(models.Model):
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True)
    remember_token = models.CharField(max_length=1000, blank=True, null=True)
    active = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
