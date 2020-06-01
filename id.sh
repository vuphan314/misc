#!/bin/bash

################################################################################

ID_TAGS="addmc|phan|vhp|dudek|jmd|vardi|rice|nots"

EXCLUDED_DIRS="{cudd-3.0.0,jet,rsynth,.git,.gitmodules}"

EXCLUDED_FILES=".git*"

COMMAND="grep --ignore-case --extended-regexp \"$ID_TAGS\" --dereference-recursive $1 --exclude-dir=$EXCLUDED_DIRS --exclude=\"$EXCLUDED_FILES\" --binary-files=without-match --color"

################################################################################

echo $COMMAND $1
echo

eval $COMMAND $1
