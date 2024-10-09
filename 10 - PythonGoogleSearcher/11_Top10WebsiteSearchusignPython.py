from googlesearch import search

def GoogleSearch(Query):
    SearchResults = search(Query, num_results = 10)

    for i, result in enumerate(SearchResults, start=1):
        print(f'Result {i}: {result}')


Query = input('Search here, what you want to search:  \n')
GoogleSearch(Query)

"""
Search here, what you want to search:  
Automation Anywhere Company
Result 1: https://www.automationanywhere.com/
Result 2: https://www.automationanywhere.com/
Result 3: https://en.wikipedia.org/wiki/Automation_Anywhere
Result 4: https://in.linkedin.com/company/automation-anywhere
Result 5: https://www.crunchbase.com/organization/automation-anywhere
Result 6: https://www.coforge.com/who-we-are/partner-ecosystem/automation-anywhere
Result 7: https://www.youtube.com/automationanywhere
Result 8: https://www.infosys.com/about/alliances/automation-anywhere.html
Result 9: https://www.forbes.com/companies/automation-anywhere/
Result 10: https://www.glassdoor.co.in/Overview/Working-at-Automation-Anywhere-EI_IE555068.11,30.htm
"""

