n = 20
id = Array.new(n)
thread = Array.new(n)
1.upto(n) do |x|
	id[x] = x.to_s
	puts id[x]
	puts "ruby client.rb #{id[x]} #{id[x]}"
	thread[x] = Thread.new { system "ruby client.rb #{id[x]}"}
end
1.upto(n) do |x|
	thread[x].join
end
