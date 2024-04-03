# House app
The goal of the project is to create an app in which users can log in or register and receive their homes' energy consumption and pollution estimates based on filled out assessments. The application was developed using Python 3.11 and using Poetry as a dependency manager<br/>


## Documentation
[Changelog](https://github.com/jakubgrad/ot-harjoitustyo/blob/main/documentation/changelog.md)<br/>
[Architecture](https://github.com/jakubgrad/ot-harjoitustyo/blob/main/documentation/architecture.md)<br/>
[Specification document](https://github.com/jakubgrad/ot-harjoitustyo/blob/main/documentation/specification%20document.md)<br/>
[Time Keeping](https://github.com/jakubgrad/ot-harjoitustyo/blob/main/documentation/time_keeping.md)<br/>


## Using the application 
Run `poetry install --no-root` in the command line opened inside the topmost project directory. If you don't have poetry install and use a university computer, you'll likely be prompted if you want to install it. In that case, press <y> and <enter>. Then quit the terminal and open it in the same place. <br/>
Then run `poetry run invoke init` to initialize the database<br/> 
The project doesn't yet have a database and instead relies on hardwired user "m" with passsword "m". <br/>
The project can be started with: `poetry run invoke start`<br/>
The project can be tested with: `poetry run invoke test`<br/>
The coverage report can be created and viewed in HTML: `poetry run invoke coverage-report`<br/>
These commands can now be run in any project directory thanks to using absolute path of the project in tasks.py<br/>


