using System;
namespace project;

public enum TypeAccountEnum {Saving,Checking,Business};
class BankAccount
{
    private string? _accountType;
    public string? accountType
    {
        get => _accountType;
        set
        {
            if (string.Equals(value,TypeAccountEnum.Saving.ToString(), StringComparison.OrdinalIgnoreCase) || string.Equals(value,TypeAccountEnum.Checking.ToString(), StringComparison.OrdinalIgnoreCase) || string.Equals(value,TypeAccountEnum.Business.ToString(), StringComparison.OrdinalIgnoreCase))
            {
                _accountType = value.ToString();
            }
            else _accountType = TypeAccountEnum.Checking.ToString();
        }
    }
    private int _accountNumber
        { get; }
    
    private string _ownerName;
    public string ownerName {
        get => _ownerName;
        set
        {
            if (!string.IsNullOrEmpty(value.Trim())) {
                _ownerName = value.Trim();
            }
            else _ownerName = "Unknon";
        }
    }
        
    private double _balance;
    public double balance
    {
        get => _balance;
        set
        {
            if (value < 0)
                _balance = 0;
            else
                _balance = value;
        }
    }

    private bool _IsActive;
    public bool IsActive
    {
        get => _IsActive;
        set
        {
            _IsActive = value;
        }
    }

    private List<string> transactionHistory;

    public void Deactivate()
    {
        IsActive = false;
    }
    public void Activate()
    {
        IsActive = true;
    }
    public BankAccount(int numberAccount, string nameOwner, double newBalance, string typeAccount,bool active=true) {
        accountType = typeAccount;
        _accountNumber = numberAccount;
        ownerName = nameOwner;
        balance = newBalance;
        IsActive = active;
        Console.WriteLine("constractor run");
    }
    public BankAccount(int numberAccount, string nameOwner) 
        : this(numberAccount, nameOwner, 0.0, "Checking", false) { }
    public override string ToString()
    => $"The id is:{_accountNumber}| OnwerName: {_ownerName}| Balance: {_balance:0.##}| BankAccount {_accountType}| is active {_IsActive}";
    public void Deposit(double amount)
    {
        if (amount > 0)
        {
            balance += amount;
            transactionHistory.Add($"Deposit {amount}");
        }
        else
        {
            Console.WriteLine("Error: deposit amount should be positive");
        }
    }
    public bool Withdraw(double amount)
    {
        if (amount < 0||balance-amount<0) {
            Console.WriteLine("Error: cannot withdraw more than have");
            return false;
        }
        balance -= amount;
        transactionHistory.Add($"Withdraw {amount}");
        return true;
    }
    public void ApplyInerest()
    {
        if(!string.Equals(accountType, TypeAccountEnum.Saving.ToString(), StringComparison.OrdinalIgnoreCase))
        {
            return;
        }
        double interestAmount = balance * 0.02;
        balance += interestAmount;
    }
    public void PrintTransactionHistory()
    {
        foreach(string i in transactionHistory)
        {
            Console.WriteLine(i);
        }
    }
    public static bool Transfer(BankAccount from, BankAccount to,double amount) {
        if (amount <= 0)
        {
            Console.WriteLine("Error: Transfer amount must be positive");
            return false;
        }
        if (!from.IsActive || !to.IsActive)
        {
            Console.WriteLine("Error: Both accounts must be active to perform a transfer");
            return false;
        }
        if (from.Withdraw(amount))
        {
            to.Deposit(amount);
            Console.WriteLine($"Successfully transferred {amount} from {from.ownerName} to {to.ownerName}");
            return true;
        }
        return false;
    }
}

class main()
{
    static void Main()
    {
        BankAccount a = new BankAccount(1, "pesach",100,"saving",true);
        BankAccount b = new BankAccount(1, "pesach", 100, "saving", true);
        BankAccount c = new BankAccount(1, "pesach", 100, "saving", true);
        BankAccount d = new BankAccount(1, "pesach", 100, "saving", true);
        BankAccount e = new BankAccount(1, "pesach", 100, "saving", true);
        List<BankAccount> listAccount = new List<BankAccount>();
        listAccount.Add(a);

        Console.WriteLine($"{a}");
    }
}