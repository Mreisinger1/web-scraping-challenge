# import necessary libraries
from flask import Flask, render_template
import pymongo

# create instance of Flask app
app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_data


@app.route("/")
def index():
    mars_data = mongo.db.mars_data.find_one()
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():
    mars_data = mongo.db.mars_data
    mars_info = scrape_mars.scrape()
    mars_data.update({},mars_info, upsert = True)
    return redirect("/", code=302)


print("data uploaded")



if __name__ == "__main__":
    app.run(debug=True)