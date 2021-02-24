### Signup
| API | Create a new user |
| ------ | ------ |
| Uri | ``` /api/v1/users/signup/ ``` |
| Method | ``` POST ``` |
| Content-Type | ``` application/json ``` |
| Response Data | ``` { username: <string:usrname>, email: <string:email>, password1: <string:password1>, password2: <string: password2>} ``` |


### Current Profile
| API | Get current logged in user profile |
| ------ | ------ |
| Uri | ``` /api/v1/users/profile ``` |
| Method | ```GET``` |
| Content-Type | ``` application/json ``` |
| Authorization Header | ``` Authorization: Bearer <your_access_token> ``` |
| Response Data | ``` { "id": <int: profile id>, "user": <int: user id>, "avatar": <string: avatar url> or <null>, "address": <string: address>, "gender": <string: gender> } ``` |


### Profile
| API | Get or Update a user profile |
| ------ | ------ |
| Uri | ``` /api/v1/users/[id]/profile ``` |
| Method | ``` GET, PUT, PATCH ``` |
| Content-Type | ``` application/json ``` |
| Authorization Header | ``` Authorization: Bearer <your_access_token> ``` |
| PUT/PATCH DATA | ``` { address: <string: address>, gender: <string:gender>, avatar: <string: base64 data> or null } ``` |
| GET RESPONSE | ``` { id: <int: profile id>, user: <int: user>, address: <string: address>, gender: <string: gender>, avatar: <string: url> or null } ``` |


### Profile List
| API | Get user profile list |
| ------ | ------ |
| Permission | ``` Only admin user can access this API ``` |
| Uri | ``` /api/v1/users/profiles/ ``` |
| Method | ``` GET ``` |
| Content-Type | ``` application/json ``` |
| Authorization Header | ``` Authorization: Bearer <your_access_token> ``` |
| Response Data | ``` { count: <int: count>, next: <string or null: next url>, previous: <string or null: previous url>, results: [ { id: <int: profile id>, user: <int: user id>, avatar: <string or null: avatar url>, address: <string: address>, gender: <string: gender> }, { id: <int: profile id>, user: <int: user id>, avatar: <string or null: avatar url>, address: <string: address>, gender: <string: gender> } ] } ``` |

