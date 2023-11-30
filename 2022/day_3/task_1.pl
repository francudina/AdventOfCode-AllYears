#!/usr/bin/perl

use experimental 'smartmatch';

sub uniq_vals {
    my %seen;
    grep !$seen{$_}++, @_;
}

open(file_data, "<input.txt") or die "Couldn't open file: $!";

@a_z = ("a".."z");
$total = 0;

while(<file_data>) {

   $_ =~ s/^\s+|\s+$//g;
   $h = int(length($_)/2);

   @l = split //, $_;

   @f = @l[0..$h-1];
   @s = @l[$h..length($_)];

   @r = uniq_vals(grep { $f = $_; grep $_ eq $f, @s } @f);

   foreach $e (@r){

       ($index) = grep { $a_z[lc $_] ~~ lc $e } 0 .. $#a_z;
        $total += ($e eq uc $e)? 27 + $index : 1 + $index;
   }
}
print "Sum: $total\n";
