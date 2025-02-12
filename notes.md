@What are path parameters?
1. path parameters are request parameters that have been attached
to the URL.

2. path parameters are usually defines as the way to find information
based on location.

@What are query parameters?
1. Query parameters are requests parameters that have been attached 
after a question mark.
2. Query parameters have a name:value pairs relationship.

@What is POST request method
ans: Used to create data, POST can have a body that has additional information
that GET method does not have.

@What is a PUT request method
ans: Is used to update data, PUT can have a body that has additional information
(like POST) that GET does not have.

@What is the DELETE request method
ans: Is used to delete data,   

CRUD Methods => Create(POST), Read(GET), Update(PUT), DELETE(DELETE)

@What is pydantics?
1. Pydantics is a python library that is used for data modeling, data parsing
and has efficient errors handling.

2. Pydantics is commonly used as a resource for data validation and how
to handle data coming to our FastAPI application.

@What is Status Code?
ans: An HTTP Status Code is used to help the Client(the user or system
submitting data to the server) to understand what happened on the server
side application. 

Status Code are international standards on how a Client/Server should
handle a result of a request.

It allows anyone who send a request to know if their submission was 
successful or not.
1. 1xx -> Information Response: Request Processing
2. 2xx -> Success: Request Successfully complete
3. 3xx -> Redirection: Futher action must be complete
4. 4xx -> Client Errors: An error was caused by a client
5. 5xx -> Server Errors: An error occurred on the server.

@2xx Successful Status Code
# 200: OK -> Standard Response for a successful request. 
commonly used for successful GET request when data is 
being returned.

# 201: Created -> The request had been successfully, creating a new
resource. Used when a POST creates an entity.

# 204: No Content-> The request had been successful, did not create an
entity nor return anything. Commonly used with PUT requests.
---------------------------------------------------------------

@4xx Client Errors Status Codes:
# 400: Bad Request -> Cannot process request due to client error.
Commonly used for invalid request methods.

# 401: Unauthorized -> The request had been successfully, creating a new
resource. Used when a POST creates an entity.

# 404: Not Found -> The clients requested resource can not be found.

# 422: Unprocessable Entity -> Semantics Errors in Client Requests.

---------------------------------------------------------------

@5xx Server Errors Status Codes:
# 500: Internal Server Error -> Generics Error Message, when an expected
issue on the server happened. 



