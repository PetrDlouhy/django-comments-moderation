django-comments-moderation
==========================

This is addition to django-fluent-comments.

This module registers all emails from comments and allows to set moderation rules for them (blacklist/whitelist).


installation
============

.. code-block:: bash

    pip install django-comments-moderation
    
OR

.. code-block:: bash

    pip install -e git+https://github.com/PetrDlouhy/django-comments-moderation.git#egg=django-comments-moderation


Add ``comments_moderation`` to your INSTALLED_APPS:

.. code-block::

    INSTALLED_APPS = (
        ...
        'comments_moderation',
        ...
    )

Register comments moderator - add following lines to admin.py:

.. code-block:: python

    from comments_moderation import filtered_moderator
    filtered_moderator.register(CommentedObject)

You can select moderation mode for new users from two modes - ``'approve'`` and ``'moderate'``.
If you want to moderate all comments from new users, set:

.. code-block::

    COMMENTS_MODERATION_MODE = 'moderate'

Migrate your models:

.. code-block:: bash

    ./manage.py migrate comments_moderation
    
Now you should see new application ``comments_moderation`` with model ``Email filters`` in your admin interface.
