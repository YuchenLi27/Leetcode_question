class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.curr + 1]
        self.stack.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        new_idx = self.curr - steps
        self.curr = max(0, new_idx)
        return self.stack[self.curr]

    def forward(self, steps: int) -> str:
        jump_stp = self.curr + steps
        self.curr = min(jump_stp, len(self.stack) - 1)
        return self.stack[self.curr]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)