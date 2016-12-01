require 'httparty'

ENV['FOOD2FORK_KEY'] = '61eed7f41f58b3490f9303c483acdec1'
class Recipe
  include HTTParty

  base_uri "http://food2fork.com/api"
  default_params key: ENV["FOOD2FORK_KEY"]
  format :json

  def self.for (keyword)
    get("/search", query: {q: keyword})["recipes"]
  end
end
