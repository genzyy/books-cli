#!usr/bin/env python3

import click
import requests

__author__ = "Rishit"
apidata = ''

@click.group()
def main():
    """
    Simple CLI for querying books on Google Books!
    """
    pass

@main.command()
@click.argument('query')
def search(query):
    """
    This fetches the results and return corresponding to the given query from the given query from Google Books!
    """
    query = '+'.join(query.split())
    url_format = 'https://www.googleapis.com/books/v1/volumes'

    query_params = {
        'q': query
    }

    response = requests.get(url_format, params=query_params)

    #click.echo(response.json()['items'])
    apidata = response.json()
    #click.echo(apidata["items"])
    items = apidata["items"]
    print(end="\n")
    for item in items:
        #click.echo(item["volumeInfo"])
        vol = item["volumeInfo"]
        click.secho(vol["title"], bold=True, fg='green')
        print(end="\n")



@main.command()
@click.argument('id')
def get(id):
    """
    This returns particular book from the given id on Google Books
    """
    url_format = 'https://www.googleapis.com/books/v1/volumes/{}'
    click.echo(id)

    response = requests.get(url_format.format(id))

    #click.echo(response.json())
    

if __name__ == "__main__":
    main()
