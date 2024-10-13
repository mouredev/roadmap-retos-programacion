require 'csv'

ACTIVE   = "activo"
INACTIVE = "inactivo"

def main participants_file
   return "ERROR: Debes proporcionar un fichero CSV" if participants_file.nil?
   return "ERROR: File Not Found" unless File.exist? participants_file
   participants   = []
   awards = ["ganador de una suscripción", "ganó un descuento", "ganó un libro"]

   CSV.foreach participants_file, headers: true do |participant_row|
      participant = { 
         id: participant_row["id"],
         email: participant_row["email"],
         status: participant_row["status"]
      }
      participants << participant unless participant[:status] == INACTIVE
   end

   winners = 3.times.map do  
      p = participants.shuffle!.shift

      "#{p[:id]} #{p[:email]} #{awards.shift}"
   end

end

participants_file = ARGV.first

puts main( participants_file )