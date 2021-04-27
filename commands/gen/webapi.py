import click

@click.command("")
@click.argument('name')
@click.option('--count', default=1, help='number of greetings')
def dropdb(count, name):
    click.echo('Dropped the database')
    print(name)
    print(count)

@click.command()
def initx():
    click.echo('Initialized the database')