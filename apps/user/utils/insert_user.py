from django.contrib.auth.models import User

user = User.objects.create_user('nBarmane', 'n.barmane@gmail.com', '123456')
user.last_name = 'Nouamane'
user.first_name = 'BARMANE'
user.save()
