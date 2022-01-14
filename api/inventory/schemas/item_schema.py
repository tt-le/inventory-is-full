create_item = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/product.schema.json",
    "title":"Item",
    "description":"An item create request json",
    "type":"object",
    "properties":{
       "id":{
          "description":"The unique identifier for a product",
          "type":"integer"
       },
       "name":{
          "description":"Name of the product",
          "type":"string"
       },
       "description":{
        "description":"Brief description of the product",
          "type":"string"
       },
       "weight":{
        "description":"Weight per unit of product",
        "type":"number",
        "exclusiveMinimum": 0
       },
       "price":{
        "description":"Price per unit of product",
        "type":"number",
        "exclusiveMinimum": 0
       }
    },
    "required":[
       "id",
       "name",
       "weight",
       "price"
    ]
 }

update_item = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/product.schema.json",
    "title":"Item Update",
    "description":"An item update request json",
    "type":"object",
    "properties":{
       "id":{
          "description":"The unique identifier for a product",
          "type":"integer"
       },
       "name":{
          "description":"Name of the product",
          "type":"string"
       },
       "description":{
        "description":"Brief description of the product",
          "type":"string"
       },
       "weight":{
        "description":"Weight per unit of product",
        "type":"number",
        "exclusiveMinimum": 0
       },
       "price":{
        "description":"Price per unit of product",
        "type":"number",
        "exclusiveMinimum": 0
       }
    },
    "minProperties": 2,
    "required": ["id"]
 }