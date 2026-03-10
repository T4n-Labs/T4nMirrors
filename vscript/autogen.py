#!/usr/bin/env python3

from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent
arch_dir = repo_root / "x86_64"

BASE_URL = "https://t4n-labs.github.io/T4nMirrors/x86_64"

packages = sorted(arch_dir.glob("*.xbps"))

html = """
<html>
<head>
<title>T4n OS Package Repository</title>

<style>
body {
    font-family: sans-serif;
    margin: 40px;
}

input {
    padding:8px;
    width:300px;
}

li {
    margin:5px 0;
}
</style>

<script>
function searchPkg() {
    let input = document.getElementById("search").value.toLowerCase();
    let items = document.getElementsByTagName("li");

    for (let i = 0; i < items.length; i++) {
        let txt = items[i].innerText.toLowerCase();
        items[i].style.display = txt.includes(input) ? "" : "none";
    }
}
</script>

</head>

<body>

<h1>T4n OS Repository</h1>

<input id="search" onkeyup="searchPkg()" placeholder="Search package...">

<ul>
"""

for pkg in packages:
    url = f"{BASE_URL}/{pkg.name}"
    html += f'<li><a href="{url}">{pkg.name}</a></li>\n'

html += """
</ul>

</body>
</html>
"""

with open(arch_dir / "index.html", "w") as f:
    f.write(html)

print("Package index generated.")