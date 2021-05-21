# AgriBusiness Information System.

## Requirements
- Python 3+
- Pip

## Project Summary:
AgriBizz is a web-base technology that aims to help farmers, breeders and fishermen to get agricultural and business information and also access their crop markets through their mobile phones, tablets, Desktop computers and laptop through the web browsers. This will enable them to reach the markets and especially the buyers of their products and agricultural products without the hassle of exporting the products to the market.

![front](https://user-images.githubusercontent.com/83826268/119102353-9bc58680-ba22-11eb-8f1d-4e9be73e8e38.png)


## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env or python3 -m venv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```
Activate Virtual Enviroment Windows:

```
.\venv\scripts\activate
```

Then install the project dependencies with

```
pip install -r requirements.txt
```
Migrate the Database:
```
python manage.py migrate
```

Create SuperUser:
```
python manage.py createsuperuser
```

Now you can run the project with this command

```
python manage.py runserver
```
