import pygame

import object as obj

from book import text

from book import chat_gpt_logic as bot

from book import connection as con

class Book:
    def __init__(self, name, render_list):
        self.book = obj.Object(name = name, init_pos = (448, 0), init_pos_z = 1.95, order_frames = ('book_closed', 'book_opened'), order_sounds = ('paper',), all_objects = render_list)
        self.state = 'closed'
        self.lock = self.old_lock = False

        self.max_line_size = 25
        self.max_lines = 15

        self.pageX = 70
        self.pageY = 120

        self.user_text = text.Text(0, 0, font_type = None, font_size=20, initial_text="     Your questions!     ", min_text=self.max_line_size)

        self.magic_text = text.Text(0, 0, font_type = None, font_size=20, initial_text="    Magic answers!      ", min_text=self.max_line_size)
        self.offset = 0

        self.chat_bot = bot.Logic()
    
    def open_close(self, mouse_image, game_events):
        for event in game_events:
            x, y = mouse_image.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and x > 128 + 256:
                # Get the mouse position when a mouse button is pressed
                x, y = mouse_image.get_pos()
                # print(f"Mouse X: {x}, Mouse Y: {y}")
                coll_obj = self.book.all_objects.check_all((x, y))

                self.lock = not self.lock

                if coll_obj == self.book and self.state == 'closed' and self.lock != self.old_lock:
                    self.state = 'opened'
                    self.book.set_pos((0, 0))
                    self.book.set_cur_frame_num(1)
                    self.book.play_sound()
                    self.old_lock = self.lock

                if coll_obj == self.book and self.state == 'opened' and self.lock != self.old_lock:
                    self.state = 'closed'
                    self.book.set_pos((448, 0))
                    self.book.set_cur_frame_num(0)
                    self.book.play_sound()
                    self.old_lock = self.lock

    def run(self, mouse_image, game_events):
        if self.state == 'opened':
            # conversation logic
            for event in game_events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if con.is_internet_connected():
                            self.magic_text.text = "     Magic answers!       "
                            self.magic_text.text += self.chat_bot.run(self.user_text.text[self.max_line_size:-1])
                            self.magic_text.text = self.filter_ascii_basic(self.magic_text.text)
                            self.magic_text.text = self.remove_special_characters(self.magic_text.text)
                            self.user_text.text = "     Your questions!     "
                        else:
                            return False
                    else:
                        self.user_text.handle_event(event)

            # your questions rendered
            self.book.get_cur_frame().set_text(True)
            self.book.get_cur_frame().clear_text()

            lines = []
            counter = 0
            while counter * self.max_line_size < len(self.user_text.text):
                start_index = counter * self.max_line_size
                end_index = (counter + 1) * self.max_line_size
                line_text = self.user_text.text[start_index:end_index]

                # Check if line_text is not empty and the last character is not a space, '?', or '!'
                # if line_text and line_text[-1] not in (' ', '?', '!') and len(line_text) == self.max_line_size:
                    # line_text += '-'

                lines.append(text.Text(self.pageX, self.pageY + counter * 20, font_type = None, font_size=20, initial_text=line_text))
                counter += 1

            if len(lines) < self.max_lines:
                for line in lines:
                    # line.render(self.book.all_objects.get_game_surface())

                    # self.book.get_cur_frame().clear_text()
                    line.render(self.book.get_cur_frame().get_text_surface())
            else:
                zero_counter = 0
                for line_counter in range(len(lines) - self.max_lines, len(lines)):
                    lines[line_counter].text_rect.topleft = (self.pageX, self.pageY + zero_counter * 20)
                    # lines[line_counter].render(self.book.all_objects.get_game_surface())

                    # self.book.get_cur_frame().clear_text()
                    lines[line_counter].render(self.book.get_cur_frame().get_text_surface())

                    zero_counter += 1
            
            # bot answers rendered if they are to long mouse operation will scroll the text
            '''
            lines = []
            counter = 0
            while counter * self.max_line_size < len(self.magic_text.text):
                start_index = counter * self.max_line_size
                end_index = (counter + 1) * self.max_line_size
                line_text = self.magic_text.text[start_index:end_index]

                # Check if line_text is not empty and the last character is not a space, '?', or '!'
                if line_text and line_text[-1] not in (' ', '?', '!') and len(line_text) == self.max_line_size:
                    line_text += '-'

                lines.append(text.Text(self.pageX + 200, self.pageY + counter * 20, font_type = None, font_size=20, initial_text=line_text))
                counter += 1
            '''
            lines = []
            counter = 0

            for line_text in self.magic_text.text.split('\n'):
                # Iterate through lines separated by '\n'

                while line_text:
                    # Process the line in chunks of max_line_size characters
                    chunk, line_text = line_text[:self.max_line_size], line_text[self.max_line_size:]

                    # if chunk and chunk[-1] not in (' ', '?', '!') and len(chunk) == self.max_line_size:
                        # chunk += '-'

                    lines.append(text.Text(self.pageX + 200, self.pageY + counter * 20, font_type=None, font_size=20, initial_text=chunk))
                    counter += 1

            if len(lines) < self.max_lines:
                for line in lines:
                    # line.render(self.book.all_objects.get_game_surface())

                    # self.book.get_cur_frame().clear_text()
                    line.render(self.book.get_cur_frame().get_text_surface())

            else:
                x, y = mouse_image.get_pos()

                if x > 256 and x < 512 and y > 256 and y < 512:
                    if self.offset < len(lines) - self.max_lines:
                        self.offset += 0.25
                elif self.offset > 0:
                    self.offset -= 0.25
                else:
                    self.offset = 0
                
                print(self.offset, (len(lines) - self.max_lines))

                zero_counter = 0
                for line_counter in range(int(self.offset), int(self.offset + self.max_lines - 1)): #len(lines) - self.max_lines, len(lines)):
                    lines[line_counter].text_rect.topleft = (self.pageX + 200, self.pageY + zero_counter * 20)
                    # lines[line_counter].render(self.book.all_objects.get_game_surface())

                    # self.book.get_cur_frame().clear_text()
                    lines[line_counter].render(self.book.get_cur_frame().get_text_surface())

                    zero_counter += 1

        return True
        
    def filter_ascii_basic(self, input_string):
        # Initialize an empty string to store the filtered result
        filtered_string = ""

        # Iterate through each character in the input string
        for char in input_string:
            # Check if the ASCII value of the character is in the range [0, 127]
            if ord(char) < 128:
                filtered_string += char

        return filtered_string
    
    def remove_special_characters(self, input_string):
        # Define a set of special characters to remove
        special_characters = {'\0', '\t', '\r'}  # Add more if needed

        # Initialize an empty string to store the result
        result_string = ""

        # Iterate through each character in the input string
        for char in input_string:
            # Check if the character is not in the set of special characters
            if char not in special_characters:
                result_string += char

        return result_string