from django_comments.moderation import CommentModerator, moderator
from comments_moderation import settings
from .models import EmailFilter

class FilteredCommentsModerator(CommentModerator):
    def moderate(self, comment, content_object, request):
        if settings.MODERATION_MODE == 'approve':
            moderate_states = ('moderate',)
        else:
            moderate_states = ('moderate', 'new')
        if EmailFilter.objects.filter(email = comment.user_email, active__in = moderate_states).count() > 0:
            return True
        email_filter = EmailFilter(email = comment.user_email)
        email_filter.save()
        return settings.MODERATION_MODE == 'approve'

def register(model):
    moderator.register(model, FilteredCommentsModerator)
