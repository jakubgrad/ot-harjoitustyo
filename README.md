# Ohjelmistotekniikka, harjoitustyö <br />
**Software development, practice work**. A repository for practice work related to the course *[Ohjelmistotekniikka](https://ohjelmistotekniikka-hy.github.io/)* at *[University of Helsinki](https://studies.helsinki.fi/kurssit/opintojakso/otm-fc35db8b-596c-4287-a03c-047e81e1254b)*. 

[💻 Calculators = laskarit](https://github.com/jakubgrad/ot-harjoitustyo/tree/main/laskarit) folder: https://github.com/jakubgrad/ot-harjoitustyo/tree/main/laskarit

[📎 Specification / requierements / marittely / vaatimus document](https://github.com/jakubgrad/ot-harjoitustyo/blob/main/documentation/specification%20document.md).

[🕐 Time keeping =  työaikakirjanpito](https://github.com/jakubgrad/ot-harjoitustyo/blob/main/documentation/time_keeping.md)

The goal of the project is to create an app in which users can log in or register and receive their homes' energy consumption and pollution estimates based on filled out assessments.<br/>
Python 3.11 was used to develop and test the application.<br/>

## Documentation


## Installation 
Run `poetry install`<br/>
The project doesn't yet have a database and instead relies on hardwired user "m" with passsword "m". <br/>
The project can be started with: `poetry run invoke start`<br/>
The project can be tested with: `poetry run invoke test`<br/>
The coverage report can be created and viewed in HTML: `poetry run invoke coverage-report`<br/>
These commands can now be run in any project directory thanks to using absolute path of the project in tasks.py<br/>


