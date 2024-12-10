#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        # Validate value on initialization
        self._value = self._validate_string(value)
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        # Validate value on assignment
        self._value = self._validate_string(new_value)
    
    def _validate_string(self, value):
        """Helper method to validate if the value is a string."""
        if not isinstance(value, str):
            print("The value must be a string.")
            return ""  # Return an empty string if validation fails
        return value

    def is_end_with(self, punctuation):
        """Helper method to check if the string ends with a specific punctuation mark."""
        return self._value.endswith(punctuation)
    
    def is_sentence(self):
        return self.is_end_with('.')
    
    def is_question(self):
        return self.is_end_with('?')
    
    def is_exclamation(self):
        return self.is_end_with('!')
    
    def count_sentences(self):
        """Split the value into sentences based on punctuation marks and count them."""
        sentences = [segment.strip() for segment in re.split(r'[.?!]', self._value) if segment.strip()]
        return len(sentences)
