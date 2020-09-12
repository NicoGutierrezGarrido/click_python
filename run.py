import click
import requests
import logging
import json
import progressbar
from time import sleep


sh = logging.StreamHandler()
logging.basicConfig(format='%(asctime)s |%(name)s|%(levelname)s|%(message)s',
                    level=logging.INFO,
                    handlers=[sh])

bar = progressbar.ProgressBar(
    maxval=20,
    widgets=[
        progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()
    ]
)

URL_BREAKING_BAD_API = 'https://breakingbadapi.com/api'


def progress_bar():
    for i in range(20):
        bar.update(i + 1)
        sleep(0.1)


@click.group()
def cli():
    pass


@click.command()
def random_character():
    logging.info("Exec click command random_character")
    response = requests.get(
        f"{URL_BREAKING_BAD_API}/character/random", timeout=30
    )
    bar.start()
    progress_bar()
    click.echo(json.dumps(response.json(), indent=4, sort_keys=True))
    bar.finish()
    logging.info("Exec click command random_character Finished")


@click.command()
def random_quote():
    logging.info("Exec click command random_quote")
    response = requests.get(
        f"{URL_BREAKING_BAD_API}/quote/random", timeout=30
    )
    bar.start()
    progress_bar()
    click.echo(json.dumps(response.json(), indent=4, sort_keys=True))
    bar.finish()
    logging.info("Exec click command random_quote Finished")


@click.command()
@click.option('--name', required=True, help='Name of character', type=str)
def find_character(name):
    logging.info("Exec click command find_character")
    response = requests.get(
        f"{URL_BREAKING_BAD_API}/characters?name={name}", timeout=30
    )
    bar.start()
    progress_bar()
    click.echo(json.dumps(response.json(), indent=4, sort_keys=True))
    bar.finish()

cli.add_command(find_character)
cli.add_command(random_character)
cli.add_command(random_quote)


if __name__ == '__main__':
    cli()
