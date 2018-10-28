#Test for Part 5
my @strings_1 = ("be or not to be", "to be to be", "to be to be to be", "to be to be to be to be", "to be or", "to be", "to be or not", "to be or not to");
my @strings_2 = ("hello", "world!!", "hello!?", "perl?!", "cat.", "dog?", "computer..", "world!");
my @strings_3 = ("1/25/2018", "3/11/2119", "6/8/224", "1/30/0","1/1/131357");;
my @strings_4 = ("bag ok asdfasdfafdas", "o aaasasdfas a", "okasdfasfdsaf lol a", "abc a asdfasfdasfasfa", "doga a al", "asb asdf llll");

# foreach my $string (@strings_1){
    # if($string =~ m/((to|be|or|not)\s)+(to be)$/){
        # print "true\n";
    # }else{
        # print "false\n";
    # }
# }

# foreach my $string (@strings_2){
    # if($string =~ m/(\w|[!?]{2})$/){
        # print "true\n";
    # }else{
        # print "false\n";
    # }
# }

# foreach my $string (@strings_3){
    # if($string =~ m/^([1-9]|1[0-2])\/([1-9]|[12]\d|30)\/[1-9]\d{0,3}$/){
        # print "true\n";
    # }else{
        # print "false\n";
    # }
# }

# foreach my $string (@strings_4){
    # if($string =~ m/^((\w{1,4})\s)*\w{1,4}$/){
        # print "true\n";
    # }else{
        # print "false\n";
    # }
# }

my @match_1 = ("F a", "F  b", "F c", "a", "b", "c");
my @match_2 = ("oneone", "#1oneone", "#1one#1one", "a", "b", "c");
my @match_3 = ("a", "b", "c", "?", ".", "!");

# foreach my $string (@match_1){
#     if($string =~ m/[-+]?\d*(\.\D+)?F\s/){
#         print "true\n";
#     }else{
#         print "false\n";
#     }
# }
# foreach my $string (@match_2){
#     if($string =~ m/(#?)(1?)(one)\1\2\3/){
#         print "true\n";
#     }else{
#         print "false\n";
#     }
# }
foreach my $string (@match_3){
    if($string =~ m/((a*?)\b).*\w\2\1/){
        print "true\n";
    }else{
        print "false\n";
    }
}