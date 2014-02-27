#SRobo who is in this match tool

##Command line

run `./who.py <match_number>`

##Web

run `pip install flask` then run `python app.py`

it's got **endpoints**

```
/who/<match_number>

shows who is in the match with match number (zero indexed)

/current_match

shows who is in the current match

/next_match

shows who is in the next match

/match_after_next

shows who is in the match after the next match
```

All responses are YAML

##CONFIGURING

![Configuring is hard](http://4.bp.blogspot.com/-fYJrkNWec08/T9EYOmNGPNI/AAAAAAAAC04/UtdRRM8a3hc/s640/cat-fat-dancing-cat-gif.gif)

Give it a config.yml that looks like the one in this repository but with
more matches because there will be more matches

Also: it needs a which-match-is-it server. This defaults to
"http://localhost:5112" but reads the env var WMII_BASE_URL
