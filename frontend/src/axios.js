import axios from "axios";

/*
cookies will be sent with each request made using Axios, 
and cookies received in the response will be stored. 
This is useful when you're making 
requests that require authentication, 
and the authentication data is stored in cookies.
*/
axios.defaults.withCredentials = true;
// axios.defaults.baseURL = 'http://localhost:8000'