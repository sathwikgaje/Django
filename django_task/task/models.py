from django.db import models

# Create your models here.
class CompanyDetailsTb(models.Model):
    id = models.TextField(blank=True, null=False,primary_key=True)
    sub_category = models.TextField(db_column='Sub_Category', blank=True, null=True)  # Field name made lowercase.
    company_name = models.TextField(db_column='Company_name', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company_details_tb'


class DetailsTb(models.Model):
    id = models.TextField(blank=True, null=False,primary_key=True)
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sub_category = models.TextField(db_column='Sub_Category', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'details_tb'

class JobCategoriesTb(models.Model):
    id = models.TextField(blank=True, null=False,primary_key=True)
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'job_categories_tb'


class JobSubCategoriesTb(models.Model):
    id = models.TextField(blank=True, null=False,primary_key=True)
    sub_category = models.TextField(db_column='Sub_Category', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'job_sub_categories_tb'


class JobsDetailsTb(models.Model):
    id = models.TextField(blank=True, null=False,primary_key=True)
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sub_category = models.TextField(db_column='Sub_Category', blank=True, null=True)  # Field name made lowercase.
    company_name = models.TextField(db_column='Company_name', blank=True, null=True)  # Field name made lowercase.
    job_position = models.TextField(db_column='Job_Position', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jobs_details_tb'


class StatesTb(models.Model):
    id = models.TextField(blank=True, null=False,primary_key=True)
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'states_tb'


class SubDetailsTb(models.Model):
    id = models.TextField(blank=True, null=False,primary_key=True)
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sub_category = models.TextField(db_column='Sub_Category', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sub_details_tb'
