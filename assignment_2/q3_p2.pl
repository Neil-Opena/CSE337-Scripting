#Part 3 - Array Operators and Hashes
use strict;
use warnings;

my %table = ("JAN"=>4840, "FEB"=>4340, "MAR"=>3900, "APR"=>4330, "MAY"=>3090, "JUN"=>3660, "JUL"=>3520, "AUG"=>3280, "SEP"=>4130, "OCT"=>3690, "NOV"=>4260, "DEC"=>4800);


print "Enter the initial month: ";
my $initial = <STDIN>;
chomp $initial;
$initial = uc $initial;

until(valid_key($initial)){
    print "Re-enter the initial month: ";
    $initial = <STDIN>;
    chomp $initial;
    $initial = uc $initial;
}

print "Enter the final month: ";
my $final = <STDIN>;
chomp $final;
$final = uc $final;

until(valid_key($initial)){
    print "Re-enter the final month: ";
    $initial = <STDIN>;
    chomp $initial;
    $initial = uc $initial;
}


sub valid_key{
    my $test = $_[0];
    foreach my $month (keys %table){
        if($month eq $test){
	    return 1;
	}
    }
    return 0;
}
