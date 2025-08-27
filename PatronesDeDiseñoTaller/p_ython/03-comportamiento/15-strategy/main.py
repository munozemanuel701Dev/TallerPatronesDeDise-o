from context import PaymentProcessor
from strategy import FixedCommission
from strategy import PercentegeCommission

def main():
    
    processor = PaymentProcessor(FixedCommission())
    print(processor.process_payment(100))
    
    processor = PaymentProcessor(PercentegeCommission())
    print(processor.process_payment(100))
    
if __name__ == "__main__":
    main()