class BrowserHistory(object):

    # BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.current_index = 0

    # void visit(string url) Visits url from the current page. It clears up all the forward history.
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        # Remove any forward history after the current position
        self.history = self.history[:self.current_index + 1]
        # creates a new list that contains all elements from the start (:) of self.history up to, but not including,
        # self.history[self.current_index + 1].
        # self.current_index + 1 refers to the next position in the list after the current index.
        # All entries after the current index are excluded from this new list, thereby clearing any forward history.

        self.history.append(url)  # append new URL to history
        self.current_index += 1  # increment index bc you are now at that new URL (you are the last index)

    # string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x,
    # you will return only x steps. Return the current url after moving back in history at most steps.
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        # cant go farther back then 0
        self.current_index = max(0, self.current_index - steps)
        # return page you are now on
        return self.history[self.current_index]

    # string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and
    # steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        # cant go further back than length-1 (last index)
        self.current_index = min(len(self.history) - 1, self.current_index + steps)
        # return page you are now on
        return self.history[self.current_index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
# browserHistory = BrowserHistory("leetcode.com")


# Test case
def test_browser_history():
    browserHistory = BrowserHistory("leetcode.com")
    assert browserHistory.visit("google.com") == None
    assert browserHistory.visit("facebook.com") == None
    assert browserHistory.visit("youtube.com") == None
    assert browserHistory.back(1) == "facebook.com"
    assert browserHistory.back(1) == "google.com"
    assert browserHistory.forward(1) == "facebook.com"
    assert browserHistory.visit("linkedin.com") == None
    assert browserHistory.forward(2) == "linkedin.com"
    assert browserHistory.back(2) == "google.com"
    assert browserHistory.back(7) == "leetcode.com"

    print("All test cases passed!")


# Run the test case
test_browser_history()
