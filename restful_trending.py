import requests
from bs4 import BeautifulSoup
from flask import Flask,jsonify,request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return jsonify(Products=scrape('',25))

def scrape(filter,num): # This function performs the scraping of https://github.com/trending

    l = [] # List containing all the useful information of the website

    # Access the trending github page
    req = requests.get('https://github.com/trending')
    soup = BeautifulSoup(req.text, "html.parser")

    # Access each item of the page
    all_items = soup.find_all('li', class_="col-12 d-block width-full py-4 border-bottom")
    i=0

    for item in all_items:

        d={}

        # Getting the name information:
        name=item.find("a").getText().replace(" ", "").replace("\n", "")

        if (filter in name)&(i<num):
            d['Name']=name

            # We need to access to the web page of each projects in order to get the number of views:
            req2 = requests.get('https://github.com/'+name)
            soup2 = BeautifulSoup(req2.text, "html.parser")

            # Getting the number of views:
            views =soup2.find("a",{"class":"social-count"}).getText().replace(" ", "").replace("\n", "")
            d['Views']=views

            # Getting the number of stars:
            stars=soup2.find("a",{"class":"social-count js-social-count"}).getText().replace(" ", "").replace("\n", "")
            d['Stars']=stars

            l.append(d) # Stores all information inside a list
            i+=1

    return l





class search(Resource):
    def get(self):
        # items=scrape()
        filter = request.args.get('filter',default='',type=str) # Filtered search
        num = request.args.get('num',default=25,type=int) # Selects the number of repositories available
        l_filter=scrape(filter,num) # List containing the filtered items

        return l_filter,200


api.add_resource(search,'/search')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
