import click
import textrank


@click.group()
def cli():
    pass


@cli.command()
def initialize():
    """Download required nltk libraries."""
    textrank.setup_environment()


@cli.command()
@click.argument('filename')
@click.argument('summary_length', type=int)
def extract_summary(filename, summary_length):
    """Print summary text to stdout."""
    with open(filename) as f:
        summary = textrank.extract_sentences(f.read(), summary_length)
        print(summary)


@cli.command()
@click.argument('filename')
def extract_phrases(filename):
    """Print key-phrases to stdout."""
    with open(filename) as f:
        phrases = textrank.extract_key_phrases(f.read())
        print(phrases)
