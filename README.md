# CYE_home_exercise
implemented API proxy server that receive HTTP REST API requests and  
forward them to a remote REST API that supports the same API endpoints.
<br/>
API REMOTE SERVER = 'https://reqres.in/'
<br/>

The proxy server would send a response to the client (same response as the remote server sent) while limiting the requests rate:
<br/>
* A maximum of 10 requests per minute.
* A maximum of 1,000 requests per day.

 The proxy uses caching and return valid responses from the past 10 minutes.


## RUN THE PROXY_SERVER 
You need to download pipenv in order to create virtualenv and install all the packages from pipfile
or download from the requirements.txt file
<br/>
 * `python server.py`
The proxy run in [http://localhost:8000]
In order to see the REST API documentation run: [http://localhost:8000/docs]

