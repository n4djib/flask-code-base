import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy

from flask_graphql import GraphQLView

from app import app
# from app import db
from models import User, Post


# Objects Schema
class PostObject(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (graphene.relay.Node,)

class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_posts = SQLAlchemyConnectionField(PostObject)
    all_users = SQLAlchemyConnectionField(UserObject)


# noinspection PyTypeChecker
schema_query = graphene.Schema(query=Query)

# Mutation Objects Schema
class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        email = graphene.String(required=True)

    post = graphene.Field(lambda: PostObject)

    def mutate(self, info, title, body, email):
        user = User.query.filter_by(email=email).first()
        post = Post(title=title, body=body)
        if user is not None:
            post.author = user
        db.session.add(post)
        db.session.commit()
        return CreatePost(post=post)

class Mutation(graphene.ObjectType):
    save_post = CreatePost.Field()

# noinspection PyTypeChecker
schema_mutation = graphene.Schema(query=Query, mutation=Mutation)



def add_url_rules():
    # /graphql-query
    app.add_url_rule('/graphql-query', view_func=GraphQLView.as_view(
        'graphql-query',
        schema=schema_query, graphiql=True
    ))

    # /graphql-mutation
    app.add_url_rule('/graphql-mutation', view_func=GraphQLView.as_view(
        'graphql-mutation',
        schema=schema_mutation, graphiql=True
    ))


