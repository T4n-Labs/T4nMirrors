#!/usr/bin/env python3

import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# URL raw github mirror
base_url = "https://raw.githubusercontent.com/T4n-Labs/T4nMirrors/main/{arch}/{package}"

# search script
search_script = """
<script>
function searchPackages(inputId, listId) {
    const input = document.getElementById(inputId).value.toLowerCase();
    const listItems = document.getElementById(listId).getElementsByTagName('li');

    for (let i = 0; i < listItems.length; i++) {
        const txt = listItems[i].innerText.toLowerCase();

        if (txt.includes(input))
            listItems[i].style.display = '';
        else
            listItems[i].style.display = 'none';
    }
}
</script>
"""

def generate_page(archs, root_path, index_text="<ul>"):

    for arch in archs:

        logging.info("Generating page for arch: %s", arch)

        arch_name = arch.name

        # add arch to root page
        index_text += f'<li><a href="{arch_name}/index.html">{arch_name}</a></li>\n'

        arch_text = f"""<html>
<head>
<title>T4n OS Packages ({arch_name})</title>
{search_script}
</head>

<body>

<a href="{root_path}index.html">../</a>

<h1>T4n OS Packages ({arch_name})</h1>

<input type="text" id="search_{arch_name}" placeholder="Search package..."
onkeyup="searchPackages('search_{arch_name}', 'pkglist_{arch_name}')">

<ul id="pkglist_{arch_name}">
"""

        packages = sorted(arch.glob("*.xbps"))

        for pkg in packages:

            logging.info("Generating entry for package: %s", pkg.name)

            pkg_url = base_url.format(
                arch=arch_name,
                package=pkg.name
            )

            pkg_name = pkg.name.split(".xbps")[0]

            arch_text += f'<li><a href="{pkg_url}">{pkg_name}</a></li>\n'

        arch_text += """
</ul>

</body>
</html>
"""

        with open(arch / "index.html", "w") as f:
            f.write(arch_text)

    index_text += "</ul></body></html>"

    with open("index.html", "a") as f:
        f.write(index_text)


def clear_page():

    with open("index.html", "w") as f:
        f.write("")


def main():

    page1 = (Path("x86_64"),)

    clear_page()

    index_text = "<html><head><title>T4n OS Packages</title></head><body>\n"
    index_text += "<h1>T4n OS Package Mirror</h1>\n<ul>\n"

    generate_page(page1, "../", index_text)


if __name__ == "__main__":
    main()