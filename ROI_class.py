class roi:
    def __init__(self):
        pass

    def income(self):
        self.rental = int(input('How much will this pay you? '))
        self.laundry = int(input('how much will you charge for laundry? '))
        self.storage = int(input('how much will you charge for storage? '))
        self.full_income = (int(self.rental) + int(self.laundry) + int(self.storage))
        print(f"Your monthly income is {self.full_income} a month.")
        continue0 = input('would you like to find your cash on cash return? Type yes to continue or quit to exit. ')
        if continue0 == 'yes':
            self.expenses()
        elif continue0 == 'quit':
            exit        

    def expenses(self):
        
        self.tax = float(input('How much for tax?\n ex: 6.25% would be .0625 '))
        self.insurance = int(input('what does the insurance cost you? '))
        self.electric = int(input('electric cost '))
        self.water = int(input('water cost '))
        self.sewer = int(input('sewer cost '))
        self.gas = int(input('gas cost '))
        self.hoa = int(input('How much is the home owner assosication? '))
        self.lawn = int(input('How much for lawn services? '))
        self.vacancy = int(input('How much to cover vacancies? '))
        self.repairs = int(input('How much are you putting away a week for repairs? '))
        self.managment = int(input('how much for your property manager? '))
        self.mortage = int(input('How much is your mortage? '))
        self.utilites = (int(self.gas) + int(self.water) + int(self.sewer) + int(self.gas) + int(self.electric))
        self.total_expenses = int(self.utilites) + int(self.hoa) + int(self.lawn) + int(self.vacancy) + int(self.repairs) + int(self.managment) + int(self.mortage) + int(self.insurance)
        print(f"Your monthly expenses are: {self.total_expenses} a month.")
        continue1 = input('would you like to find your cash on cash return? Type yes to continue or quit to exit. ')
        if continue1 == 'yes':
            self.cashflow()
        elif continue1 == 'quit':
            exit


    def cashflow(self):
        self.incomes = int(self.full_income) - int(self.total_expenses)
        print(f" Your income before tax {self.incomes}")
        self.expenses = float(self.incomes) * float(self.tax)
        self.final_expenses = int(self.incomes) - int(self.expenses)
        print(f"Your monthly income: {self.final_expenses} a month with tax.")
        continue2 = input('would you like to find your cash on cash return? Type yes to continue or quit to exit. ')
        if continue2 == 'yes':
            self.cash_On_cash()
        elif continue2 == 'quit':
            exit        
        
    
    def cash_On_cash(self):
        self.down_payment = input('How much did you put down? ')
        self.closing_cost = input('how much was closing costs? ')
        self.rehab_budget = input('how much are you putting into fixing the place up? ')
        self.total_investment = int(self.down_payment) + int(self.closing_cost) + int(self.rehab_budget)
        print(f"your total investment has been {self.total_investment} ")
        self.annual_cash_flow = 12 * int(self.final_expenses)
        print(f" your annual cash flow is ${self.annual_cash_flow}")
        self.cash_on_cash_roi = float(self.annual_cash_flow) / float(self.total_investment)
        self.cash_on_cash_roi = float(self.cash_on_cash_roi) * float(100)
        print(f'your ROI is {self.cash_on_cash_roi}%')


cash = roi()
cash.income()

