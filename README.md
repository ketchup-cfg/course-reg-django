# course-reg-django

This is a full stack web application created with Django, that can be used as a tool to register for courses.

## Installing Dependencies

Before setting up the dependencies for the application, first make sure to create a virtual environment and activate it:

```shell
python3 -m venv venv
source venv/bin/activate
```

After that has been done, you can install the dependencies for the application by running the following from the command line:

```shell
pip install --upgrade pip && pip install -r requirements.txt
```

## Running the Application

To run the application, run the following from the command line:

```shell
cd coursereg
python3 manage.py migrate && python3 manage.py runserver
```
