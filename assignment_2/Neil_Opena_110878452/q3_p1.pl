#Part 3 - Array Operators and Hashes
use strict;
use warnings;

my $file = $ARGV[0];

open INPUT, "<$file" or die "Can't open input file: $!";

my %dict = (0 => "", 1 => "", 2 => "", 3 => "", 4 => "", 5 => "", 6 => "", 7 => "", 8 => "", 9 => "");

while(<INPUT>){
    chomp $_;
    my @line = split(",", $_);
    my $feature = $line[1];
    $dict{$feature} = $dict{$feature} . " $line[0]";
}

for(my $i = 0; $i <= 9; $i+=1){
    my @temp = split(" ", $dict{$i});
    print scalar @temp . "\n";
}
