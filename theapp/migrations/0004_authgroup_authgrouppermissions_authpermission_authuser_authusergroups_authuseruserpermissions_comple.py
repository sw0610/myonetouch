# Generated by Django 3.0.8 on 2020-09-28 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('theapp', '0003_auto_20200929_0644'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Complete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete_vote', models.IntegerField()),
            ],
            options={
                'db_table': 'complete',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MajorVote',
            fields=[
                ('mj_vt_pk', models.IntegerField(primary_key=True, serialize=False)),
                ('mj_vt_name', models.CharField(max_length=45)),
                ('mj_vt_dday', models.DateField()),
                ('mj_category1', models.CharField(blank=True, max_length=45, null=True)),
                ('mj_category2', models.CharField(blank=True, max_length=45, null=True)),
                ('mj_category3', models.CharField(blank=True, max_length=45, null=True)),
                ('mj_category4', models.CharField(blank=True, max_length=45, null=True)),
                ('mj_category5', models.CharField(blank=True, max_length=45, null=True)),
                ('mj_vt_result1', models.CharField(blank=True, max_length=45, null=True)),
                ('mj_vt_result2', models.CharField(blank=True, max_length=45, null=True)),
                ('mj_vt_result3', models.CharField(blank=True, max_length=45, null=True)),
                ('mj_vt_result4', models.CharField(blank=True, max_length=45, null=True)),
                ('mj_vt_result5', models.CharField(blank=True, max_length=45, null=True)),
                ('mj_final_result', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'major_vote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('mb_number', models.IntegerField(primary_key=True, serialize=False)),
                ('mb_pw', models.IntegerField()),
                ('mb_undergraduate', models.CharField(max_length=45)),
                ('mb_major', models.CharField(max_length=45)),
                ('mb_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'member',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('nt_pk', models.IntegerField(primary_key=True, serialize=False)),
                ('nt_title', models.CharField(max_length=45)),
                ('nt_writer', models.CharField(max_length=45)),
                ('nt_count', models.IntegerField(blank=True, null=True)),
                ('nt_updateday', models.DateField()),
                ('nt_content', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'notice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolVote',
            fields=[
                ('sh_vt_pk', models.IntegerField(primary_key=True, serialize=False)),
                ('sh_vt_name', models.CharField(max_length=45)),
                ('sh_vt_dday', models.DateField()),
                ('sh_category1', models.CharField(blank=True, max_length=45, null=True)),
                ('sh_category2', models.CharField(blank=True, max_length=45, null=True)),
                ('sh_category3', models.CharField(blank=True, max_length=45, null=True)),
                ('sh_category4', models.CharField(blank=True, max_length=45, null=True)),
                ('sh_category5', models.CharField(blank=True, max_length=45, null=True)),
                ('sh_vt_result1', models.CharField(blank=True, max_length=45, null=True)),
                ('sh_vt_result2', models.CharField(blank=True, max_length=45, null=True)),
                ('sh_vt_result3', models.CharField(blank=True, max_length=45, null=True)),
                ('sh_vt_result4', models.CharField(blank=True, max_length=45, null=True)),
                ('sh_vt_result5', models.CharField(blank=True, max_length=45, null=True)),
                ('sh_final_result', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'school_vote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SuggestOther',
            fields=[
                ('sgother_pk', models.IntegerField(primary_key=True, serialize=False)),
                ('sgother_title', models.CharField(max_length=45)),
                ('sgother_writer', models.CharField(max_length=45)),
                ('sgother_count', models.IntegerField(blank=True, null=True)),
                ('sgother_updateday', models.DateField()),
                ('sgother_content', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'suggest_other',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SuggestVote',
            fields=[
                ('sgvote_pk', models.IntegerField(primary_key=True, serialize=False)),
                ('sgvote_title', models.CharField(max_length=45)),
                ('sgvote_writer', models.CharField(max_length=45)),
                ('sgvote_count', models.IntegerField(blank=True, null=True)),
                ('sgvote_updateday', models.DateField()),
                ('sgvote_content', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'suggest_vote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UndergraduateVote',
            fields=[
                ('ud_vt_pk', models.IntegerField(primary_key=True, serialize=False)),
                ('ud_vt_name', models.CharField(max_length=45)),
                ('ud_vt_dday', models.DateField()),
                ('ud_category1', models.CharField(blank=True, max_length=45, null=True)),
                ('ud_category2', models.CharField(blank=True, max_length=45, null=True)),
                ('ud_category3', models.CharField(blank=True, max_length=45, null=True)),
                ('ud_category4', models.CharField(blank=True, max_length=45, null=True)),
                ('ud_category5', models.CharField(blank=True, max_length=45, null=True)),
                ('ud_vt_result1', models.CharField(blank=True, max_length=45, null=True)),
                ('ud_vt_result2', models.CharField(blank=True, max_length=45, null=True)),
                ('ud_vt_result3', models.CharField(blank=True, max_length=45, null=True)),
                ('ud_vt_result4', models.CharField(blank=True, max_length=45, null=True)),
                ('ud_vt_result5', models.CharField(blank=True, max_length=45, null=True)),
                ('ud_final_result', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'undergraduate_vote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VoteList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'vote_list',
                'managed': False,
            },
        ),
    ]
