from app import db
from models import User, Post

db.create_all()     # create tables from models

user1 = User(
    name="Sadhan Sarker",
    email='cse.sadhan@gmail.com'
)
user2 = User(
    name="nadjib saddedine",
    email='n4djib@gmail.com'
)

post1 = Post()
post1.title = "Blog Post Title 1"
post1.body = "This is the first blog post 1"
post1.author = user1

post2 = Post()
post2.title = "Blog Post Title 2"
post2.body = "This is the first blog post 2"
post2.author = user2

db.session.add(post1)
db.session.add(user1)
db.session.add(post2)
db.session.add(user2)
db.session.commit()

print(User.query.all())
print(Post.query.all())


### RUN
# python seed.py
