from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='bob', password='pass')

    def test_can_list_posts(self):
        bob = User.objects.get(username='bob')
        Post.objects.create(owner=bob, title='a title')
        response = self.client.get('/posts/')
        print(response.data)
        print(len(response.data))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cannot_create_post(self):
        response = self.client.post('/posts/', {'content': 'a content'})
        count = Post.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        bob = User.objects.create_user(username='bob', password='pass')
        martin = User.objects.create_user(username='martin', password='pass')
        Post.objects.create(
            owner=bob, title='a title', contact='bob contact'
        )
        Post.objects.create(
            owner=martin, title='a title', contact='martin contact'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_post_using_invalid_it(self):
        response = self.client.get('/posts/99/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_cannot_update_another_users_post(self):
        self.client.login(username='bob', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
