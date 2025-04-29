class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  
        self._balance = balance               

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._log_transaction(f"Nạp {amount}")
        else:
            print("Số tiền nạp phải > 0.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self._log_transaction(f"Rút {amount}")
        else:
            print("Không đủ số dư để rút.")

    def get_balance(self):
        return self._balance

    def _log_transaction(self, message):
        print(f"Giao dịch: {message}")

account_holder = input("Nhập tên chủ tài khoản: ")
initial_balance = float(input("Nhập số dư ban đầu: "))

acc = BankAccount(account_holder, initial_balance)

deposit_amount = float(input("Nhập số tiền nạp: "))
acc.deposit(deposit_amount)
print(f"Số dư hiện tại: {acc.get_balance()}")

withdraw_amount = float(input("Nhập số tiền rút: "))
acc.withdraw(withdraw_amount)
print(f"Số dư hiện tại: {acc.get_balance()}")
