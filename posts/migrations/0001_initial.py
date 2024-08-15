# Generated by Django 5.1 on 2024-08-15 09:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, default='../default_post_penf1s', upload_to='images/')),
                ('image_filter', models.CharField(choices=[('action_adventure', 'Action/Adventure fiction'), ('art_photography', 'Art & photography'), ('autobiography_memoir', 'Autobiography/Memoir'), ('biography', 'Biography'), ('childrens_fiction', 'Children’s fiction'), ('classic_fiction', 'Classic fiction'), ('contemporary_fiction', 'Contemporary fiction'), ('essays', 'Essays'), ('fantasy', 'Fantasy'), ('food_drink', 'Food & drink'), ('graphic_novel', 'Graphic novel'), ('historical_fiction', 'Historical fiction'), ('horror', 'Horror'), ('how_to_guides', 'How-To/Guides'), ('humanities_social_sciences', 'Humanities & social sciences'), ('humor', 'Humor'), ('lgbtq', 'LGBTQ+'), ('literary_fiction', 'Literary fiction'), ('mystery', 'Mystery'), ('new_adult', 'New adult'), ('parenting', 'Parenting'), ('philosophy', 'Philosophy'), ('religion_spirituality', 'Religion & spirituality'), ('romance', 'Romance'), ('satire', 'Satire'), ('science_fiction', 'Science fiction'), ('science_technology', 'Science & technology'), ('self_help', 'Self-help'), ('short_story', 'Short story'), ('thriller', 'Thriller'), ('travel', 'Travel'), ('true_crime', 'True crime'), ('western', 'Western'), ('womens_fiction', 'Women’s fiction'), ('young_adult', 'Young adult')], default='normal', max_length=32)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
