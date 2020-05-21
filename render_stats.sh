#!/bin/bash
set -eu

LOGFILE=${LOGFILE:-logs/access.log}
OUTDIR=${OUTDIR:-html}
OUTFILE=${OUTFILE:-index.html}

cd "$(dirname "${BASH_SOURCE}")"

./parse.py ${LOGFILE} > parsed.log
goaccess -p goaccessrc --no-progress parsed.log > ${OUTDIR}/${OUTFILE}
