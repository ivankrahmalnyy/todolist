import factory

from core.models import User
from goals import models as goal_models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("email")
    password = "superPassword21"


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = goal_models.Board

    title = factory.Faker("name")


class ParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = goal_models.BoardParticipant


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = goal_models.GoalCategory

    title = factory.Faker("name")


class GoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = goal_models.Goal

    title = factory.Faker("name")

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = goal_models.GoalComment

    text = "text comment"