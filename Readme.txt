
This code creates a RESTful API with one endpoint that fetches the list of trending open source repositories from github (https://github.com/trending) and sums up:
- The name of the project
- Its number of views
- Its number of stars

The API client can also provide a search term for filtering and a size parameter to limit the amount of analyzed repositories.

This exercise was coded using Flask, Flask_restful and BeautifulSoup on Python.

Once the code is running, visiting http://0.0.0.0:5000/ will display all the available items. 

The filtered search can be performed using the following URL:
http://0.0.0.0:5000/search?filter=filter_term&num=number_of_repositories
where filter_term is the term used for filtering and number_of_repositories refers to the maximum number of repositories available on the screen.
In case only one/none of the terms are specified, the default values are filter_term='' and number_of_repositories=25.