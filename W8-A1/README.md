### cocoon.py
* This file uses the Factory Design Pattern.
* The getButterfly() method decides which object to create.
* If y is not zero, it creates a TrigButterfly.
* If y is zero, it creates an AddButterfly.
* The program does not need to know which butterfly class is used.

### name-ui.py
* This file uses the Factory Design Pattern to process names entered by the user.
* NamerFactory decides how to split the name.
* If the name contains a comma, it creates a LastFirst object.
* If there is no comma, it creates a FirstFirst object.
* The user interface only works with the Namer base class.
* This keeps the UI code simple and independent of name formats.

### namer-console.py
* This file shows the same Factory pattern used to process names entered through console.
* NamerFactory creates the correct Namer object based on input.
* The Builder class does not know which class is created.
* The program prints first and last names using the returned object.
* This shows how the Factory pattern can be reused in different programs.