import pytest
from login.models import Posts
from model_bakery import baker
from django.urls import reverse


@pytest.mark.django_db
class TestPost:
    def test_create_object(self, fake, user):
        Posts.objects.create(
            user=user,
            title=fake.sentence(),
            text=fake.text()
        )
        post = Posts.objects.all()
        assert post.count() == 1

    def test_get_url(self, fake, user, user_client):
        post = Posts.objects.create(
            user=user,
            title=fake.sentence(),
            text=fake.text()
        )
        url = post.get_absolute_url()
        response = user_client.get(url)
        assert response.data["id"] == post.id


@pytest.mark.django_db
class TestApi:
    def test_get_queryset(self, fake, user, django_user_model, user_client):
        for i in range(10):
            Posts.objects.create(
                user=user,
                title=fake.sentence(),
                text=fake.text()
            )

        wrong_post = Posts.objects.create(
            user=baker.make(django_user_model, username=fake.name()),
            title=fake.sentence(),
            text=fake.text()
        )
        response = user_client.get(reverse('post-list'))
        assert response.status_code == 200
        assert len(response.data) == 10
        assert not any(entry["id"] == wrong_post.id for entry in response.data)
