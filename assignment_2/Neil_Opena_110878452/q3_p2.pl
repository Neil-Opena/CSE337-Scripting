#Part 3 - Array Operators and Hashes
use strict;
use warnings;

# my %table = ("jan"=>4840, "feb"=>4340, "mar"=>3900, "apr"=>4330, "may"=>3090, "jun"=>3660, "jul"=>3520, "aug"=>3280, "sep"=>4130, "oct"=>3690, "nov"=>4260, "dec"=>4800);
my %cummulative_table = ("jan"=>4840, "feb"=>9180, "mar"=>13080, "apr"=>17410, "may"=>20500, "jun"=>24160, "jul"=>27680, "aug"=>30960, "sep"=>35090, "oct"=>38780, "nov"=>43040, "dec"=>47840);
my %to_subtract = ("jan"=>0, "feb"=>4840, "mar"=>9180, "apr"=>13080, "may"=>17410, "jun"=>20500, "jul"=>24160, "aug"=>27680, "sep"=>30960, "oct"=>35090, "nov"=>38780, "dec"=>43040);

print "Months can be selected using the three initials letters.\n";
my $three_initial_phrase = "Please enter only the three initials of a valid month.";

print "Enter the initial month: ";
my $initial = <STDIN>;
chomp $initial;
$initial = lc $initial;

until(valid_key($initial)){
    print "$three_initial_phrase\n";
    print "Re-enter the initial month: ";
    $initial = <STDIN>;
    chomp $initial;
    $initial = lc $initial;
}

print "Enter the final month: ";
my $final = <STDIN>;
chomp $final;
$final = lc $final;

until(valid_final($final)){
    print "$three_initial_phrase\n";
    print "Re-enter the final month: ";
    $final = <STDIN>;
    chomp $final;
    $final = lc $final;
}

my $ans = $cummulative_table{$final} - $to_subtract{$initial};
print "The cumulative revenue is: $ans";

sub valid_key{
    my $test = $_[0];
    foreach my $month (keys %cummulative_table){
        if($month eq $test){
	        return 1;
	    }
    }
    return 0;
}

sub valid_final{
    unless(valid_key($_[0])){
        return 0;
    }
    if($cummulative_table{$_[0]} < $cummulative_table{$initial}){
        return 0;
    }
    return 1;
}
