ENV["FOOD2FORK_KEY"] = '61eed7f41f58b3490f9303c483acdec1'

class Recipe
  include HTTParty

  key_value = ENV['FOOD2FORK_KEY']
  hostport = ENV['FOOD2FORK_SERVER_AND_PORT'] || 'www.food2fork.com'
  base_uri "http://#{hostport}/api"
  default_params key: key_value
  format :json
  puts key_value, hostport, base_uri

  def self.search_for search_term
    get("/search", query:{q: search_term})["recipes"]
  end
end