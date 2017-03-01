function tmp_cc {
  out_file=/tmp/tmp.out
  g++ tmp.cc -o $out_file
  $out_file
}

function tmp_tex {
  out_dir=/tmp/out
  latexmk -pdf --synctex=-1 -outdir=$out_dir
  evince $out_dir/tmp.pdf
}

############################################################

clear
tmp_cc
# tmp_tex
