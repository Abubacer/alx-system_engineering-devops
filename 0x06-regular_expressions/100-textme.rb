#!/usr/bin/env ruby
# This a script that extracts sender, receiver, and flags.
# from a log entry file.
def extract_data(log_entry)
	from = log_entry[/\[from:(.*?)\]/, 1]
	to = log_entry[/\[to:(.*?)\]/, 1]
	flags = log_entry[/\[flags:(.*?)\]/, 1]

	return "#{from},#{to},#{flags}"
end
# script usage
if ARGV.empty?
	puts 'Usage: ./100-textme.rb <log_entry>'
	exit
end
# script output
log_entry = ARGV[0]
puts extract_data(log_entry),"\n"
