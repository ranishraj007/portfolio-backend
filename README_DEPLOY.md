# Deploying The Portfolio Backend

This backend is ready for hosts such as Render, Railway, or Heroku-style platforms.

## Required Environment Variables

Set these in your hosting dashboard:

```env
SECRET_KEY=make-this-long-and-random
DJANGO_DEBUG=False
ALLOWED_HOSTS=portfolio-backend-hpcb.onrender.com
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
CSRF_TRUSTED_ORIGINS=https://your-frontend-domain.com,https://portfolio-backend-hpcb.onrender.com
DATABASE_URL=postgres://user:password@host:5432/database
DB_SSL_REQUIRE=True
```

For a custom backend domain, add it to `ALLOWED_HOSTS` and include the
`https://` origin in `CSRF_TRUSTED_ORIGINS`.

After HTTPS is working, also set:

```env
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
```

## Build And Start Commands

Build command:

```bash
./build.sh
```

Start command:

```bash
gunicorn config.wsgi:application
```

Render must use that exact start command. If the deploy log says
`Running 'gunicorn app:app'`, open the Render service dashboard and replace
the Start Command with `gunicorn config.wsgi:application`.

This repo also includes `.python-version` and `render.yaml` so new Render
Blueprint deployments use Python 3.10.12 and the correct Django WSGI command.

If your platform does not run `build.sh`, use:

```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
```

## First Deploy Checklist

1. Create a PostgreSQL database on the host.
2. Add the environment variables above.
3. Deploy the GitHub repo.
4. Create your admin user if needed:

```bash
python manage.py createsuperuser
```

5. Seed your current portfolio data if the production database is empty:

```bash
python manage.py seed_portfolio
```

## API URLs

```text
GET  /api/v1/portfolio/
POST /api/v1/contact/
POST /api/v1/auth/login/
POST /api/v1/auth/refresh/
GET  /api/v1/admin/messages/
GET  /admin/
```
