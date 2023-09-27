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
    ENGINE=django.db.backends.sqlite3
    NAME=db.sqlite3

3. Start the project using Docker Compose:

    ```
    docker-compose up --build

4. After a successful launch, your application will be accessible at 😇

    ```
    http://localhost:8000/

## Admin Panel 📑

Administrators have access to the Django admin panel where they can create custom access tiers with configurable parameters such as thumbnail sizes, the presence of links to the original file, and the ability to generate expiration links.


1. Create superuser for admin panel.

    ```
    1) Open the terminal of the Docker container
    2) Make sure that you are in correct directory where manage.py file.
    3) Use command: python manage.py createsuperuser
    4) Enter: name, email, password, password(second time)
    5) Successfully you may enter to the adminstration panel: http://localhost:8000/admin/


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

For a detailed description of the API endpoints and data models, you can refer to the [schema.yaml](schema.yaml) file in this repository. Below is a link to summary of the API paths:

```
[SWAGGER](#https://app.swaggerhub.com/apis/GASIME101AEHIT/ImageTierApi/1.0.0)
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

### **Author 👨‍💻**

- Eltun Gasimov 
- https://github.com/gasimovv21
- https://www.linkedin.com/in/eltun-gasimov-3b8b65256/