class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {}  # Dictionary to store token expiration times
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        # Generate a new token with the given tokenId and set its expiration time
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        # Check if the token exists and is unexpired, then renew its expiration time
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        # Count the number of unexpired tokens at the given currentTime
        count = 0
        for expiration_time in self.tokens.values():
            if expiration_time > currentTime:
                count += 1
        return count

