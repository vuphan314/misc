#!/bin/bash

################################################################################

function get_disk_usage {
  location=$1
  if [[ -z $location ]]; then
    location=.
  fi

  du $location -ah --max-depth=1 | sort -h
}

################################################################################

get_disk_usage $@
