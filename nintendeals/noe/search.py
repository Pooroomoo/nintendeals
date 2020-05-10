import logging
from datetime import datetime
from typing import Iterator, Union

from nintendeals.classes import N3dsGame, SwitchGame
from nintendeals.helpers import filter_by_date
from nintendeals.noe import list_3ds_games, list_switch_games

log = logging.getLogger(__name__)


def _search_games(
    listing,
    *,
    title: str = None,
    released_at: datetime = None,
    released_after: datetime = None,
    released_before: datetime = None,
) -> Iterator[Union[N3dsGame, SwitchGame]]:
    params = {}

    if title:
        params = {"query": f"\"{title}\""}

    for game in listing(**params):
        if not filter_by_date(
            game.release_date,
            released_at,
            released_after,
            released_before
        ):
            continue

        yield game


def search_3ds_games(
    *,
    title: str = None,
    released_at: datetime = None,
    released_after: datetime = None,
    released_before: datetime = None,
) -> Iterator[N3dsGame]:
    """
        Search and filter all the 3DS games in Nintendo of Europe.

    Parameters
    ----------
    title: str (Optional)
        String that should be contained in the title of each game.
    released_at: datetime (Optional)
        Keep only those games that have been released on this date.
    released_after: datetime (Optional)
        Keep only those games that have been released after this date.
    released_before: datetime (Optional)
        Keep only those games that have been released before this date.

    Yields
    -------
    nintendeals.classes.N3dsGame:
        3DS game from Nintendo of Europe.

    See Also
    ---------
    nintendeals.noe.list_3ds_games
    """
    log.info("Searching Nintendo 3DS games")

    yield from _search_games(
        list_3ds_games,
        title=title,
        released_at=released_at,
        released_after=released_after,
        released_before=released_before,
    )


def search_switch_games(
    *,
    title: str = None,
    released_at: datetime = None,
    released_after: datetime = None,
    released_before: datetime = None,
) -> Iterator[SwitchGame]:
    """
        Search and filter all the Switch games in Nintendo of Europe.

    Parameters
    ----------
    title: str (Optional)
        String that should be contained in the title of each game.
    released_at: datetime (Optional)
        Keep only those games that have been released on this date.
    released_after: datetime (Optional)
        Keep only those games that have been released after this date.
    released_before: datetime (Optional)
        Keep only those games that have been released before this date.

    Yields
    -------
    nintendeals.classes.SwitchGame:
        Switch game from Nintendo of Europe.

    See Also
    ---------
    nintendeals.noe.list_switch_games
    """
    log.info("Searching Nintendo Switch games")

    yield from _search_games(
        list_switch_games,
        title=title,
        released_at=released_at,
        released_after=released_after,
        released_before=released_before,
    )
