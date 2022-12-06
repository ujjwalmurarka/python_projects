from selenium import webdriver
import pandas as pd
import xlsxwriter  
import bs4

def scrape_page():
    url = input('Enter the url containing the table: ')

    browser = webdriver.Chrome()
    browser.get(url)

    print('Navigate to the page or section of the website where the table is located.\nOnce you are on the desired page, enter Y/y in the text box below')
    continue_response = input('Enter Y/y when you are ready to proceed: ')
    while continue_response.lower()!= 'y':
        continue_response = input('Enter Y/y when you are ready to proceed: ')

    response = browser.page_source

    soup = bs4.BeautifulSoup(response)

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
    browser.quit()

scrape_page()
