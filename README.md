# Assignment

Have created a backend server which supports rendering website page variants, tracking and displaying summary
The algorithm basically calculates the % of times a page is rendered and try to normalize it with other page variant impressions.
This essentialy works like a round-robin fashion but it can be changed anytime as per the business requirement

# Files

A.html, B.html, C.html, D.html, E.html - Page Variants
server.py - Backend Server
summary.html - Displays Summary of conversions/impressions
static/util.js - JS Helper Functions

// Port 8000 
To Run : python -m server

Exposed URLs:

 http://localhost:8000/?utm_id=2
 http://localhost:8000/?utm_id=1
 http://localhost:8000/summary 
 http://localhost:8080/static/util.js
 http://localhost:8080/summaryJson
 