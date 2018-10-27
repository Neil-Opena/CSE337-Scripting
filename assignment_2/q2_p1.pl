#Part 1 - Text Transformation

open INPUT, "<q2.in" or die "Can't open input file: $!";
open OUTPUT, ">q2p1.out" or die "Can't open output file: $!";

while(<INPUT>){
    print $_;
}

# sub replace_line()

close INPUT;
close OUTPUT;