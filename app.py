"""
Compatibility WSGI entrypoint for hosts configured with ``gunicorn app:app``.

The canonical Django entrypoint remains ``config.wsgi:application``. This
module exists so an older or manually configured Render service can still boot
while its dashboard Start Command is updated.
"""

from config.wsgi import application as app
