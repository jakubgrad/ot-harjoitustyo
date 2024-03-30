### Specification document = Määrittelydokumentti = Vaatimusmarittely<br />
**Purpose of the application**<br />
The application is designed for (finnish) household owners to estimate their energy consumption and pollution based on the information about their houses and a simple energy model.<br />
**Users**<br />
A user can log in and fill out an assessment of their home. <br />
There could possibly exist an admin group who can change the parameters of the model. <br />

**User interface draft**<br />
A user is welcomed by login/register buttons. If they click register, they're taken to registration. If they choose login, they are presented with the information about their house. If they haven't created it yet, there will be a "Create new house" button, clicking on which a user is taken to an assessment.<br /><br />

![User interface draft](/documentation/user_interface_draft.png)

**Functionality**<br />
- Before logging in:<br />
- The user can register in the system<br />
- The user can log into the system with existing credentials<br />
- If the user does not exist, or the password does not match, there is information about it<br />
**After logging in**
- The user can complete an assesment of their home.<br />
- Afterwards they can see the information about their home such as pollution generated and consumption of electricity <br />
**Further development ideas**<br />
- An administrator role could be created. An administrator could update the values of the model<br />
- Password reset functionality for when a user forgets their password<br />
- The assessment could be expanded, or there could be a basic and an advanced assesment<br />
- An option could be added to change username, e.g. in settings<br />
- An option could be added to export information about your home<br />
- Users could have several homes <br />

