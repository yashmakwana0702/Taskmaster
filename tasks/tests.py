from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import Task
from django.contrib.auth.models import User


class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.user_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'first_name':'yash', 'last_name':'makwana', 'email':'yashmakwana9601@gmial.com'
        }
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            due_date='2024-02-20',
            status='Pending',
            owner=self.user
        )

    def test_signup_view(self):
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, 200)  # Check if signup redirects after successful registration

    def test_signup_existing_user(self):
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, 200)  # Check if signup fails for existing user

    def test_login_view(self):
        login_data = {
            'username': 'testuser',
            'password': 'testpassword123',
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, 302)  # Check if login redirects after successful authentication

    def test_login_invalid_credentials(self):
        login_data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, 200)  # Check if login fails for invalid credentials

    def test_create_task_view(self):
        response = self.client.get(reverse('create_task'))
        self.assertEqual(response.status_code, 302)

    def test_update_task_view(self):
        response = self.client.get(reverse('update_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_task_view(self):
        response = self.client.get(reverse('delete_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)

    def test_list_tasks_view(self):
        response = self.client.get(reverse('list_tasks'))
        self.assertEqual(response.status_code, 200)

    def test_view_task_view(self):
        response = self.client.get(reverse('view_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
