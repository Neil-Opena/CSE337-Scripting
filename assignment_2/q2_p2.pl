#Part 2 - Text Transformation
use strict;
use warnings;

open INPUT, "<q2.in" or die "Can't open input file: $!";
open OUTPUT, ">q2p2.out" or die "Can't open output file: $!";

my $k = <STDIN>;
chomp $k;

my @original = ();
my @output = ();

while(<INPUT>){
    if(keep_line($_, $k)){
	push (@output, $_);
    }
    push (@original, $_);
}

if(scalar @output == scalar @original){
    print OUTPUT "Oooh Nooo!";
}else{
    foreach my $line (@output){
        print OUTPUT $line;
    }
}

sub keep_line{
    my $line = $_[0];

    my @words = split(" ", $_[0]);
    if(scalar @words == $_[1]){
    	return 0;
    }else{
    	return 1; #1 == true, 0 == false
    }
}

close INTPUT;
close OUTPUT;
