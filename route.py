import pymongo
import mars_scrape
from flask import Flask
from pymongo import MongoClient

app= Flask(_name_)



# Create connection variable
conn = 'mongodb://localhost:27017'
hw_db= 'mars_db'
hw_cl= 'mars_data'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client[mars_db]
cl = db[mars_data]

mars_data= list(db[mars_data.find()])

print(mars_data)
#create route for html
@app.route('/')
def index():
    return mars_data, 'index.html'

#scarep route

@app.route('/scrape')
def scrape():
    mars_date= scape_mars.scrape()
    db.mars_data.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect('http://localhost:5000/', code=302)

    if __name__== '__main__':
        app.rin(debig=True)

