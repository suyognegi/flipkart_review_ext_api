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
