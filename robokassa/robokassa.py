class Robokassa:
    def __init__(self, merchant_login: str, password1: str, is_test: bool) -> None:
        self.merchant_login = merchant_login
        self.password1 = password1
        self.is_test = is_test

    def generate_link(self) -> str:
        pass
