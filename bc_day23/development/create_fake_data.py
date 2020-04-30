import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# print(User.objects.all())

user_ids = [user.id for user in User.objects.all() if user.id >= 2]
# print(user_ids)

from posts.models import Post

dummy_text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis repellendus ipsa sit delectus, repudiandae illum distinctio mollitia, cupiditate nostrum fugit, totam cumque rem aspernatur facere. Sequi ullam aut assumenda ducimus, accusamus deserunt nobis alias, in exercitationem eligendi, aperiam eum ipsum quae rerum, id enim! Itaque voluptatem placeat assumenda qui, sint enim minima ad, aliquam officiis eum minus velit magnam pariatur animi omnis. Alias molestias magnam illo deleniti, odio nostrum qui fuga accusantium aperiam quos sequi. Sed nostrum beatae sapiente perferendis adipisci natus quod. Nisi, beatae in! Autem illum distinctio minima enim incidunt aspernatur, dolorem aperiam odit maiores! Ipsam, perspiciatis, rerum.'.split()

def rand_select(num):
	return [random.choice(dummy_text) for i in range(num)]


post_entries = 20


for i in range(post_entries):
	# user = User.objects.get(pk=random.choice(user_ids))	
	title = ' '.join(rand_select(random.randint(3,7))).title()
	author = ' '.join(rand_select(random.randint(1,3))).title()
	message = ' '.join(rand_select(random.randint(40,100))).capitalize()

	Post.objects.get_or_create(
		# user=user,
		title=title,
		author=author,
		message=message)
