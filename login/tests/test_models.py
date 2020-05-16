import pytest

from login.models import Post


@pytest.mark.django_db
def test_create_object(fake, user):
    Post.objects.create(
        user=user,
        title=fake.sentence(),
        text=fake.text()
    )

    post = Post.objects.all()

    assert post.count() == 1
