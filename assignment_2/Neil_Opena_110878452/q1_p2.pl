#Part 2 - Preparing an Exhibition
use strict;
use warnings;

open INPUT, "<collections.csv" or die "Can't open input file: $!";

my $min_year = "+inf";
my $max_year = "-inf";
my $min_id = 0;
my $max_id = 0;

while (<INPUT>){
    if($. > 1){
        my @line = split(",", $_);
        my $line_year = $line[3];
        if($line_year < $min_year){
            $min_year = $line_year;
            $min_id = $line[0];
        }
        if($line_year > $max_year){
            $max_year = $line_year;
            $max_id = $line[0];
        }
    }
}

print "$min_id\n";
print "$max_id\n";


close INPUT;