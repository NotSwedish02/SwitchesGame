

class Controller():
    def __init__(self, keys):
        self.keys = keys
        self.keys_pressed = {}
        self.keys_by_word = {}
        for i in self.keys:
            self.keys_pressed[i] = False

    def bind_keys(self, words):
        for i in range(len(words)):
            self.keys_by_word[words[i]] = self.keys[i]
            
    def handle_keys(self, key, is_pressed):
        if key in self.keys:
            self.keys_pressed[key] = is_pressed
