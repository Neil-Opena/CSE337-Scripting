#Part 4 - Files and Directories
use strict;
use warnings;

mkdir "features";

my @files = ();

for(my $i = 0; $i <= 9; $i += 1){
    my $TEMP;
    open $TEMP, ">features/$i-features.txt" or die "Can't open output file: $!";
    push(@files, $TEMP);
}

open FEATURES, "<features.txt" or die "Can't open input file: $!";
while(<FEATURES>){
    my @line = split(",", $_);
    my $file = $files[$line[1]];
    print $file "$line[0]\n";
}

close FEATURES;

for(my $i = 0; $i <= 9; $i += 1){
    close $files[$i];
}
