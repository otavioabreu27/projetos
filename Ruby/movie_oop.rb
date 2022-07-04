@movies = {
  Hercules: 5,
  Coraline: 5,
  Batman: 5
}

@title = ""

def stay
  puts "Still want to stay on this function? y/n"
  ans = gets.chomp
  while ans != "y" && ans != "n"
    system("clear")
    puts "That's not y/n"
    puts "Still want to stay on this function? y/n"
    ans = gets.chomp
  end  
  if ans == "y"
    add
  else
    menu_function
  end
end

def menu_function 
  system("clear")
  puts""
  puts"-------------------------------------------"
  puts "Welcome to the OOP movie, chose a comand"
  puts "--type 'add' to Add a new Movie"
  puts "--type 'update' to Update a Movie Rating"
  puts "--type 'display' to Display the Movie list"
  puts "--type 'delete' to delete a Movie"
  puts"-------------------------------------------"
  puts " "
  choice = gets.chomp
  return choice
end

def show_list
  puts "Actual list"
  puts"--------------------------------"
  @movies.each do |n,r| 
    puts "#{n}: #{r}"
    puts " "
  end
  puts "-------------------------------"
  puts ""
end

def exists (n)
  return @movies[n].nil?
end


def add
  system("clear")
  show_list()
  puts "What is the movie name?"
  @title = gets.chomp
  @title.to_sym
  if exists(@title)
    puts "What's the rating?"
      rating = gets.chomp
      rating.to_i
      @movies [@title] = rating
      puts "Movie added!"
      stay()
  else
    puts "Already exists"
    stay()
  end
end


case (menu_function)
  when "add"  
    add()
end



  


