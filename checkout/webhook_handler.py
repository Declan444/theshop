from django.http import HttpResponse

class StripeWH_Handler:
    """Handle Strip weebhooks"""

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook receeived: {event['type']}',
            status=200
        )