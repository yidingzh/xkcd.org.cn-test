#!/usr/bin/env python

# This scripts generate all posts from data source - posts.json.
# For each record it read from posts.json, it will
#   - generate a page (<post_id>.html) based on post.template.html
#     > link the page to previous page if it's not first record in posts.json
#     > link the page to next page if it's not the last record in posts.json
#     > link to the original xkcd.com post (xkcd.com/<post_id>)
#     > substitute the following
#       >> img source
#       >> img title
#       >> permanent link text (translated - this page)
#       >> img link text (translated - this image)
#       >> permanent link text (original xkcd.com post)
#       >> img link text (original xkcd.com img)
#     > TODO: random button (/random): handle this in lambda@edge in cloudfront
