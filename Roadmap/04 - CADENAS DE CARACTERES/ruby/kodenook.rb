
txt = 'hello, ruby!'

puts txt.size
puts txt.reverse
puts txt.upcase
puts txt.downcase
puts txt.capitalize
puts txt.strip
puts txt.split
puts txt.gsub('h', 'j')
puts txt.chars

##
# The function checks if a word is a palindrome, an anagram of another word, or an isogram.
#
# Args:
#   word: The parameter "word" is a string that represents a word.
#   word2: The parameter "word2" is used to compare with the first word to check if they are anagrams.
def word_type(word, word2) :nil
    if word == word.reverse
        puts 'is palindrome'
    end

    if word.split('').sort == word2.split('').sort
        puts 'is an anagram'
    end

    if word.size == word.split('').uniq.size
        puts 'is isogram'
    end
end

word_type('amor', 'roma')