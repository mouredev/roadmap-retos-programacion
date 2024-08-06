class MegaAnfitrion
    attr_accessor :nombres

    def initialize(nombres = 'Mundo')
        @nombres = nombres
    end

    def decir_hola
        if @nombres.nil?
            puts '...'
        elsif @nombres.respond_to?('each')
            @nombres.each { |nombre|
                puts "Hola #{nombre}"
        }
        else
            puts "Hola #{@nombres}"
        end
    end

    def decir_adios
        if @nombres.nil?
            puts '...'
        elsif @nombres.respond_to?('join')
            puts "Adiós #{@nombres.join(',')}. Vuelvan pronto"
        else
            puts "Adiós #{nombres}"
        end
    end
end

if __FILE__ == $0
    ma = MegaAnfitrion.new
    ma.decir_hola
    ma.decir_adios

    ma.nombres = 'Edward'
    ma.decir_hola
    ma.decir_adios

    ma.nombres = ['Alexis', 'Maldonado', 'Vargas']
    ma.decir_hola
    ma.decir_adios

    ma.nombres = nil
    ma.decir_hola
    ma.decir_adios
end
