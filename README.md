LOL as the name suggest 

# FLIPKART REVIEW EXTRACTION API

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
