#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
      self._value = None
      self.value = value
     

    @property
    def value(self):
       return self._value

    @value.setter
    def value(self, value):
       if isinstance(value, str):
          self._value = value
       else:
          print("The value must be a string.")

    def is_sentence(self):
      return self._value.endswith('.') if self._value else False
               
    def is_question(self):
       return self._value.endswith('?') if self._value else False
       
    def is_exclamation(self):
       return self._value.endswith('!') if self._value else False
       
    def count_sentences(self):
        if isinstance(self._value, str):

          import re
          sentences = re.split('[.!?]', self._value)

          sentences = [sentence for sentence in sentences if sentence]
          return len(sentences)
        else:
           print("The value must be a string.")
           return 0
