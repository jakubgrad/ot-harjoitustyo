# House app
The goal of the project is to create an app in which users can log in or register and receive their homes' energy consumption and pollution estimates based on filled out assessments. The application was developed using `Python 3.11` and using `Poetry` as a dependency manager<br/>


## Documentation
[Changelog](https://github.com/jakubgrad/ot-harjoitustyo/blob/main/documentation/changelog.md)<br/>
[Architecture](https://github.com/jakubgrad/ot-harjoitustyo/blob/main/documentation/architecture.md)<br/>
[Specification document](https://github.com/jakubgrad/ot-harjoitustyo/blob/main/documentation/specification%20document.md)<br/>
[Time Keeping](https://github.com/jakubgrad/ot-harjoitustyo/blob/main/documentation/time_keeping.md)<br/>


## Using the application 
Clone the repository and enter topmost directory:<br/>
```
git clone https://github.com/jakubgrad/ot-harjoitustyo.git
cd ot-harjoitustyo
```
Then you want to install poetry: 
```
poetry install --no-root
```
in the command line opened inside the topmost project directory. If you don't have poetry installed and use a university computer, you'll likely be prompted if you want to install it. In that case, press <y> and <enter>. Then quit the terminal and open it in the same place so that the shell recognizes newly installed poetry <br/>
Then, to initializa the database run:
```
poetry run invoke init`
```
According to course materials:<br/> <br/>
"NOTE: If you are running an application using a SQLite database in a virtual desktop, 
you may encounter the error `database is locked`. [This guide](https://ohjelmistotekniikka-hy.github.io/python/toteutus#sqlite-tietokanta-lukkiutuminen-virtuaality%C3%B6asemalla) will probably solve the problem"<br /><br/>

The project can be started by running (preferably in the topmost directory of the project): 
```
poetry run invoke start
```
You can test the project with: 
```
poetry run invoke test
```
The coverage report can be created and viewed in HTML: 
```
poetry run invoke coverage-report
```
You can see linting errors of the project with: 
```
poetry run invoke lint
```
If you get an error similar to this one:
```
[13289:13289:0403/183659.749216:ERROR:process_singleton_posix.cc(353)] The profile appears to be in use by
 another Google Chrome process (44970) on another computer (vdi-cubic-025.ad.helsinki.fi).
Chrome has locked the profile so that it doesn't get corrupted.
If you are sure no other processes are using this profile,
you can unlock the profile and relaunch Chrome.
```
You can run  `rm -rf ~/.config/google-chrome/Singleton*` and then try to generate the report again. It should open in your browser. If it doesn't, there is still the possibility of opening it with a browser application directly from the file in html-cov in the topmost directory of the project.<br/>
Note: in principle the above `poetry` commands can be run in any project directory thanks to using absolute path of the project in `tasks.py`, but the app was only tested by running commands in the topmost directory<br/>

**[Ylimääräinen koodikatselmointi = Additional code review](https://github.com/nuuttikuosa/ohjelmistotekniikka2024)**

