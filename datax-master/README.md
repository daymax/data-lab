# DataX Project

## How to Run the Demo

Make sure docker compose is installed.

```bash
docker-compose up
```

Admin Account:

```
username: superadmin
password: digglife
```

## Note

1. Email Settings

    A valid smtp server is required for sending email from Django application.
    Say if you want send email from `noreply@datax.com` address, you have to own the domain name `datax.com` and setup a smtp server with it.

    Of course you can also use Gmail or whatever email provider, as long as you use their SMTP server. For example:

    ```
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = '587'
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'digglife@gmail.com'
    EMAIL_HOST_PASSWORD = 'verysecurepassword'
    DEFAULT_FROM_EMAIL = 'digglife@gmail.com'
    ```
