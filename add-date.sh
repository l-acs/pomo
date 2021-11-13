(d="$(date '+# %Y-%m-%d')" ; log="$HOME/.scripts/output/pomo.log" ; grep -x "$d" "$log" || echo "\n$d" >> "$log")
