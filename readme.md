# Descriptions
Simple quiz web application using optional answers. You can see your score after the quiz end.

# Author
Rakka Alhazimi, October 2022

# Requirements
- python3.8 or later

# Installations
1. Clone this repository
   ```
   git clone https://github.com/rakkaalhazimi/Quiz-Prototype-Website
   ```

2. Move to cloned directory
   ```
   cd Quiz-Prototype-Website
   ```

3. Install all required library
   ```
   pip install -r requirements.txt
   ```

4. Make database migrations
   ```
    python manage.py makemigrations quiz
   ```
   We are doing this to see what django need to build the database table

5. Migrate databse
   ```
    python manage.py migrate
   ```
   Once we make the migrations, we can then migrate to create the database and its tables

6. Start server
   ```
    python manage.py runserver
   ```

# Optional
Create new superuser to manage all lesser user
```
python manage.py createsuperuser
```

Create another app
```
django-admin startapp [app name]
```