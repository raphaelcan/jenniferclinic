1. Create a python venv :
`python3 -m venv venvv`
2. Activate the venv :
`source venv/bin/activate`
   
3. If pip is not installed, make sure to install it first :
details here https://pip.pypa.io/en/stable/installing/
   
4. Install requirements :
`pip3 install -r requirements.txt`
   
5. launch migration :
`python3 manage.py migrate`
   
6. insert your zoom api token line 122 of the file settings.py

7. launch the django server :
`python3 manage.py runserver`
   
8. Access the app on the url `http://localhost:8000`