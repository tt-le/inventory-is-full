# 🛒 inventory-is-full

Shopify Backend Developer Intern Challenge: An inventory tracking service for a logistic company.


---
### 🐳 Docker deployment
---

The following section requires the docker compose and docker engine.
Both are included with docker destop install for **Windows** and **MacOS**.
It is available to download [here](https://docs.docker.com/desktop/).
On **Linux**, they are installed seperately.  First the engine [here](https://docs.docker.com/engine/install/#server), then 
docker compose [here](https://docs.docker.com/compose/install/).

### Running with Docker:
1. Run the following command and the API and a database container will start up.
```
docker-compose up 
```
When you see the following message the database is ready.
```
postgres     | 2022-01-15 23:03:23.547 UTC [1] LOG:  database system is ready to accept connections
```
When you see the following message the API is ready to accept requests.
```
webserver_1  |  * Serving Flask app 'api' (lazy loading)
webserver_1  |  * Environment: docker
webserver_1  |  * Debug mode: on
webserver_1  |  * Running on all addresses.
webserver_1  |    WARNING: This is a development server. Do not use it in a production deployment.
webserver_1  |  * Running on http://192.168.48.2:8080/ (Press CTRL+C to quit)
webserver_1  |  * Restarting with stat
webserver_1  |  * Debugger is active!
webserver_1  |  * Debugger PIN: 716-097-762
```

---
### 📝 Test some endpoints
---
NB: for the following section you may use postman, curl or even your favourite browser to 
make the API calls.

1. First let's try to get a product with id 1:

```
curl --request GET -i -o - 'http://localhost:8080/inventory/product/1'
```

We get a 404 status code which is normal because the database is empty.

```
HTTP/1.0 404 NOT FOUND
Content-Type: application/json
Content-Length: 65
Access-Control-Allow-Origin: *
Server: Werkzeug/2.0.2 Python/3.7.2
Date: Sun, 16 Jan 2022 00:02:54 GMT

{
  "message": "No product found with id: 1", 
  "payload": {}
}
```

2. Let's create a product:

```
curl --request POST -i -o - 'http://localhost:8080/inventory/product' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "Lay'\''s Original", "price": 0.99, "weight": 0.001, "description": "Nice crips bag of salty air!"}'
```

You'll receive the following back. The payload is describes the row that was added to the database.
Notice, that the quantity field that is set to 0. This is one of 2 optional attributes, the other being description.

```
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 211
Access-Control-Allow-Origin: *
Server: Werkzeug/2.0.2 Python/3.7.2
Date: Sun, 16 Jan 2022 00:39:43 GMT

{
  "message": "CREATE-OK", 
  "payload": {
    "description": "Nice crips bag of salty air!", 
    "id": 1, 
    "name": "Lay's Original", 
    "price": "0.99", 
    "quantity": 0, 
    "weight": "0.001"
  }
}
```

3. Great! Now we can to to fetch this object from the database.

```
curl --request GET -i -o - 'http://localhost:8080/inventory/product/1'
```

We get a 200 status code and the requested resource back under payload!

```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 204
Access-Control-Allow-Origin: *
Server: Werkzeug/2.0.2 Python/3.7.2
Date: Sun, 16 Jan 2022 00:34:39 GMT

{
  "message": "OK", 
  "payload": {
    "description": "Nice crips bag of salty air!", 
    "id": 1, 
    "name": "Lay's Original", 
    "price": "0.99", 
    "quantity": 0, 
    "weight": "0.001"
  }
}

```

4. Let's modify the quantity to 55 and the price to 1.99

```
curl --request PATCH -i -o - 'http://localhost:8080/inventory/product/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "price": 1.99, 
    "quantity": 1000
  }'
```

The payload reflects the changes.

```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 214
Access-Control-Allow-Origin: *
Server: Werkzeug/2.0.2 Python/3.7.2
Date: Sun, 16 Jan 2022 01:04:49 GMT

{
  "message": "UPDATE-OK", 
  "payload": {
    "description": "Nice crips bag of salty air!", 
    "id": 1, 
    "name": "Lay's Original", 
    "price": "1.99", 
    "quantity": 1000, 
    "weight": "0.001"
  }
}
```

5. Let's add some more product and export a csv!

```
curl --request POST 'http://localhost:8080/inventory/product' \
--header 'Content-Type: application/json' \
--data-raw '{"description": "Nice crips bag of smokey air!", "name": "Lay'\''s BBQ", "price": 1.99, "quantity": 200, "weight": 0.001}'
curl --request POST 'http://localhost:8080/inventory/product' \
--header 'Content-Type: application/json' \
--data-raw '{"description": "Nice crips bag of tomatoee air!", "name": "Lay'\''s Ketchup", "price": 1.99, "quantity": 100, "weight": 0.001}'
curl --request POST 'http://localhost:8080/inventory/product' \
--header 'Content-Type: application/json' \
--data-raw '{"description": "Nice crips bag of spicy air!", "name": "Lay'\''s Jalapeno", "price": 1.99, "quantity": 100, "weight": 0.001}'
```

6. Export the csv with the following curl; or just visit the url on a browser!

```
curl --request GET 'http://localhost:8080/inventory/product/export' 
```

```
id,name,price,weight,quantity,description
1,Lay's Original,1.99,0.001,1000,Nice crips bag of salty air!
3,Lay's BBQ,1.99,0.001,200,Nice crips bag of smokey air!
4,Lay's Ketchup,1.99,0.001,100,Nice crips bag of tomatoee air!
5,Lay's Jalapeno,1.99,0.001,100,Nice crips bag of spicy air!
```
