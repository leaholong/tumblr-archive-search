# tumblr-archive-search
Python program allowing Tumblr users to search their blog backups

## Dependencies
Running this program requires that you install the `bs4` and `alive_progress` modules. You can do so by typing the following code into your command line:
```
py -m pip install bs4
```
```
py -m pip install alive_progress
```
## Installation
1. Download `blog_search.py` from this repository
2. Place `blog_search.py` in the root folder of your Tumblr blog backup.
## Usage
Open a command line instance in the root folder of your Tumblr blog backup.

There are three arguments you can use to search your blog: `-s` or `--string`, `-t` or `--tag`, and `-d` or `--date`.

At this early stage of development, only one may be used at a time.

To search for all posts containing the text "duck", enter the following:
```
blog_search.py -s duck
```
Alternatively, each argument has a longer notation for ease of use, meaning the following code returns an identical result:
```
blog_search.py --string duck
```
(The program is not case-sensitive, so posts containing "Duck", "DUCK", and the like will also come up).

A progress bar will appear as the program searches your posts. When it is complete, a new file titled `search_output.html` will appear in the root folder of your Tumblr blog backup. This file can be opened in a browser, and when opened will look something like this:

![Screenshot 2024-08-24 130008](https://github.com/user-attachments/assets/1646742f-4a62-4b80-8bb2-241b65102e92)

Each link is a post containing the text "duck" from the date and time listed. Clicking these links will open the posts in a new tab as an HTML file.

Every search will automatically update `search_output.html` with the results, so it is not necessary to delete this file between searches.

### Search by tag

To search for a list of your posts with a certain tag, for example, "fav", enter one of the following options:
```
blog_search.py -t fav
```
```
blog_search.py --tag fav
```
### Search by date
To search for a list of your posts in a certain date range, such as December 25th, 2023, to January 1st, 2024, enter one of the following options:
```
blog_search.py -d 2023/12/25 2024/01/01
```
```
blog_search.py --date 2023/12/25 2024/01/01
```
I use the date format YYYY/MM/DD. Other date formats will work so long as they do not contain any spaces. For example, `12/25/2023` and `1/1/2024` will work, but `December 25, 2023` will not.
