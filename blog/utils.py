
import random
from faker import Faker
from blog.models import Category, Tag
def generate_data():
    fake = Faker()
    # fake.text(100) title 
    # fake.text(1000) body
    # fake.random.randint(1,600) views 
    cats = Category.objects.all()
    print(random.choice(cats))
    post = Post.objects.create()
    post.category = random.choice(cats)
    for i in range(random.randint(1,4)):
        post.tag.add(random.choice(Tag.objects.all()))
    # fake.random.randint(1,100) up , down
    # print(fake.random.randint(1,600))
    # for i in range(10):
generate_data()

