Packaging diagram:<br/>
[Packaging diagram image](/documentation/pictures/package_diagram.drawio.png)

Class diagram:<br/>
```mermaid
 classDiagram
    class House{
        id
        user_id
        parameters
    }
    class User{
        id
        username
        password
    }
    User <-- House
```
