#!/bin/bash

################################################################################

function get_disk_usage {
  location=$1
  if [[ -z $location ]]; then
    location=.
  fi

  du $location -ah --max-depth=1 | sort -hr
}

################################################################################

get_disk_usage $@
