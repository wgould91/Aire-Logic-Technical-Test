# Aire-Logic-Technical-Test

An example API for the submission of Bug Reports and assigning them to users.
### Installation

To run this API you must first have `flask` and `flask_sqlalchemy` installed, these can be installed in the command line by running the file `install.bat`

or alternatively in the command line:
```
pip install flask

pip install flask _sqlalchemy
```

### Launch the API

To launch the API navigate to the directory in your commande terminal and run:

`python main.py`

The resultant output should be similar to:

![]()

The API page should then load in your web browser with the following link:

http://127.0.0.1:5500/

### Navigation

All functions can be made via the Toolbar at the Top of the API

![](https://github.com/wgould91/Aire-Logic-Technical-Test/blob/main/Nav%20Bar.png)

- Home - The Home Page
- Bug Reporter - Submit a new bug report and assign it to a user (optional)
- Bug Updater - Assign the bug a new user and open/close the bug report
- Open Bugs - See the list of open bug reports and investigate the details of specific open reports
- Closed Bugs - See a list of closed bug titles
- New Users - Submit a new username
- Update Users - Alter the username of an existing user
- Users - See the list of available users registered to the system

### Bug reporter

Submissions must be made to both the **Bug Title** and **Bug Details** Entry forms
