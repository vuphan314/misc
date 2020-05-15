function main_cc {
  out_file=./tmp.out
  g++ -o $out_file tmp.cc -lgmp
  # $out_file
}

function main_tex {
  out_dir=.
  latexmk -outdir=$out_dir -pdf -synctex=-1
  evince $out_dir/tmp.pdf &
}

################################################################################

main_cc
# main_tex
