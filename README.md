# ws-first
Web Services pirma užduotis

## Application:
#### App runs on port 5000.
#### To run it, write `docker-compose up`

URL = localhost:5000/api<br />

**Usage**<br />

**GET All**<br />
localhost:5000/api/movies<br />
Response: returns all movies in an array if successful<br />

**GET by movieId**<br />
localhost:5000/api/movies/<int: movieId><br />
Response: returns movie if successful<br />
Return on failure: ```404```<br />

**POST**<br />
localhost:5000/api/movies + JSON body<br />
example body:<br />
```
{
    "title": "title",
    "director": "name of director",
    "rating": movie_rating,
    "release_year" : movie_release_year
}
```
An error message will be returned on failure<br />
Status on success: ```201```<br />
Status on failure: ```400```<br />

**PUT by movieID**<br />
localhost:5000/api/movies/<int: movieId> + JSON body<br />
example body (requires at least one parameter of a movie object):<br />
```
{
    "title": "title",
    "director": "name of director",
    "rating": movie_rating,
    "release_year" : movie_release_year
}
```
Edited object will be returned upon success<br />
Otherwise an error message will be returned<br />
Status on success: ```200```<br />
Status on failure: ```400```<br />

**PATCH by movieID**<br />
localhost:5000/api/movies/<int: movieId> + JSON body<br />
example body (requires at least one parameter of a movie object):<br />
```
{
    "rating": new_movie_rating
}
```
Edited object will be returned upon success<br />
Otherwise an error message will be returned<br />
Status on success: ```200```<br />
Status on failure: ```400```<br />


**DELETE by movieID**<br />
localhost:5000/api/movies/<int: movieId><br />
Object with the corresponding id will be deleted upon success<br />
An error message will be returned on failure<br />
Status on success: ```204```<br />
Status on failure: ```404```<br />
