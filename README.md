# stats.ninefiveslabs.io

## What is this?

A bunch of scripts, used to translate NGINX access logs for simple image-based tracking to a goaccess report.

Idea based on [this blog post](https://benhoyt.com/writings/replacing-google-analytics/).

## How to use it?

Requires [goaccess 1.3+](https://goaccess.io/download#installation).

`render_stats.sh` takes a `$LOGFILE` and translates it to `parsed.log`, which is then rendered using goaccess to `$OUTDIR` as `$OUTFILE`. Configuration file for `goaccess` is provided as `goaccessrc` in the repository.
