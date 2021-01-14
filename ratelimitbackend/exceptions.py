class RateLimitException(Exception):
    def __init__(self, msg, counts):
        self.counts = counts
        super().__init__(msg)
