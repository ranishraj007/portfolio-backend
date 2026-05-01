from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from .models import About, ContactMessage


class PortfolioApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_portfolio_endpoint_returns_frontend_shape(self):
        About.objects.create(
            name='Ranish Raj Shrestha',
            title='Frontend Developer',
            address='Kathmandu',
            contact='9840800899',
            email='ranish@example.com',
            github='https://github.com/ranishraj007',
            linkedin='https://www.linkedin.com/in/ranish-raj-shrestha-89aa32207/',
            summary='Portfolio summary',
        )

        response = self.client.get('/api/v1/portfolio/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            set(response.data.keys()),
            {'about', 'experience', 'education', 'projects', 'skills', 'languages'},
        )
        self.assertEqual(response.data['about']['name'], 'Ranish Raj Shrestha')
        self.assertEqual(response.data['skills'], [])

    def test_contact_endpoint_saves_message(self):
        response = self.client.post(
            '/api/v1/contact/',
            {
                'name': 'Visitor',
                'email': 'visitor@example.com',
                'message': 'Hello from the frontend.',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_admin_messages_endpoint_requires_authentication(self):
        response = self.client.get('/api/v1/admin/messages/')

        self.assertEqual(response.status_code, 401)

    def test_authenticated_user_can_read_admin_messages(self):
        user = User.objects.create_user(username='admin', password='secret-pass')
        self.client.force_authenticate(user=user)
        ContactMessage.objects.create(
            name='Visitor',
            email='visitor@example.com',
            message='Private message',
        )

        response = self.client.get('/api/v1/admin/messages/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
