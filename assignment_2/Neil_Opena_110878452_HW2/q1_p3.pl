#Part 3 - Preparing an Exhibition
use strict;
use warnings;

open COLLECTIONS, "<collections.csv" or die "Can't open input file: $!";
my $first_line = "";
my @exhibition_array = ();

while(<COLLECTIONS>){
    chomp $_;
    if($. == 1){
    	$first_line = "$_\n";
    }else{
    	push(@exhibition_array, $_);
    }
}
close COLLECTIONS;

open M1, "<m1.csv" or die "Can't open input file: $!";
while(<M1>){
    chomp $_;
    unless($. == 1){
    	push(@exhibition_array, $_);
    }
}
close M1;

open M2, "<m2.csv" or die "Can't open input file: $!";
while(<M2>){
    chomp $_;
    unless($. == 1){
    	push(@exhibition_array, $_);
    }
}
close M2;

@exhibition_array = sort @exhibition_array;

open EXHIBITION, ">exhibition.csv" or die "Can't open output file: $!";
my $file_lines = $first_line . join("\n",@exhibition_array);

#print EXHIBITION "$first_line\n";
#foreach my $elem (@exhibition_array){
#print EXHIBITION "$elem\n";
#}
print EXHIBITION $file_lines;
close EXHIBITION;
