#!/bin/sh

if [ "$1" = "--extend" ] && [ -n "$2" ]; then
   when="$2 hours ago"
else
   when=today
fi

# use ex. `--extend 4` to only have the date added if it's past 4am (otherwise, use the  yesterday)

# if the `when` date is ill-formed, just use today's date
d="$(date -d "$when" '+# %Y-%m-%d' 2>/dev/null)"
log="$HOME/.scripts/output/pomo.log"

if [ -n "$d" ] && [ -f "$log" ]; then
   grep -xqE "^$d$" "$log" || echo "\n$d" >> "$log"
fi
