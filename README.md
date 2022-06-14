This is a rest api for renting and selling houses
<h1 >
Installition
</h1>
1-SETTING UP THE PROJECT:
after downloading the .rar file extract it wherever you want then open this folder with ur editor
2-SETTING UP THE DATABASE:
after creating a new MySQL database
go to Agence/settings
then go to DATABASES
and change the USER to the username of SQL and the PASSWORD to the password of MYSQL and the name to the name of the database you created
3-INSTALLING DJANGO AND THE REQUIRED FRAMEWORKS:
check if you already installed python then install Django and these frameworks
python -m pip install Django
python -m pip install Djoser
pip install -U djangorestframework_simplejwt
pip install django-filter
pip install drf-nested-routers
pip install djangorestframework
pip install Pillow
4-MIGRITIONS
in the terminal of the project type "python manage.py makemigrations"then "python manage.py migrate"
5-RUN THE SERVER:
in the terminal of the project type "python manage.py runserver"
then you should access the server by this URL 
http://127.0.0.1:8000/




<h1 >
Paths
</h1>

URL  | METHODE | ..
------------- | ------------- | -------------
/API/products/  | GET,POST | get all products
/API/products/{product_id}/  | GET, PUT, PATCH, DELETE | get the product with the id {product_id} 
/API/products/{product_id}/reviews/ | GET, PUT, PATCH, DELETE | get all the reviews of the product with the id {product_id}
/API/products/{product_id}/{review_id} | GET, PUT, PATCH, DELETE | get the review with {review_id} of the product with the id {product_id}
/auth/users/me/ | GET, PUT, PATCH, DELETE | get the information of the user who logged in
/auth/jwt/create/ | POST | loggin in
