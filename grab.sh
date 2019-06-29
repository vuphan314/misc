function report_syntax_error {
  function_name=$1

  echo syntax error when calling function: $function_name
}

################################################################################

function grab_list_lines {
  pattern=$1
  location=$2
  file_flag=$3 # possible empty

  grep -E $pattern -r $location $file_flag
}

function grab_list_files {
  pattern=$1
  location=$2

  grab_list_lines $pattern $location -l
}

function grab_count_files {
  pattern=$1
  location=$2

  if [[ -z $location ]]; then
    report_syntax_error "grab_count_files"
  else
    grab_list_files $pattern $location | wc -l
  fi
}

function grab_move_files {
  pattern=$1
  location=$2

  if [[ -z $location ]]; then
    report_syntax_error "grab_move_files"
  else
    new_dir=$pattern
    mkdir -p $new_dir
    grab_list_files $pattern $location | xargs -I{} mv {} $new_dir
  fi
}

function main {
  action=$1
  pattern=$2
  location=$3

  if [[ $action == "c" ]]; then
    grab_count_files $pattern $location
  elif [[ $action == "m" ]]; then
    grab_move_files $pattern $location
  else
    report_syntax_error "main"
  fi
}

################################################################################

main $@
