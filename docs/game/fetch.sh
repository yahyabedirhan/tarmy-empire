#!/bin/sh
# Re-fetch the terminal.army manual pages as markdown (needs curl + pandoc).
# The copies are gitignored: they are verbatim third-party content kept for private reference only.
set -e
cd "$(dirname "$0")"
for p in index mechanics commands commander; do
  url="https://docs.terminal.army/$p/"; [ "$p" = index ] && url="https://docs.terminal.army/"
  curl -sL -A "Mozilla/5.0" "$url" | python3 -c '
import sys,re,subprocess
s=sys.stdin.read()
m=re.search(r"<article[^>]*>(.*?)</article>",s,re.S); body=m.group(1) if m else s
md=subprocess.run(["pandoc","-f","html","-t","gfm","--wrap=none"],input=body,capture_output=True,text=True).stdout
md=re.sub(r"<a href=\"#[^\"]*\" class=\"headerlink\" title=\"Permanent link\">¶</a>","",md)
md=re.sub(r"\n{3,}","\n\n",md)
print("<!-- verbatim copy of "+sys.argv[1]+" — do not edit; re-fetch with fetch.sh -->\n\n"+md,end="")
' "$url" > "$p.md"
  echo "wrote $p.md"
done
