# CYE_home_exercise
implemented API proxy server that receive HTTP REST API requests and  
forward them to a remote REST API that supports the same API endpoints.
<br/>
API REMOTE SERVER = 'https://reqres.in/'
<br/>

The proxy server would send a response to the client (same response as the remote server sent) while limiting the requests rate:
<br/>
* A maximum of 10 requests per minute.
<br/>
* A maximum of 1,000 requests per day.


