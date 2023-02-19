def quine(template):
    print(f"{template}({template!r})")

quine('def quine(template):\n    print(f"{template}({template!r})")\n\nquine')
