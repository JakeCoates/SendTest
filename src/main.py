from src.models.models import LineDetails, WordDetails
import os

class problem_1():
    def __init__(self, path_to_file, match_case=True):
        """_summary_

        :param path_to_file: path to the input file
        """
        self.path_to_file: str = path_to_file
        self.match_case = match_case
        self.words = {}
        self.lines = []
        self.load_data()

    def load_data(self):
        """
        load in the text file with the encoding selected as it isn't all plain text
        """
        if not os.path.exists(self.path_to_file):
            raise Exception("file does not exist")

        if not self.path_to_file.lower().endswith('.txt'):
            raise Exception("invalid file type")

        with open(self.path_to_file, encoding="utf-8") as f:
            content = f.readlines()
            if self.match_case:
                self.format_data([line.strip() for line in content])
            else:
                self.format_data([line.strip().lower() for line in content])
    
    def format_data(self, lines: list):
        """Format the data to allow it to be manipulated with a bit more context

        :param lines: list of lines from the txt file that have been stripped
        """
        for line_index, line in enumerate(lines):
            self.lines.append(
                LineDetails(
                    line_no=line_index,
                    char_length=len(line),
                    text=line
                )
            )

    def count_words(self, words: list()):
        """Determine all the places that the words that have been specified can be found

        :param words: list of words passed through to check for
        :return: return the dict of words and where they were found
        """
        for line in self.lines:
            for word in words:
                if not self.match_case:
                    word = word.lower()
                if word in line.text:
                    char_index = line.text.index(word)
                    if word not in self.words:
                        self.words[word] = []

                    self.words[word].append(
                        WordDetails(
                            line_no=line.line_no,
                            char_no=char_index,
                            remaining_chars=line.char_length - len(word) - char_index,
                            word=word
                        )
                    )
        return self.words

    def determine_character_overflow(self, word1, word2):
        """Determine the amount of character you need to remove either side of the 2 words
        E.G. "Blah Nautilus and Nemo Blah" you would need to remove the intial and secondary "Blah"
        alongside the whitespace and you're determining the distance between the two N's so you can remove
        the "emo" part of Nemo and leaving you with "Nautilus and N" which and then you can remove
        the N's to determine the distance between the two "autilus and " would have 12 characters between
        the two N's

        :param word1: The word that occurs first
        :param word2: The word that occurs second
        :return: The character count between the two N's
        """
        # remove all characters before word 1 including the first occurance of that character
        char_to_remove = word1.char_no + 1
        
        # remove all characters after word 2
        char_to_remove += word2.remaining_chars
        
        # remove all characters in the second word
        char_to_remove += len(word2.word)
        return char_to_remove
    
    def determine_distance(self, word1: str, word2: str):
        """Determining the smallest distance between the first word and the second
        The second word can appear before and after the first word

        :param word1: Main word to compare against
        :param word2: Secondary word to compare
        :raises Exception: Exception is raised when one of the words are not found
        :return: returns both the LineDetails object and the distance in characters
        """
        # check the casing and replace with lowercase to match the original text
        if not self.match_case:
            word1 = word1.lower()
            word2 = word2.lower()
            
        if word1 not in self.words and word2 not in self.words:
            raise Exception("One or more words not found")
        
        closest_line_no = None
        distance = None
        
        for main_word in self.words[word1]:
            line_occurances = [line.line_no for line in self.words[word2]]
            # using a lambda and list comprehension as quick way to grab the closest line
            closest_line = min(line_occurances, key=lambda x: abs(x-main_word.line_no))
            
            secondary_words = [line for line in self.words[word2] if line.line_no is closest_line]
            
            for secondary_word in secondary_words:
                # determine if secondary word is before or after main word
                after = False
                if secondary_word.line_no > main_word.line_no:
                    after = True
                if secondary_word.line_no == main_word.line_no and secondary_word.char_no > main_word.char_no:
                    after = True

                character_count = 0
                range_items = [main_word.line_no, secondary_word.line_no]
                range_items.sort()
                
                # count all characters in at the line start of word1 and the end of line of the line with word2
                for line_index in range(range_items[0], range_items[1] + 1):
                    current_line = self.lines[line_index]
                    character_count += current_line.char_length

                # remove appropriate left over characters
                if after:
                    character_count -= self.determine_character_overflow(main_word, secondary_word)
                else:
                    character_count -= self.determine_character_overflow(secondary_word, main_word)

                if not distance or abs(character_count) < distance:
                    distance = abs(character_count)
                    closest_line_no = main_word

        return closest_line_no, distance
