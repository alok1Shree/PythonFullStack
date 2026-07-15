# ============================================================
# FILE: payment_system.py
# ============================================================

# ── BASE CLASS ───────────────────────────────────────────────
class Payment:

    def __init__(self, payer_name, amount):
        if not payer_name or not payer_name.strip():
            raise ValueError("Payer name is required")
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.__payer_name = payer_name.strip()
        self.__amount     = amount

    @property
    def payer_name(self): return self.__payer_name

    @property
    def amount(self): return self.__amount

    def calculate_fee(self):
        return 0    # default: no fee

    def process_payment(self):
        print(f"Processing ₹{self.__amount} for {self.__payer_name}")

    def execute_transaction(self):
        print("━" * 35)
        print(f"Payer       : {self.__payer_name}")
        print(f"Amount      : ₹{self.__amount}")
        print(f"Fee         : ₹{self.calculate_fee()}")
        print(f"Total       : ₹{self.__amount + self.calculate_fee()}")
        print(f"Method      : {self.__class__.__name__}")
        self.process_payment()   # calls overridden version
        print("━" * 35 + "\n")


# ── CHILD CLASSES ────────────────────────────────────────────
class CreditCardPayment(Payment):

    def __init__(self, payer_name, amount, card_number, bank_name):
        super().__init__(payer_name, amount)
        self.__card_number = self.__mask_card(card_number)
        self.__bank_name   = bank_name
        self.__fee_percent = 2.0

    def calculate_fee(self):     # OVERRIDES
        return self.amount * self.__fee_percent / 100

    def process_payment(self):   # OVERRIDES
        print(f"💳 Credit Card charged: {self.__card_number} [{self.__bank_name}]")
        print("   Status: APPROVED ✅")

    def __mask_card(self, card):
        return "**** **** **** " + card[-4:]


class UPIPayment(Payment):

    def __init__(self, payer_name, amount, upi_id, upi_app):
        super().__init__(payer_name, amount)
        self.__upi_id  = upi_id
        self.__upi_app = upi_app

    # calculate_fee() not overridden — inherits 0 from parent

    def process_payment(self):   # OVERRIDES
        print(f"📱 UPI Payment via {self.__upi_app} to {self.__upi_id}")
        print("   UPI PIN verified ✅")
        print("   Amount debited instantly ✅")


class NetBankingPayment(Payment):

    def __init__(self, payer_name, amount, bank_name, account_type):
        super().__init__(payer_name, amount)
        self.__bank_name    = bank_name
        self.__account_type = account_type

    def calculate_fee(self):     # OVERRIDES — flat ₹25
        return 25.0

    def process_payment(self):   # OVERRIDES
        print(f"🏦 Net Banking via {self.__bank_name} [{self.__account_type}]")
        print("   OTP verified ✅")
        print("   Transaction successful ✅")


class CashOnDelivery(Payment):

    def __init__(self, payer_name, amount, delivery_address, estimated_days):
        super().__init__(payer_name, amount)
        self.__delivery_address = delivery_address
        self.__estimated_days   = estimated_days

    def calculate_fee(self):     # OVERRIDES — flat ₹40
        return 40.0

    def process_payment(self):   # OVERRIDES
        print("📦 Cash on Delivery scheduled")
        print(f"   Address  : {self.__delivery_address}")
        print(f"   Delivery : {self.__estimated_days} days ✅")
        print(f"   Pay ₹{self.amount + self.calculate_fee()} on delivery")


# ============================================================
# FILE: main.py — Polymorphism in Action
# ============================================================

print("╔═══════════════════════════════════╗")
print("║     PAYMENT PROCESSING SYSTEM     ║")
print("╚═══════════════════════════════════╝\n")

print("==== INDIVIDUAL TRANSACTIONS ====\n")

p1 = CreditCardPayment("Aman Kumar", 5000, "4111111111111234", "HDFC")
p2 = UPIPayment("Riya Sharma", 1200, "riya@ybl", "PhonePe")
p3 = NetBankingPayment("Zoya Patel", 15000, "SBI", "Savings")
p4 = CashOnDelivery("Kabir Singh", 2500, "123, MG Road, Bengaluru", 3)

# RUNTIME POLYMORPHISM — same call, different behaviour
for payment in [p1, p2, p3, p4]:
    payment.execute_transaction()

# ── BATCH PROCESSING ─────────────────────────────────────────
print("==== BATCH PROCESSING ====\n")

transactions = [
    CreditCardPayment("Alice",   3000,  "4111000011112222", "ICICI"),
    UPIPayment       ("Bob",     800,   "bob@paytm",         "Paytm"),
    NetBankingPayment("Charlie", 12000, "Axis",              "Current"),
    UPIPayment       ("Diana",   500,   "diana@gpay",        "GPay"),
    CreditCardPayment("Eve",     7500,  "5500000000001234",  "Kotak"),
    CashOnDelivery   ("Frank",   1800,  "45 Park Street",    5),
]

total_revenue = 0
total_fees    = 0
upi_count     = 0
card_count    = 0

for txn in transactions:
    fee = txn.calculate_fee()
    total_revenue += txn.amount
    total_fees    += fee

    if isinstance(txn, UPIPayment):        upi_count  += 1
    if isinstance(txn, CreditCardPayment): card_count += 1

    print(f"{txn.__class__.__name__:<20} | {txn.payer_name:<12} "
          f"| ₹{txn.amount:>8,.2f} | Fee: ₹{fee:.2f}")

print("─" * 60)
print(f"Total Transactions : {len(transactions)}")
print(f"Total Revenue      : ₹{total_revenue:,.2f}")
print(f"Total Fees Earned  : ₹{total_fees:,.2f}")
print(f"UPI Payments       : {upi_count}")
print(f"Card Payments      : {card_count}")