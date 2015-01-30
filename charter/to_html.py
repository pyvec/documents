#! /usr/bin/env python3

import markdown

with open('stanovy.txt') as f:
    body = markdown.markdown(f.read())

with open('template.html') as f:
    print(f.read().replace('{{body}}', body))
