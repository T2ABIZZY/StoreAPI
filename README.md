This is a rest api for renting and selling houses
<h1 >
Installition
</h1>


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
