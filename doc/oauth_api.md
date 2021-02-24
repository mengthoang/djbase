```sh
    - Create application at http://localhost:8000/admin/oauth2_provider/application/
    with (Grant Type=Confidential) and (Authorization grant type=Resource owner password-based)
    - Request token: curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/
    - Requeset API: curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/users/
    - Request refresh token: curl -X POST -d "grant_type=refresh_token&refresh_token=<your_refresh_token>&client_id=<your_client_id>&client_secret=<your_client_secret>" http://localhost:8000/o/token/
```