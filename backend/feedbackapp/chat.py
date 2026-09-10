import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def chat_view(request):
    """Proxy a browser chat message to the Rasa REST webhook.

    Keeping Rasa behind Django avoids exposing the Rasa service directly to the
    public frontend and gives the application one API origin for chat + feedback.
    """
    message = str(request.data.get("message", "")).strip()
    sender = str(request.data.get("sender", "web-user")).strip() or "web-user"

    if not message:
        return Response({"detail": "message is required"}, status=400)

    rasa_url = os.getenv(
        "RASA_REST_URL",
        "http://127.0.0.1:5005/webhooks/rest/webhook",
    )
    payload = json.dumps({"sender": sender, "message": message}).encode("utf-8")
    req = Request(
        rasa_url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urlopen(req, timeout=30) as response:
            body = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        return Response(
            {"detail": "Rasa returned an error", "status": exc.code},
            status=502,
        )
    except (URLError, TimeoutError):
        return Response(
            {"detail": "Rasa service is unavailable"},
            status=503,
        )
    except (json.JSONDecodeError, UnicodeDecodeError):
        return Response(
            {"detail": "Invalid response from Rasa"},
            status=502,
        )

    return Response(body)
