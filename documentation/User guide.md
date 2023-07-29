#Set up guide:

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

To change the configuration of the application use the command
```bash
invoke config 
```
You can change the configurations by adding one or more of the following lines to the end of the command.
```bash
--length integer_Here
```
This will be the length of the generated cave, measured in cells. Input a positive integer.


```bash
--width integer_Here
```
This will be the width of the generated cave, measured in cells. Input a positive integer.


```bash
--floor float_here
```
This will be the chance that a cell will be initally a floor tile. Input a positive floating point number between 1 and 0.


So for example, to restore the original configurations, use the command

```bash
invoke config --length 20 --width 20 --floor 0.4
```


To test the app use the command 
```bash
invoke test
```


To get the coverage report use the command
```bash
invoke coverage-report
```
The command also executes all the tests required. The report will be generated to the directory htmlcov 