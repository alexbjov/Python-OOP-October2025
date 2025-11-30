from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }
    
    CLIENT_TYPES = {
        "Adult": Adult,
        "Student": Student
    }
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: list[BaseLoan] = []
        self.clients: list[BaseClient] = []
    
    def add_loan(self, loan_type: str) -> str:
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")
        
        new_loan = self.LOAN_TYPES[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."
    
    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")
        
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        
        new_client = self.CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."
    
    def grant_loan(self, loan_type: str, client_id: str) -> str:
        searched_loan = next((loan for loan in self.loans if loan.__class__.__name__ == loan_type), None)
        searched_client = next((client for client in self.clients if client.client_id == client_id), None)
        
        if (searched_client.__class__.__name__ == "Adult" and loan_type == "StudentLoan") or (
                searched_client.__class__.__name__ == "Student" and loan_type == "MortgageLoan"):
            raise Exception("Inappropriate loan type!")
        
        self.loans.remove(searched_loan)
        searched_client.loans.append(searched_loan)
        return f"Successfully granted {loan_type} to {searched_client.name} with ID {searched_client.client_id}."
    
    def remove_client(self, client_id: str) -> str:
        searched_client = next((client for client in self.clients if client.client_id == client_id), None)
        if not searched_client:
            raise Exception("No such client!")
        
        if searched_client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        
        self.clients.remove(searched_client)
        return f"Successfully removed {searched_client.name} with ID {searched_client.client_id}."
    
    def increase_loan_interest(self, loan_type: str) -> str:
        counter = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                counter += 1
        
        return f"Successfully changed {counter} loans."
    
    def increase_clients_interest(self, min_rate: float) -> str:
        counter = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                counter += 1
        
        return f"Number of clients affected: {counter}."
    
    def get_statistics(self) -> str:
        output: list[str] = [
            f"Active Clients: {len(self.clients)}",
            f"Total Income: {sum(client.income for client in self.clients):.2f}"
        ]
        
        granted_loans = [loan.amount for client in self.clients for loan in client.loans]
        output.append(f"Granted Loans: {len(granted_loans)}, Total Sum: {sum(granted_loans):.2f}")
        
        output.append(f"Available Loans: {len(self.loans)}, Total Sum: {sum(loan.amount for loan in self.loans):.2f}")
        
        client_interest = [client.interest for client in self.clients]
        avg_interest = 0
        if client_interest:
            avg_interest = sum(client_interest) / len(client_interest)
        
        output.append(f"Average Client Interest Rate: {avg_interest:.2f}")
        
        return "\n".join(output)
