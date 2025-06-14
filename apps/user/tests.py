# import pytest
# from rest_framework.test import APIClient
# from django.urls import reverse
# from apps.user.models import GDUser
#
#
# @pytest.mark.django_db
# class TestUserDetailView:
#     def test_get_user_details_authenticated(self):
#         """
#         Test that an authenticated user can retrieve their own details.
#         """
#         user = GDUser.objects.create_user(username='testuser', password='password123')
#         client = APIClient()
#         client.force_authenticate(user=user)
#         # Assuming 'user_details' is the name of the url pattern for this view
#         url = reverse('user_details')
#
#         response = client.get(url)
#
#         assert response.status_code == 200
#         assert response.data['username'] == user.username
#
#     def test_get_user_details_unauthenticated(self):
#         """
#         Test that an unauthenticated user cannot retrieve user details and gets a 403 Forbidden response.
#         """
#         client = APIClient()
#         # Assuming 'user_details' is the name of the url pattern for this view
#         url = reverse('user_details')
#
#         response = client.get(url)
#
#         assert response.status_code == 403
