import pytest
from django.urls import reverse
from goals import serializers
from tests import factories


@pytest.mark.django_db
def test_create(auth_client, new_user, category):
    response = auth_client.post(reverse('goal_create'),
                                data={'title': 'test goal', 'category': category.pk, 'description': 'testdescri'},)

    expected_response = {'id': response.data.get('id'),
                         'created': response.data.get('created'),
                         'updated': response.data.get('updated'),
                         'title': 'test goal',
                         'description': 'testdescri',
                         'status': 1,
                         'priority': 2,
                         'due_date': None,
                         'category': category.pk}

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_list(auth_client, new_user, category):
    goals = factories.GoalFactory.create_batch(5, category=category, user=new_user)
    response = auth_client.get(reverse('goal_list'))

    expected_response = serializers.GoalSerializer(instance=goals, many=True).data

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_retrieve(auth_client, goal, new_user, category):
    resource = auth_client.get(reverse('goal_pk', args=[goal.pk]))

    expected_response = {'id': goal.pk,
                         'user': {'id': new_user.pk,
                                  'username': 'testname',
                                  'first_name': '',
                                  'last_name': '',
                                  'email': 'test@mail.ru'},
                         'created': resource.data.get('created'),
                         'updated': resource.data.get('updated'),
                         'title': goal.title,
                         'description': '',
                         'status': 1,
                         'priority': 2,
                         'due_date': None,
                         'category': category.pk}

    assert resource.status_code == 200
    assert resource.data == expected_response


@pytest.mark.django_db
def test_update(auth_client, new_user, goal, category):
    response = auth_client.put(reverse('goal_pk', args=[goal.pk]),
                               data={'title': 'test updated goal', 'category': category.pk, 'description': 'test updated goal'})

    assert response.status_code == 200
    assert response.data.get('title') == 'test updated goal'


@pytest.mark.django_db
def test_delete(auth_client, goal):
    response = auth_client.delete(reverse('goal_pk', args=[goal.pk]))
    assert response.status_code == 204