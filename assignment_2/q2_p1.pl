#Part 1 - Text Transformation
use strict;
use warnings;

open INPUT, "<q2.in" or die "Can't open input file: $!";
open OUTPUT, ">q2p1.out" or die "Can't open output file: $!";

#Get standard input str1, str2
my $str1 = <STDIN>;
chomp $str1;

my $str2 = <STDIN>;
chomp $str2;

while(<INPUT>){
    my $result = swap_line($_, $str1, $str2);
    print OUTPUT "$result";
}

sub swap_line{
    #first arg = sentence
    #second arg = word to replace
    #third arg = replacement word
    #my @line = split("", @_[0]);
    my $line = $_[0];
    my $str1 = $_[1];
    my $str2 = $_[2];

    $line =~ s/$str1/$str2/g;
    return $line;
}

close INPUT;
close OUTPUT;
