from bs4 import BeautifulSoup
from alive_progress import alive_bar
from dateutil.parser import parse
import sys

if len(sys.argv) < 3:
    print("""Usage: blog_search.py\t-s\t--string\t[string]\n\t\t\t-t\t--tag\t\t[tag]\n\t\t\t-d\t--date\t\t[start date] [end date]\t format: YYYY/MM/DD""")
    quit()

posts_index = BeautifulSoup(open("posts/posts_index.html","r").read(),"lxml")

search_output = []

with alive_bar(len(posts_index.find_all("a")), spinner='dots_waves') as bar:
    for link in posts_index.find_all("a"):
        post = BeautifulSoup(open(f"posts/{link['href']}","r",errors="ignore").read(),"lxml")
        timestamp = post.find("span",id="timestamp").text
        tags = []
        for tag in post.find_all("span",class_="tag"):
            tags.append(tag.text.lower())
        post.find("div",id="footer").decompose()
        if sys.argv[1] == "-s" or sys.argv[1] == "--string":
            if sys.argv[2].lower() in post.text.lower():
                search_output.append([timestamp,f"posts/{link['href']}"])
        elif sys.argv[1] == "-t" or sys.argv[1] == "--tag":
            if sys.argv[2].lower() in tags:
                search_output.append([timestamp,f"posts/{link['href']}"])
        elif sys.argv[1] == "-d" or sys.argv[1] == "--date":
            if parse(sys.argv[2]) <= parse(timestamp) and parse(timestamp) <= parse(sys.argv[3]):
                search_output.append([timestamp,f"posts/{link['href']}"])
        bar()

open("search_output.html","w").write("\n".join(f"<a href='{post[1]}' target='_blank'>{post[0]}</a><br>" for post in search_output))
