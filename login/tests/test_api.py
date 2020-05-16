import pytest
from django.urls import reverse
from model_bakery import baker

from login.models import Post


@pytest.mark.django_db
def test_get_queryset(fake, user, django_user_model, user_client):
    for i in range(10):
        Post.objects.create(
            user=user,
            title=fake.sentence(),
            text=fake.text()
        )

    wrong_post = Post.objects.create(
        user=baker.make(django_user_model, username=fake.name()),
        title=fake.sentence(),
        text=fake.text()
    )

    response = user_client.get(reverse('post-list'))

    assert response.status_code == 200
    assert len(response.data) == 10
    assert not any(entry["id"] == wrong_post.id for entry in response.data)
