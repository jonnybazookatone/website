website
=======

My personal website.

The site is written in Python/Flask, so that pages can be made on-the-fly when a user pings the server.

The webpages take from a skeleton structure, which is then filled using Python/Flask. The layout, CSS and Javascript
features are all implememented with the nice package, bootstrap.

The website is hosted on heroku, which is free for low-traffic applications like this.

The ADS is queried everytime that someone loads the "Publication" webpage, such that the references are always as up to date as possible. For this to work, a DEV_KEY must be given.
