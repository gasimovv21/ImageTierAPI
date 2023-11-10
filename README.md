# ImageTierApi 📷

ImageTierApi is a RESTful API for uploading and managing images in PNG and JPG formats with different access levels. This application is developed using Django REST Framework and provides a convenient way for users to upload, manage, and access their images.

## Set up the project 🔋

To set up the project, you'll need Docker and Docker Compose. Follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/your/repository.git
   cd ImageTierApi

2. Create a .env file near with docker-compose.yml file and specify the following environment variables for the database:
    
    ```
    SECRET_KEY=django-insecure-hc^-dz#z2=ilnsh&v^(2^ddt3oc@@!#v8b5(9!)!f5ml9@(+fo
    DEBUG=True
    NAME=mydb
    USER=myuser
    PASSWORD=mypassword
    HOST=db
    PORT=5432

3. Open the terminal in project directory and start the project using Docker Compose command:

    ```
    docker-compose up --build

4. Open one more terminal in project directory, for creating and using migration.
    ```
    1) docker-compose exec web python manage.py makemigrations
    2) docker-compose exec web python manage.py migrate

5. After a successful launch, your application will be accessible at 😇

    ```
    http://localhost:8000/

## Admin Panel 📑

Administrators have access to the Django admin panel and pgAdmin4 where they can create custom access tiers with configurable parameters such as thumbnail sizes, the presence of links to the original file, and the ability to generate expiration links.


1. Create superuser for django-admin panel.

    ```
    1) Open the terminal in project directory
    2) Use command: docker-compose exec web python manage.py createsuperuser
    3) Enter: name, email, password, password(second time)
    4) Successfully you may enter to the adminstration panel: http://localhost:8000/admin/

2. Entering to pgAdmin4.

    ```
    1) Go to: http://localhost:5050/
    2) Log in with the email and password specified in the PGADMIN_DEFAULT_EMAIL and PGADMIN_DEFAULT_PASSWORD environment variables in your docker-compose.yml file.
    4) Successfully you may enter to the pgAdmin4 panel.

3. Connecting to the postgreSQL databse of project.
    
    ```
    1) In the pgAdmin interface, click on "Add New Server" (usually a plus icon or an "Add New Server" option in the menu).
    2) In the "General" tab, provide a name for your server in the "Name" field.
    3) Switch to the "Connection" tab.
    4) In the "Host name/address" field, enter the name of the PostgreSQL service in your Docker Compose setup. In your case, it's likely "db."
    5) In the "Port" field, enter the PostgreSQL port, which is 5432 by default.
    6) In the "Maintenance database" field, enter the name of your PostgreSQL database. In your case, it's "mydb."
    7) In the "Username" and "Password" fields, enter the PostgreSQL username and password. In your case, they are "myuser" and "mypassword."
    8) Click "Save" to save the connection details.
    9) In the pgAdmin interface, you should now see your server listed in the left sidebar. Click on it to expand the tree and see the databases, schemas, and other objects.
    10) You can now browse and manage your PostgreSQL database using pgAdmin.


## The API provides the following features 🎇

Image Upload:

To upload an image, make a POST request to /api/upload/. In the request, provide parameters such as the username (username), access tier (tier), image file (image), and expiration link duration (expire_link_duration).

1) Fetching the List of Images:

```
To get a list of all images, make a GET request to /api/images/.
```
2) Fetching User Images:

```
To get images of a specific user, make a GET request to /api/images/{username}/, where {username} is the username.
```
3) Fetching an Image via Expiring Link:

```
To get an image via an expiring link, make a GET request to /api/expire-links/{expire_link_token}/, where {expire_link_token} is the token for the expiration link.
```

## OpenAPI Specification ⚡

For a detailed description of the API endpoints and data models, you can refer to the [schema.yaml](https://app.swaggerhub.com/apis/GASIME101AEHIT/ImageTierApi/1.0.0) file in this repository. Below is a link to summary of the API paths:

```
https://app.swaggerhub.com/apis/GASIME101AEHIT/ImageTierApi/1.0.0
```

## Testing 📊
The project includes tests to ensure functionality. You can run them using the following command:

```
python manage.py test
```

## Technologies used during development ⚙

- Python
- Django
- DRF
- REST API
- PostgreSQL
- Docker and docker compose
- pgAdmin 4

### **Author 👨‍💻**

- Eltun Gasimov 
- https://github.com/gasimovv21
- https://www.linkedin.com/in/eltun-gasimov-3b8b65256/