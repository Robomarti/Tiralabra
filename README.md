#Set up guide:

you can have virtualenv installed by using pip install virtualenv

Start the application with source venv/Scripts/activate  or source venv/bin/activate

inside virtualenv or normally use 
```bash
pip install -r requirements.txt
```
 to install dependencies


#Other commands:

To test the app use the command 
```bash
invoke test
```

To get the coverage report use the command
```bash
invoke coverage-report
```
. The command also executes all the tests required. The report will be generated to the directory htmlcov 


Weekly reports:
[Week 1 report](documentation/week%201%20report.md)