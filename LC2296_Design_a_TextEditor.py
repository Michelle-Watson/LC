class TextEditor(object):

    def __init__(self):
        self.text = []
        # cursor that is to the right of the text since deletes always delete text to the left
        self.cursor = 0

    def addText(self, text):
        """
        :type text: str
        :rtype: None
        """
        # Insert the text into the list at the cursor position
        self.text[self.cursor:self.cursor] = list(text)
        # list(text) converts string into list of chars

        # Move the cursor to the end of the newly added text
        self.cursor += len(text)

    # Delete k characters to the left of the cursor.
    def deleteText(self, k):
        """
        :type k: int
        :rtype: int
        """
        # Determine the start position for deletion
        start_pos = max(0, self.cursor - k)
        # Calculate the number of characters to delete
        num_deleted = self.cursor - start_pos
        # Delete characters and update the cursor position
        del self.text[start_pos:self.cursor]
        self.cursor = start_pos
        return num_deleted

    # Move the cursor k positions to the left and return the last min(10, len) characters.
    def cursorLeft(self, k):
        """
        :type k: int
        :rtype: str
        """
        # Move the cursor left
        self.cursor = max(0, self.cursor - k)
        # Return the last min(10, len) characters to the left of the cursor
        start_pos = max(0, self.cursor - 10)
        return ''.join(self.text[start_pos:self.cursor])

    # Move the cursor k positions to the right and return the last min(10, len) characters.
    def cursorRight(self, k):
        """
        :type k: int
        :rtype: str
        """
        # Move the cursor right
        self.cursor = min(len(self.text), self.cursor + k)
        # Return the last min(10, len) characters to the left of the cursor
        start_pos = max(0, self.cursor - 10)
        return ''.join(self.text[start_pos:self.cursor])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)

def test_text_editor():
    textEditor = TextEditor()

    # Add text
    textEditor.addText("leetcode")
    assert textEditor.deleteText(4) == 4
    textEditor.addText("practice")
    assert textEditor.cursorRight(3) == "etpractice"
    assert textEditor.cursorLeft(8) == "leet"
    assert textEditor.deleteText(10) == 4
    assert textEditor.cursorLeft(2) == ""
    assert textEditor.cursorRight(6) == "practi"

    print("All test cases passed!")


# Run the test case
test_text_editor()
