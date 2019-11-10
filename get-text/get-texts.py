# import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import csv


def main():

    # Doing: 0 - 50

    all_projects = [["title", "tagline", "responses", "tech", "is_winner", "like_count", "members", "photo_url", "has_video", "comment_count"]]
    data = []

    start_page = 101
    end_page = 200 # 6 elements per page

    root_url = "https://devpost.com/software/search?page="
    for i in range(start_page, end_page, 1):
        req = Request(root_url + str(i))
        req.add_header('Accept', 'application/json')
        # urllib.request.urlopen(root_url + str(i))
        with urlopen(req) as response:
            res = json.loads(response.read().decode())

        # each request gets a couple projects,
        for project in res['software']:
            # print(key)
            print(project)

            # Add project name
            print(project['name'])
            data.append(project['name'])

            # Add project tagline
            print(project['tagline'])
            data.append(project['tagline'])

            # Add text from the url
            # print(get_responces(project['url']))
            data.append(get_responces(project['url']))

            # Add tags / tech used
            # print(project['tags'])
            data.append(project['tags'])

            # Add winner status
            data.append(project['winner'])

            # Add like status
            data.append(project['like_count'])

            # Add members
            data.append(project['members'])

            # Add has photo status
            data.append(project['photo'])

            # Add has video
            data.append(project['has_video'])

            # Add comment count
            data.append(project['comment_count'])

            all_projects.append(data)
            data = []

    print(all_projects)

    with open("data.csv", 'w', newline='\n') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerows(all_projects)



def get_responces(url):
    inspiration: str = ""
    what_it_does: str = ""
    how_we_built_it: str = ""
    challenges_we_ran_into: str = ""
    acomplishments_we_are_proud_of: str = ""
    with urlopen(url) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    post_soup = soup.find(id="app-details")

    headers_raw = post_soup.select('h2')
    headers = []
    for h in headers_raw:
        headers.append(h.text)
    all_text = post_soup.get_text()
    # print(all_text)

    headers = ['Inspiration', 'What it does', 'How I built it', 'Challenges I ran into', "Accomplishments that I'm proud of", "What I learned", "What's next for", "Built With"]
    alt_headers = ['Inspiration', 'What it does', 'How we built it', 'Challenges we ran into', "Accomplishments that we're proud of", "What we learned", "What's next for", "Built With"]
    text_list = []

    text_list.append(len(all_text))

    for i in range(0, len(headers) - 1, 1):
        text_list.append(get_data_between_two_headers(all_text, headers[i], headers[i+1], alt_headers[i], alt_headers[i+1]))
    # for i,t in enumerate(text_list):
    #     print(i,t)
    return text_list



    # print(headers)



def get_data_between_two_headers(infile, start, end, alt_start, alt_end) -> str:
    copy = False
    data = ""
    for line in infile.split('\n'):
        if line.strip().startswith(start) or line.strip().startswith(alt_start):
            copy = True
            continue
        if line.strip().startswith(end) or line.strip().startswith(alt_end):
            copy = False
            continue
        if copy:
            data += line

    return data + " "

main()
