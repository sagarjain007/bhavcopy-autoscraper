# Bhavcopy auto-scraper

- Downloads the equity bhavcopy zip from BSE every day at 18:00 IST for the current date.
- Extracts and parses the CSV file in it.
- The data is stored in postgress.
- The entire application is hosted on heroku, which can be accessed from the URL given below 
- Allows users to perform search operation and optionally download the results as CSV.

## Tech

Behind the scenes of the application:

- Django framework
- Redis 
- PostgreSQL as Backend
- VueJS frontend

## Live Application

```sh
https://bhavcopy-autoscraper.herokuapp.com/
```
