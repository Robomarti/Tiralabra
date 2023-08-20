# Set up guide:


Please use the latest release version on your reviews and issues.


You can have virtualenv installed by using pip install virtualenv. This might make easier to remove unnecessary
dependencies after testing my application.


If you are using virtualenv, first use the command 
```bash
virtualenv .env
```
to create a virtual environment.


Start the virtual environment use 
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


To start the application, use
```bash
invoke start
```

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
[Here](documentation/User%20guide.md)


## Weekly reports:
[Week 1 report](documentation/week%201%20report.md)

[Week 2 report](documentation/week%202%20report.md)

[Week 3 report](documentation/week%203%20report.md)

[Week 4 report](documentation/week%204%20report.md)

[Week 5 report](documentation/week%205%20report.md)


## Testing document:
[Here](documentation/Testing%20document.md)


## Implemetation document:
[Here](documentation/Implementation%20document.md)


## Project specification document:
[Here](documentation/Project%20specification.md)
