# Assignment

Have created a backend server which supports rendering website page variants, tracking and displaying summary<br/>
The algorithm basically calculates the % of times a page is rendered and try to normalize it with other page variant impressions.<br/>
This essentialy works like a round-robin fashion but it can be changed anytime as per the business requirement<br/>

# Files

A.html, B.html, C.html, D.html, E.html - Page Variants<br/>
server.py - Backend Server<br/>
summary.html - Displays Summary of conversions/impressions<br/>
static/util.js - JS Helper Functions<br/>

// Port 8000 <br/>
To Run : python -m server<br/>

# Exposed Urls:

 http://localhost:8000/?utm_id=2<br/>
 http://localhost:8000/?utm_id=1<br/>
 http://localhost:8000/summary <br/>
 http://localhost:8080/static/util.js<br/>
 http://localhost:8080/summaryJson<br/>
 