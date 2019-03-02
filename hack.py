import pandas as pd
import requests
import time, sys
#import asyncio
#from aiohttp import ClientSession

headers = {'Content-Type':'text/xml'}
for url in open('urllist.txt'):
    r = requests.post(url.strip())
    print(r.content)
    
'''for x in cleanCode:
    baseCode = base + x
    print(baseCode)
    #r = requests.post(baseCode)
    #print(r.content)
    #time.sleep(.1)
'''
'''
async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read()

async def run(r):
    url = "https://bulletins.psu.edu/ribbit/index.cgi?page=getcourse.rjs&code="
    tasks = []
    
    file = 'coursecatalog.xlsx'
    courses = pd.read_excel(file)
    courseCode = courses.SubjectCode + ' ' + courses.CatalogNumber
    cleanCode = courseCode.str.strip()
    
    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for i in cleanCode:
            task = asyncio.ensure_future(fetch(url+i, session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        print(responses)

def print_responses(result):
    print(result)

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(4))
loop.run_until_complete(future)
'''
