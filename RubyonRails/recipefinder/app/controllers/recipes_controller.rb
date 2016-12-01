class RecipesController < ApplicationController
  def index
    @search_term = params[:search] || 'chocolate'
    @recipes = Recipe.search_for(@search_term)
  end
end
