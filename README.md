# Set up guide:

You can have virtualenv installed by using pip install virtualenv. This might make easier to remove unnecessary
dependencies after testing my application.

Start the application with 
```bash
source venv/Scripts/activate
```
or
```bash
source venv/bin/activate
```

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
The command also executes all the tests required. The report will be generated to the directory htmlcov 


## User guide:
[Week 1 report](documentation/User%20guide.md)


## Weekly reports:
[Week 1 report](documentation/week%201%20report.md)
[Week 2 report](documentation/week%202%20report.md)