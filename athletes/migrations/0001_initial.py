# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields
import athletes.pdffile
from django.conf import settings
import django_thumbs.db.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '__first__'),
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sports', '0003_auto_20161012_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year_acad_graduation', models.IntegerField(default=2016, max_length=4, verbose_name=b'year', choices=[(2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009)])),
                ('school', models.CharField(max_length=140)),
                ('logros', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Academic Info',
            },
        ),
        migrations.CreateModel(
            name='Archivement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=2016, max_length=4, verbose_name=b'year', choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)])),
                ('descriptions', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Athlete_history',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=2016, max_length=4, verbose_name=b'year', choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)])),
                ('highschool', models.CharField(max_length=55)),
                ('descriptions', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Athlete_profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=35)),
                ('middle_name', models.CharField(max_length=35, null=True, blank=True)),
                ('last_name', models.CharField(max_length=35)),
                ('birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(max_length=8, null=True, blank=True)),
                ('address', models.CharField(max_length=140)),
                ('address2', models.CharField(max_length=140)),
                ('image_profile', django_thumbs.db.models.ImageWithThumbsField(upload_to=b'profilephoto')),
                ('country', models.CharField(default=b'United States', max_length=45, choices=[(b'united_states', b'United States')])),
                ('ncaa', models.CharField(max_length=11, null=True, blank=True)),
                ('home_phone', models.CharField(max_length=16)),
                ('cel_phone', models.CharField(max_length=16)),
                ('guardian1', models.CharField(max_length=25, choices=[(b'Mother', b'Mother'), (b'Father', b'Father')])),
                ('g_first_name', models.CharField(max_length=35)),
                ('g_last_name', models.CharField(max_length=35)),
                ('g_phone', models.CharField(max_length=16)),
                ('g_mail', models.EmailField(max_length=250)),
                ('guardian2', models.CharField(blank=True, max_length=25, null=True, choices=[(b'Coach', b'Coach'), (b'Manager', b'Manager'), (b'Mother', b'Mother'), (b'Father', b'Father')])),
                ('g2_first_name', models.CharField(max_length=35, null=True, blank=True)),
                ('g2_last_name', models.CharField(max_length=35, null=True, blank=True)),
                ('g2_phone', models.CharField(max_length=16, null=True, blank=True)),
                ('g2_mail', models.EmailField(max_length=250, null=True, blank=True)),
                ('gpa', models.DecimalField(max_digits=3, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('sat', models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(2400.0)])),
                ('act', models.DecimalField(blank=True, null=True, max_digits=2, decimal_places=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(36.0)])),
                ('gpa_pdf', athletes.pdffile.ContentTypeRestrictedFileField(null=True, upload_to=b'pdf/gpa', blank=True)),
                ('sat_pdf', athletes.pdffile.ContentTypeRestrictedFileField(null=True, upload_to=b'pdf/sat', blank=True)),
                ('act_pdf', athletes.pdffile.ContentTypeRestrictedFileField(null=True, upload_to=b'pdf/act', blank=True)),
                ('hs_grad_year', models.IntegerField(default=2016, max_length=4, verbose_name=b'year', choices=[(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)])),
                ('personal_statement', models.TextField(blank=True)),
                ('varsity_yn', models.CharField(max_length=3, null=True, blank=True)),
                ('varsity_club', models.CharField(max_length=55, null=True, blank=True)),
                ('varsity_years', models.CharField(blank=True, max_length=1, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')])),
                ('weight', models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(250)])),
                ('height', models.CharField(max_length=10, null=True, blank=True)),
                ('slug', models.SlugField(editable=False)),
                ('position', models.ForeignKey(to='administrator.Position', null=True)),
                ('profile_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('sport', models.ForeignKey(to='sports.Sport', null=True)),
                ('state', models.ForeignKey(to='base.State')),
            ],
            options={
                'verbose_name_plural': 'Athlete Profile',
            },
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=2016, max_length=4, verbose_name=b'year', choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)])),
                ('awards', models.CharField(max_length=55)),
                ('descriptions', models.CharField(max_length=100)),
                ('profile', models.ForeignKey(to='athletes.Athlete_profile')),
            ],
        ),
        migrations.CreateModel(
            name='Club_season_history',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=2016, max_length=4, verbose_name=b'year', choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)])),
                ('club', models.CharField(max_length=55)),
                ('descriptions', models.CharField(max_length=100)),
                ('profile', models.ForeignKey(to='athletes.Athlete_profile')),
            ],
        ),
        migrations.CreateModel(
            name='Coaches_reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coach_name', models.CharField(max_length=50, null=True, blank=True)),
                ('position', models.CharField(max_length=50, null=True, blank=True)),
                ('phone', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.EmailField(max_length=250, null=True, blank=True)),
                ('profile', models.ForeignKey(to='athletes.Athlete_profile')),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.CharField(max_length=45)),
                ('evaluations', models.ForeignKey(to='administrator.Evaluations')),
                ('profile', models.ForeignKey(to='athletes.Athlete_profile')),
                ('sport', models.ForeignKey(to='sports.Sport')),
            ],
            options={
                'verbose_name_plural': 'Stats',
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video1', embed_video.fields.EmbedVideoField(null=True, verbose_name=b'Video 1', blank=True)),
                ('video2', embed_video.fields.EmbedVideoField(null=True, verbose_name=b'Video 2', blank=True)),
                ('athlete', models.ForeignKey(to='athletes.Athlete_profile')),
            ],
            options={
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.AddField(
            model_name='athlete_history',
            name='profile',
            field=models.ForeignKey(to='athletes.Athlete_profile'),
        ),
        migrations.AddField(
            model_name='archivement',
            name='profile',
            field=models.ForeignKey(to='athletes.Athlete_profile'),
        ),
        migrations.AddField(
            model_name='academic_info',
            name='profile',
            field=models.ForeignKey(to='athletes.Athlete_profile'),
        ),
    ]
