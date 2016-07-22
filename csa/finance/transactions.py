from csa.models.accounting import Transaction


class TransactionBase:
    def __init__(self, *,
                 type,
                 user):
        self.entries = []
        self.type = type
        self.user = user


class UserDepositByHand(TransactionBase):
    def __init__(self, user, amount):
        super().__init__(
            type=Transaction.TYPES.USER_DEPOSIT)
