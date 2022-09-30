# Dependencies
import requests
import os
from bs4 import BeautifulSoup 

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape(): # NASA URL

    url = 'https://redplanetscience.com/'

    # Retrieve page with the requests module
    html = requests.get(url)
     # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html.text, 'html.parser')
    # Extract title text
    title = soup.title.text
    print(title)
    
    # Print all paragraph texts
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
   
   
        def scrape(): #JPL Mars space images

            url = 'https://spaceimages-mars.com/'
          
    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    img = [i.get("src") for i in soup.find_all("img", class_="headerimage fade-in")]
    img[0]

    featured_image_url = url + img[0]
    featured_image_url
   
def scrape(): Mars facts
    
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df
    
html_table = df.to_html()
html_table
    


url = 'https://marshemispheres.com/'
browser.visit(url)


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

hemisphere_names = []

    # Search for the names of all four hemispheres
results = soup.find_all('div', class_="collapsible results")
hemispheres = results[0].find_all('h3')

    # Get text and store in list
for name in hemispheres:
hemisphere_names.append(name.text)

   
    

    #find the hemisphere photos
photo_results = results[0].find_all('a')
photo_links = []

for photo in photo_results:
    
    if (photo.img):
        
        #attached link for each photo
        photo_url = 'https://marshemispheres.com/' + photo['href']
        
        #list with links
        photo_links.append(photo_url)

    photo_links

    
    mars_info = {
        "mars_news": {
            "news_title": title,
            "news_p": paragraph.text,
            },
        "mars_img": featured_image_url,
        "mars_fact": html_table,
        "mars_hemisphere": photo_links
    }
browser.quit()

return mars_info