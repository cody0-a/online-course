# Generated by Django 5.1.4 on 2024-12-14 18:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_list', '0003_alter_course_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='+251 000 000 0000', max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='profile_images')),
                ('bio', models.TextField()),
                ('education_level', models.CharField(choices=[('high school', 'high school'), ('bachelor degree', 'bachelor degree'), ('master degree', 'master degree'), ('phd', 'phd')], default='high school', max_length=100)),
                ('interest_in', models.CharField(choices=[('python', 'python'), ('django', 'django'), ('html', 'html'), ('css', 'css'), ('javascript', 'javascript'), ('flask', 'flask'), ('react', 'react')], default='python', max_length=100)),
                ('hobby', models.CharField(choices=[('coding', 'coding'), ('reading', 'reading'), ('watching movies', 'watching movies'), ('listening to music', 'listening to music'), ('playing games', 'playing games')], default='coding', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
