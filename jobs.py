import requests
import json
import inspect

def get_page(page_num):
    """ 
    Returns a page of jobs from Github

    `page` specifies which page to return
    """

    response = requests.get(f'https://jobs.github.com/positions.json?page={page_num}')

    return [f"{job['company']} - {job['title']} [{job['location']}]" for job in json.loads(response.text)]

def pages():
    """
    A generator to yield successive pages from `get_page`

    When an empty page is returned, the generator should terminate
    """

    yield None

def jobs():
    """
    A generator to yield individual jobs

    This should iterate over the `pages` generator yielding successive jobs.

    It should not buffer more than one page at a time.
    """

    yield None

def filtered_jobs(query):
    """
    A generator to yield individual jobs from the Github API matching 
    a query

    This should yield one job at a time. You'll like want to iterate over your
    `jobs` generator.

    Jobs should all contain `query` as a case insensitive substring.
    """

    yield None

# The following code should not require modification
# Once your generators are working correctly, this should print all current web jobs
if __name__ == '__main__':
    assert(inspect.isgenerator(pages()))
    assert(inspect.isgenerator(jobs()))
    assert(inspect.isgenerator(filtered_jobs("Web")))

    for job in filtered_jobs("Web"):
        print(job)
