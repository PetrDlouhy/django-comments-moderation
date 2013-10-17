django-comments-moderation
==========================

This is addition to django-fluent-comments.

This module registers all emails from comments and allows to sed moderation rules for them.


installation
============

   pip install -e git+https://github.com/PetrDlouhy/django-comments-moderation.git#egg=django-comments-moderation


Add ``comments_moderation`` to your INSTALLED_APPS::

   INSTALLED_APPS = (
       'comments_moderation',
   )

Register comments moderator - add following lines to admin.py::

   from comments_moderation import filtered_moderator
   filtered_moderator.register(CommentedObject)

You can select moderation mode for new users from two modes - 'approve' and 'moderate'.
If you want to moderate all comments from new users, set::

   COMMENTS_MODERATION_MODE = 'moderate'

Migrate your models::

   ./manage.py migrate comments_moderation
