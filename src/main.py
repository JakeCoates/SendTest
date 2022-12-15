from src.models.models import LineDetails, WordDetails

class problem_1():
    def __init__(self, path_to_file):
        """_summary_

        :param path_to_file: path to the input file
        """
        self.path_to_file: str = path_to_file
        self.words = {}
        self.lines = []
        self.load_data()

    def load_data(self):
        with open(self.path_to_file, encoding="utf-8") as f:
            content = f.readlines()
            self.format_data([line for line in content])
    
    def format_data(self, lines):
        for line_index, line in enumerate(lines):
            self.lines.append(
                LineDetails(
                    line_no = line_index,
                    char_length = len(line),
                    text = line
                )
            )

    def count_words(self, words):
        for line in self.lines:
            for word in words:
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
        # remove all characters before word 1
        char_to_remove = word1.char_no
        
        # remove all characters after word 2
        char_to_remove += word2.remaining_chars
        return char_to_remove
    
    def determine_distance(self, word1: str, word2: str):
        closest_line_no = None
        distance = None
        for main_word in self.words[word1]:
            line_occurances = [line.line_no for line in self.words[word2]]
            closest_line = min(line_occurances, key=lambda x:abs(x-main_word.line_no))
            
            secondary_word = [line for line in self.words[word2] if line.line_no is closest_line][0]
            
            after = False
            # determine if secondary word is before or after main word
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

        return closest_line_no
    