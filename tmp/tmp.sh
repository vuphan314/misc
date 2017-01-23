function tmp_cpp {
  out_file=/tmp/tmp.out
  g++ tmp.cpp -o $out_file
  $out_file
}

function tmp_tex {
  out_dir=/tmp/out
  latexmk -pdf --synctex=-1 -outdir=$out_dir
  evince $out_dir/tmp.pdf
}

############################################################

tmp_cpp

# tmp_tex
