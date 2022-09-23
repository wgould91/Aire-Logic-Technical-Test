# Aire-Logic-Technical-Test

An example API for the submission of Bug Reports and assigning them to users.
## Installation

To run this API you must first have `flask` and `flask_sqlalchemy` installed, these can be installed in the command line by running the file `install.bat`

or alternatively in the command line:
```
pip install flask

pip install flask _sqlalchemy
```

### Dependencies

- Anaconda: Version 2022.05
- Python: Version 3.9.12
- flask: Version 1.1.2
- flask_sqlalchemy: Version 2.5.1

## Launch the API

To launch the API navigate to the directory in your commande terminal and run:

`python main.py`

The resultant output should be similar to:

![](https://github.com/wgould91/Aire-Logic-Technical-Test/blob/main/Run%20main.png)

The API page should then load in your web browser with the following link:

http://127.0.0.1:5500/

## Navigation

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

Submissions must be made to both the **Bug Title** and **Bug Details** entry forms

### Bug Updater

An exisiting and *open* **Bug Title** must be included. Then you can assign a new user in the **Assign User** box (the username must already exist: see [Users](https://github.com/wgould91/Aire-Logic-Technical-Test/blob/main/README.md#users)) and/or open/close the bug report in the **Type Open or Close** box, with the keywords *Open* and *Close* respectively.

N.B. You cannot update a closed bug report, you must open the bug report to do this.

### Open bugs

Lists all open bug report titles.

Submit an open title to the **Enter Bug Title** Box to view the bug report description.

### Closed Bugs

All closed bugs are listed here for easy of finding, should they need t be reopened.

### New Users

Enter a new username into the **Enter Username** box to add the new user to the database, existing usernames cannot be added a second time.

### Update Users

To alter an existing username include a current username in the **Enter Username** box, then include the new username in the **Update user details** box.

N.B. A username cannot be updated to an already existing username.

### Users

View all current users in the system.

## Future Development

- Use of unique ID's for users and report titles. This would allow for more traceability and allw for greater user flexibility when creating, updating and naming bug reports 
