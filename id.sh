#!/bin/bash

################################################################################

LOC="$1"

ID_TAGS="vu|phan|vhp|jeff|dudek|jmd|moshe|vardi|rice|nots"

EXCLUDED_DIRS="{.git,lib,solvers}"

EXCLUDED_FILES=".git*"

COMMAND="grep --ignore-case --extended-regexp \"$ID_TAGS\" --dereference-recursive $LOC --exclude-dir=$EXCLUDED_DIRS --exclude="$EXCLUDED_FILES" --binary-files=without-match --color"

################################################################################

echo $COMMAND
echo
eval $COMMAND
