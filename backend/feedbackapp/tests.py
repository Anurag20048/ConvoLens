from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from .models import Feedback


class FeedbackApiTests(TestCase):
    def test_feedback_post_creates_record(self):
        response = self.client.post(
            reverse("feedback"),
            {"bot_reply": "Hello", "rating": 1},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Feedback.objects.count(), 1)
        self.assertTrue(Feedback.objects.first().rating)

    def test_chat_requires_message(self):
        response = self.client.post(
            reverse("chat"),
            {},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    @patch("feedbackapp.chat.urlopen")
    def test_chat_proxies_to_rasa(self, mock_urlopen):
        class FakeResponse:
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc_value, traceback):
                return False

            def read(self):
                return b'[{"text":"Hello from Rasa"}]'

        mock_urlopen.return_value = FakeResponse()

        response = self.client.post(
            reverse("chat"),
            {"sender": "test-user", "message": "hello"},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"text": "Hello from Rasa"}])
        mock_urlopen.assert_called_once()
