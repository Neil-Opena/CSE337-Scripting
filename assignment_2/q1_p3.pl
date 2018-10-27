#Part 3 - Preparing an Exhibition
use strict;
use warnings;

open COLLECTIONS, "<collections.csv" or die "Can't open input file: $!";
my @collections_array = <COLLECTIONS>;
close COLLECTIONS;
my $first_line = $collections_array[0];
my @exhibition_array = ();
shift @collections_array;
chomp @collections_array;

open M1, "<m1.csv" or die "Can't open input file: $!";
my @m1_array = <M1>;
close M1;
shift @m1_array;

open M2, "<m2.csv" or die "Can't open input file: $!";
my @m2_array = <M2>;
close M2;
shift @m2_array;

open EXHIBITION, ">exhibition.csv" or die "Can't open output file: $!";
# don't forget first line
print "@collections_array";
close EXHIBITION;