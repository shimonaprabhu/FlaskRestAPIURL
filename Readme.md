Firstly, the index page was developed as the home page to accept the URL input by the user, 
so that the file served by the same can be downloaded. 

Next, the URL is used to download the file in chunks. In iter_content(), there is no chunk_size
mentioned. However, for large files, this parameter needs to be altered in order to prevent
the user from getting overwhelming data and also prevent lag. 

The chunk size downloaded is stored in a variable and the leftover size is calculated. 

This is then sent as parameters in render_template() in order to display the data in the front end. 

There are certain features that could not be implemented due to constraint of time. 

The next iteration would be to make the API asynchronous using SocketIO or JQuery in order to 
display the download details in real time, which would make other enhancements to the API possible. 
