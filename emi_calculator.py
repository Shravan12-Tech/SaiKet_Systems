class EMICalculator:

    def __init__(self, principal, rate, months):
        self.principal = principal
        self.rate = rate
        self.months = months

    def calculate_emi(self):
        monthly_rate = self.rate / (12 * 100)

        emi = (
            self.principal
            * monthly_rate
            * (1 + monthly_rate) ** self.months
        ) / (
            (1 + monthly_rate) ** self.months - 1
        )

        return round(emi, 2)