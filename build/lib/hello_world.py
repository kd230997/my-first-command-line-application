import click


@click.command()
@click.option("--name", default="Duy", help="Your name to greetings")
def HelloWorld(name):
    print(f"Hello {name}!")
