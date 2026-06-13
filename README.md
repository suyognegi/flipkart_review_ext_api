

# FLIPKART REVIEW EXTRACTION API


## WHAT DOES IT DO ?

  LOL as the name suggest 

  
  IT extract reviews from the provied url of flipkart product

  
  NOTE : Later user pydentic 

  
  ### INPUTs :-

- `url` (necessary)

- `const_alpha` (optional)

- `limit` (optional)

 >adjust the const_alpha variablee low means less reviews hence faster
>
 >high the value more the reviews hence slower (advixe keep it max to 12 (have successfully extracted 1576 total reviewed reviews of a sinple product with speed 13/sec) )
>
 >for best/avg results keep it to 6
>
 >personally note havig limit is good (fast) and gnerally generates result 2.8x*limit ~ 4*limit



---
`OUTPUT SCHEMA : `
```json
{
  "success": true,
  "data": [
    { 
      "MOST_HELPFUL": [ReviewObject], 
      "count": 50 
    },
    { 
      "MOST_RECENT": [ReviewObject], 
      "count": 50 
    },
    { 
      "POSITIVE_FIRST": [ReviewObject], 
      "count": 100 
    },
    { 
      "NEGATIVE_FIRST": [ReviewObject], 
      "count": 100 
    }
  ],
  "total_count": 300,
  "response_time_ms": 18,
  "speed": "16.6 rev/sec"
}
```

`ReviewObject`
```
{
  "rating": "5.0",
  "head_review": "string",
  "review_for": "string",
  "text_review": "string",
  "name": "string",
  "city": "string",
  "helpful": "string",
  "not_helpful": "string",
  "ago": "string",
  "media": ["url1", "url2"]
}
```

`Eg :-`
```
    {
      "rating": "5.0",
      "head_review": "Terrific",
      "review_for": "Review for: Quantity 56x9.6 g",
      "text_review": "Nice one..",
      "name": "Dr. ABDUL SAMAD P",
      "city": " Kannur",
      "helpful": "5",
      "not_helpful": "0",
      "ago": "Jun, 2021",
      "media": [
        "https://rukminim2.flixcart.com/blobio/376/376/imr-202106/blobio-imr-202106_a4f89eaad1d34eabb1ce22f818a0b74e.jpg?q=90",
        "https://rukminim2.flixcart.com/blobio/376/376/imr-202106/blobio-imr-202106_3f513c8da55a42bb8dcf481b5c4ada1b.jpg?q=90",
        "https://rukminim2.flixcart.com/blobio/376/376/imr-202106/blobio-imr-202106_69206a3109ea47f093730912107f64bc.jpg?q=90"
      ]
    }
```
---



## HOW TO RUN

download keep your main.py file someone and note its location
in your local of **PyCham venv** run

```bash
pip install fastapi uvicorn playwright && playwright install chromium

```
or 
```bash
pip install -r requirements.txt
```
and then run 

```bash
uvicorn main:app
```


