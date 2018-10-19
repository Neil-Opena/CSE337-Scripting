#Part I - Preparing an Exhibition
use strict;
use warnings;

open INPUT, "<collections.csv" or die "Can't open input file: $!";

my $test_country = <STDIN>;
chomp $test_country;

my $num = 0;

while (<INPUT>){
    my @line_arr = split(",", $_);
    my $line_country = $line_arr[2];

    $num++ if ($line_country eq $test_country);
}

print "$num\n";

close INPUT;