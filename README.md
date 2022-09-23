# Aire-Logic-Technical-Test

An example API for the submission of Bug Reports and assigning them to users.
### Installation

To run this API you must first have `flask` and `flask_sqlalchemy` installed, these can be installed in the command line by running the file `install.bat`

or alternatively in the command line:
```
pip install flask

pip install flask _sqlalchemy
```
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
