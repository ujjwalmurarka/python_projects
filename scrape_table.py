#!/usr/bin/env python
# coding: utf-8

# In[61]:


from selenium import webdriver
import pandas as pd
import xlsxwriter  
import bs4


# In[69]:


url = input('Enter the url containing the table: ')


# In[78]:


browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(10)
response = browser.page_source


# In[71]:


soup = bs4.BeautifulSoup(response)


# In[75]:


if len(soup.select('table'))>0:
    tables = pd.read_html(response)
    with pd.ExcelWriter('output_tables.xlsx', engine='xlsxwriter') as output:
        for i in range(0,len(tables)):
            tab_number = i+1
            tab_name = 'sheet'+str(tab_number)
            tables[i].to_excel(output,sheet_name=tab_name)
    print('Outputs saved in excel')
else: 
    print('No tables found on the page')


# In[76]:


if input('Exit page (y/n): ')=='y':
    browser.quit()

