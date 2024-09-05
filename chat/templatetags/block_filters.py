from django import template
from chat.models import BlockedUser

register = template.Library()


@register.filter
def is_blocked(blocker, blocked):
    """Return True if the blocker has blocked the user, else False."""
    return BlockedUser.objects.filter(blocker=blocker, blocked=blocked).exists()
