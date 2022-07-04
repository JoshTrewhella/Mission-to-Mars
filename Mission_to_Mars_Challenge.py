#!/usr/bin/env python
# coding: utf-8

# In[330]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import numpy as np


# In[331]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[332]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[333]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[334]:


slide_elem.find('div', class_='content_title')


# In[335]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[336]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[337]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[338]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[339]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[340]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[341]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[342]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[343]:


df.to_html()


# In[344]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[345]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

# Loop through returned results
for i in range(4):

    browser.links.find_by_partial_text('Hemisphere')[i].click()

    html = browser.html
    img_soup = soup(html,"html.parser")

    img_url_rel = img_soup.find('img', class_="wide-image").get('src')
    img_url = f'https://marshemispheres.com/{img_url_rel}'
    title = img_soup.find('h2', class_='title').text

    hemispheres = {'img_url': img_url,'title': title}
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()


# In[346]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[347]:


# 5. Quit the browser
browser.quit()


# In[ ]:




