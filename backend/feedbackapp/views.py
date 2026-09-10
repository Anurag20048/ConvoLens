import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Feedback

@api_view(['POST', 'GET'])
def feedback_view(request):
    secret_key = os.getenv('FEEDBACK_ADMIN_KEY', '')

    if request.method == 'POST':
        data = request.data
        Feedback.objects.create(
            bot_reply=data.get('bot_reply', ''),
            rating=bool(data.get('rating'))
        )
        return Response({'status': 'ok'})

    key = request.GET.get('key')
    if not secret_key or key != secret_key:
        return Response({'detail': 'Forbidden'}, status=403)

    feedbacks = Feedback.objects.all().order_by('-created')
    return Response([
        {'bot_reply': f.bot_reply, 'rating': f.rating, 'created': f.created}
        for f in feedbacks
    ])
