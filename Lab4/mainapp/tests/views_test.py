import pytest
from django.urls import reverse
from constants import BASE_VIEWS, SPECIFIC_VIEWS
from django.test import Client
from fixts import user, client

@pytest.mark.parametrize('view', BASE_VIEWS)
@pytest.mark.django_db
def test_general_access(user, client:Client, view):
    response = client.get(reverse(view))
    assert response.status_code == 200

    client.force_login(user)
    response = client.get(reverse(view))
    assert response.status_code == 200


@pytest.mark.parametrize('view', SPECIFIC_VIEWS)
@pytest.mark.django_db
def test_user_access(user, client:Client, view):
    client.force_login(user)
    response = client.get(reverse(view))
    assert response.status_code == 200


@pytest.mark.parametrize('view', SPECIFIC_VIEWS)
@pytest.mark.django_db
def test_nonuser_access(client:Client, view):
    response = client.get(reverse(view))
    assert response.status_code == 303
