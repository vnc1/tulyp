#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Credit to https://github.com/laszloszurok/tulyp

import sys
import dbus

from tulyp.utils.misc import get_dbus_interface
from tulyp.screen.ui import Screen

def get_active_players():
    bus = dbus.SessionBus()
    names = bus.list_names()

    prefix = "org.mpris.MediaPlayer2."
    players = [name[len(prefix):] for name in names if name.startswith(prefix)]

    return players


def resolve_player(cli_arg: str | None) -> str:
    if cli_arg:
        return cli_arg

    players = get_active_players()

    if len(players) == 1:
        return players[0]

    if len(players) == 0:
        print("No players found.")
        sys.exit(1)

    print("Multiple players found:", ", ".join(players))
    print("Please specify one.")
    sys.exit(1)


def main() -> None:
    player_arg = sys.argv[1] if len(sys.argv) > 1 else None
    player = resolve_player(player_arg)

    Screen(dbus_interface=get_dbus_interface(player=player)).run()


if __name__ == "__main__":
    main()
