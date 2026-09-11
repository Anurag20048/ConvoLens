from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Feedback


class HealthAndFeedbackTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_health_endpoint(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, 200)

    def test_feedback_submission(self):
        response = self.client.post(
            reverse("feedback"),
            {"bot_reply": "Helpful answer", "rating": True},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Feedback.objects.count(), 1)
