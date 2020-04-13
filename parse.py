#!/usr/bin/env python
# works with python 2.7
import re
import fileinput
import urlparse

# typical NGINX access log format
# really smart, got it from https://stackoverflow.com/a/28009294
conf = '$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"'
regex = ''.join(
    '(?P<' + g + '>.*?)' if g else re.escape(c)
    for g, c in re.findall(r'\$(\w+)|(.)', conf))
output = ''.join(
    '%(' + g + ')s' if g else c
    for g, c in re.findall(r'\$(\w+)|(.)', conf))


def extract_and_replace(match):
  url = re.search(' (.*) ', match["request"])
  if url:
    parsed = urlparse.urlparse(url.group(1))
    params = urlparse.parse_qs(parsed.query)
    try:
      match["request"] = "GET %s HTTP/1.1" % (params.get("u", ["/"])[0])
      match["http_referer"] = params.get("r", ["-"])[0]
      match["status"] = 200
    except KeyError:
      print url.group(1), "=", params
  return match


for line in fileinput.input():
  line_matches = re.match(regex, line).groupdict()
  if '95l.png' in line_matches["request"]:
    replaced = extract_and_replace(line_matches)
    print output % replaced
