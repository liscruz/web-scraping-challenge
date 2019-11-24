#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import time
import os


# In[3]:


#ChromeDriver
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


#Visit Mars page
url= "https://mars.nasa.gov/news/"
browser.visit(url)


# In[5]:


#Scrape the webpage
html=browser.html
soup= bs(html, 'html.parser')


# In[6]:


#Collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
news_p = soup.find("div", class_="list_text")
news_title= news_p.find("div", class_="content_title").text
print(news_p)
print(news_title)


# In[7]:


#JPL URL
jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(jpl_url)


# In[8]:


html=browser.html
soup= bs(html, 'html.parser')
image= soup.find("img", class_="thumb")["src"]
img= "https://jpl.nasa.gov"+image
featured_image_url= img
featured_image_url


# In[9]:


#Mars Weather from Twitter
url_weather = "https://twitter.com/marswxreport?lang=en"
browser.visit(url_weather)


# In[10]:


html_weather= browser.html
soup=bs(html_weather, "html.parser")
mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
mars_weather


# In[11]:


#Mars Facts
url_hemi= "https://space-facts.com/mars/"


# In[12]:


table= pd.read_html(url_hemi)
table[0]
reformat_df = table[0]
reformat_df. columns =["Parameter", "Values"]
reformat_df.set_index(["Parameter"])


# In[13]:


html_table = reformat_df.to_html()
html_table = html_table.replace("\n","")
html_table


# In[14]:


#Mars Hemispheree
#url_hemisphere ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
#base_url= "htts://astrogeology.usgs.gov"
#browser.visit(url_hemisphere)
#html=browser.html

#Get image and title using splinter
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

html=browser.html
soup=bs(html,'html.parser')
print(soup.prettify())


# In[15]:


#create listt

hemisphere_image_urls= []

base_url =(url.split('/search'))[0]
hemispheres= soup.find_all('div', class_='description')

for hemisphere in hemispheres:
    #empty
    hemisphere_info= {}
    #title
    title=hemisphere.find('h3').text
    
    #split title
    hemisphere_info['title']=title.split('Enhanced')[0]

    #Go to each link
    hem_route=hemisphere.find('a', class_='itemLink product-item')['href']
    
    #concatenate
    hemisphere_link= base_url + hem_route
    
    #Open url
    browser.visit(hemisphere_link)
    
    html=browser.html
    
    soup=bs(html, 'html.parser')
    
    image_url=soup.find('div', class_='downloads').find('ul').find('li').find('a')['href']
    
    #addd img url
    hemisphere_info['img_url']=image_url
    
    #append
    hemisphere_image_urls.append(hemisphere_info)



    


# In[16]:



hemisphere_image_urls


# In[19]:


#scrape to python using scrape
get_ipython().system(' jupyter nbconvert --to script missionstomars.ipynb --output mars_scrape')


# In[ ]:




