class Microwave
    def initialize(seconds)
      @seconds = seconds
    end
    def timer
      # trata min colocados como seg
      if @seconds >= 60 && @seconds < 100
        minutes = @seconds / 60
        seconds = @seconds % 60
      # trata min:sec com segundos estrapolando o valor por minuto
      elsif @seconds % 100 > 60
        minutes = @seconds / 100
        seconds = @seconds - 100 * minutes
        minutes += 1
        seconds -= 60
      #trata valores colocados no formato min:sec
      else
        minutes = @seconds / 100
        seconds = @seconds % 100
      end
      [minutes, seconds].map{|i| '%02d' % i}.join(':')
    end
  end
  