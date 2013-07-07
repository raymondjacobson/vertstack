# Vertstack

## About

Vertstack is a simple and very lightweight vertical timeline generator
that lets you maintain and share events in a chronological order.

## Tech

Vertstack is built using Flask, sqlite, CoffeeScript, and SASS.

## Up and running

To get your own instance of Vertstack running and sass and coffeescript compiled:

```
git clone git@github.com:raymondjacobson/vertstack.git
cd vertstack
python vertstack.py
sass --watch static/scss/:static/css/
coffee --watch --compile --output static/js static/coffee
```
