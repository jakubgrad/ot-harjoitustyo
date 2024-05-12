# Manual = käyttöohje
## User interaction
To install, follow the instructions in the README.md. After launching, the following screen should appear, either colored or uncolored:
<p align="center">
    <img src="https://github.com/jakubgrad/ot-harjoitustyo/assets/113715885/7db8409b-1339-41e6-bfb5-02263dddb338" width="25%" alt="Description of the image">
</p>
There is no users yet in the database, so you need to click on `Register` and choose username and password. There is no restrictions on the username and password apart from that the username cannot already be taken. After registration, the user is presented with `Assessment` view, which makes it possible to put in information about your home on the basis of which the energy consumption and pollution can be calculated. In the form, `age` of the house means year of construction, e.g. 1991. <br><br>
<p align="center">
    <img src="https://github.com/jakubgrad/ot-harjoitustyo/assets/113715885/b3cbfb55-0f78-40fa-b9fa-626e2a8a7f68" width="25%" alt="Description of the image">
</p><br>
After clicking on `Update` the user is taken to `House` view with a centered picture of a house and information on energy consumption and pollution. The values aren't accurate yet and don't take full advantage of the energy model. However, once they do, the energy and pollution wil be expressed in reasonable values (e.g. KW and kg). <br><br>
<p align="center">
    <img src="https://github.com/jakubgrad/ot-harjoitustyo/assets/113715885/b6b43d99-3f7b-4528-8e19-f2b27493ae1f" width="25%" alt="Description of the image">
</p> <br>
It's always possible to change the information about the house by clicking on "Create/update assessment" and putting in different values. The app rememberes users who put in information about their homes, so that after filling out the assessment and logging in again, the user is presented with the `House` view again. <br>

## Admin interaction
The admin interaction is a bit different. The goal is initially have an admin who can create other admins with their usernames and passwords. The first admin is by default one with username "m" and password "m". So to try the functionality of admin put "m" as username and as password and click "Login as administrator". <br><br>
<p align="center">
    <img src="https://github.com/jakubgrad/ot-harjoitustyo/assets/113715885/5ffef448-64d4-445c-8a32-239b2cb84c52" width="25%" alt="Description of the image">
</p><br>
You'll get `Administration` view, which currently allows you to put e.g. new named types of heating and how much pollution and electricity they produce relative to the existing methods. You can also update the pollution and electricity that depends on house age using a similar form. <br><br>
<p align="center">
    <img src="https://github.com/jakubgrad/ot-harjoitustyo/assets/113715885/2234548c-cd32-4408-9108-31f8c46c71b2" width="50%" alt="Description of the image">
</p>
The forms support replacing the values of pollution, electricity consumption, and name of the existing types of heating and construction year / house age. For changing the parameters of house age, simply put in the form the same `Min year` (the lower bound of the construction year) and the new data will replace the existing row in the database. For types of heating, put in the same `type` number and the new values will replace the existing ones for the same type of heating. <br>


<p align="center">
    <img src="https://github.com/jakubgrad/ot-harjoitustyo/assets/113715885/07501204-7c86-4c6c-9816-63f5b4200cdc" width="50%" alt="Description of the image">
</p>

It's also possible to create a new administrator so that other administrators apart from the default one exist! After logging in as administrator, simply put in the username and password of the new administrator
<p align="center">
    <img src="https://github.com/jakubgrad/ot-harjoitustyo/assets/113715885/98d89978-eed4-4b97-905f-b5ee6700a42b" width="50%" alt="Description of the image">
</p>

**Note!** When you update the values of some type of heating or a range of ages, remember that to see the changes you likely need to log out and log in as administrator again.
