from django.contrib.comments.moderation import CommentModerator, moderator

class FilteredCommentsModerator(CommentModerator):
    def moderate(self, comment, content_object, request):
        if EmailFilter.objects.filter(email = comment.user_email, active = True).count() > 0:
            return True
        email_filter = EmailFilter(email = comment.user_email, active = False)
        email_filter.save()
        return False
