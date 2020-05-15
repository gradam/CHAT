import pytest
from login.models import Posts


@pytest.mark.django_db
class TestPost:
    def test_create_object(self, fake, user):
        Posts.objects.create(
            user=user, 
            title='Test', 
            text=fake.text()
            )
        
        post = Posts.objects.all()
        assert post.count() == 1
    