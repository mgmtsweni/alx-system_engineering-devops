#!/usr/bin/env ruby
print ARGV[0].scan(/\[from:.+?\]/).join.sub!(/\[from:/, "").sub!(/\]/, "")
print ","
print ARGV[0].scan(/\[to:.+?\]/).join.sub!(/\[to:/, "").sub!(/\]/, "")
print ","
puts ARGV[0].scan(/\[flags:.+?\]/).join.sub!(/\[flags:/, "").sub!(/\]/, "")
