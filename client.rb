require "net/http"
params = Hash.new
params[:id] = ARGV[0]
addr = "http://192.168.1.150:8080"

while true
	params[:num] = rand(100) + 1
	uri = URI.parse(addr + "/attend")
	res = Net::HTTP.post_form(uri, params)
	sleep(1)
end
