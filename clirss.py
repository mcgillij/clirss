from rich.console import Console
from rich.prompt import Prompt
from rich.tree import Tree
from rich.markdown import Markdown
import feedparser
from stripper import strip_tags
import html2markdown
from rich.traceback import install
from rich import inspect
install()

c = Console()
#c = Console(style="black on white")
c.print('Welcome to clirss')

feed = Prompt.ask("Please enter an RSS feed to fetch: ")

c.print(f"You chose {feed}")


if feed:
    d = feedparser.parse(feed)
    tree = Tree(d.feed.title)
    for e in d.entries:
        branch = tree.add(e.title)
        branch.add(e.published)
        summary_md = Markdown(e.summary)
        branch.add(strip_tags(summary_md.markup))
        content_md = html2markdown.convert(e.content[0].value)
        content_stripped = strip_tags(content_md)
        content = Markdown(content_stripped)
        branch.add(content)
        branch.add(e.link)

    with c.pager(styles=True):
        c.print(tree)

# check if file of feeds exists, if it does skip prompt and fetch feeds otherwise prompt to add feed
