import pytest

from login.models import Post


@pytest.mark.django_db
def test_get_url(fake, user, user_client):
    post = Post.objects.create(
        user=user,
        title=fake.sentence(),
        text=fake.text()
    )

    url = post.get_absolute_url()
    response = user_client.get(url)

    assert response.data["id"] == post.id
