#### Installation
  ```sh
    - Clone the source code.
    $ cd djbase
    - Copy .env.example and paste as .env
    - Update environment variable in .env if you don't want to use default value.
  ```
  - Without Docker
  ```sh
    $ pip install -r requirements/base.txt
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver 0.0.0.0:8000
  ```
  - With Docker
  ```sh
    - Install Docker (https://docs.docker.com/engine/install/)
    - Install Docker Compose (https://docs.docker.com/compose/install/)
    $ ./scripts/djabase.sh init
    $ ./scripts/djabase.sh start
    - If you have some update on model fields please execute command bellow.
    $ ./scripts/djabase.sh makemigrations
    $ ./scripts/djabase.sh migrate
  ```

#### APIs

- Oauth API [doc/oauth_api.md](https://github.com/chhanhtrao/DjBase/blob/master/doc/oauth_api.md) 
- User APIs
    + [Signup](https://github.com/chhanhtrao/DjBase/blob/master/doc/user_api.md#signup)
    + [Current Profile](https://github.com/chhanhtrao/DjBase/blob/master/doc/user_api.md#current-profile)
    + [Profile](https://github.com/chhanhtrao/DjBase/blob/master/doc/user_api.md#profile)
    + [Profile List](https://github.com/chhanhtrao/DjBase/blob/master/doc/user_api.md#profile-list)

