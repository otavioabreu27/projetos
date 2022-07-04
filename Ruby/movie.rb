movies = {
  Hercules: 5,
  Coraline: 5,
  Batman: 5
}

puts "What do you Want?"
puts "--type 'add' to Add a new Movie"
puts "--type 'update' to Update a Movie Rating"
puts "--type 'display' to Display the Movie list"
puts "--type 'delete' to delete a Movie"
puts " "
choice = gets.chomp

case choice
  when "add"
    puts "What's the title?"
    title = gets.chomp
    title = title.to_sym
    if movies[title].nil?
      puts "What's the rating?"
      rating = gets.chomp
      rating = rating.to_i
      movies [title] = rating
      puts "Movie added!"
      movies.each {|n| puts n }
    else
      puts "The movie already exists!"
    end

  when "update"
    puts "What's the title?"
    title = gets.chomp
    title = title.to_sym
    if movies[title].nil?
      puts "The movie doesn't exists!"
    else
      puts "What's the rating?"
      rating = gets.chomp
      rating = rating.to_i
      movies [title] = rating
      puts "Rating updated!"
      movies.each {|n| puts n }
    end

  when "display"
    movies.each  {|movie, rating| puts "#{movie}: #{rating}"}
  
  when "delete"
    puts "Whats the title?"
    title = gets.chomp
    title = title.to_sym
    if movies[title].nil?
      puts "The movie doesn't exists!"
    else
      movies.delete(title)
      puts "Movie deleted!"
      puts "New list: "
      movies.each {|movie, rating| puts "#{movie}: #{rating}"}
    end
  else
  puts "Error, command not found!"
end
