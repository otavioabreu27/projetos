def perc_arq
  @arq.readlines.each do |line|
    ra = line[0..8]
    nome_foto = line[9..13]
    
    ra.to_s().strip()
    nome_foto.to_s().strip()

    puts(File.exist?("DSCN#{nome_foto}.PNG"))

    if File.file?(nome_foto) == true
      foto = File.open(nome_foto)
      foto.rename(nome_foto, ra)
    else
      puts("Arquivo:" + "DSCN#{nome_foto}.PNG" + " não foi encontrado.")
    end
  end
end

@nome_arq = gets.chomp
@arq = File.open(@nome_arq,"r")

perc_arq()



