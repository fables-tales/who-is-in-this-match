#!/usr/bin/env python
import os
from flask import Flask
from who import CurrentMatcher
from urllib2 import urlopen
import yaml
import os

app = Flask(__name__)

WHICH_MATCH_IS_IT_BASE = os.environ.get("WMII_BASE_URL", "http://localhost:5112")

def read_match_number(match_number):
    if match_number != -1:
        cm = CurrentMatcher(open("config.yml").read())
        return yaml.dump(
            {
                "arena_0": cm.whos_in(match_number, "arena_0"),
                "arena_1": cm.whos_in(match_number, "arena_1")
            }
        )
    else:
        return yaml.dump({})

def current_match_number():
    return int(urlopen(WHICH_MATCH_IS_IT_BASE + "/current_match").read().strip())

@app.route('/who/<match_number>')
def who(match_number):
    return read_match_number(int(match_number))

@app.route("/current_match")
def current():
    return read_match_number(current_match_number())


@app.route('/next_match')
def next():
    return read_match_number(current_match_number()+1)

@app.route('/match_after_next')
def after_next():
    return read_match_number(current_match_number()+2)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
