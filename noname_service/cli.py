"""Console script for noname_service."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for noname_service."""
    click.echo("Replace this message by putting your code into "
               "noname_service.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
