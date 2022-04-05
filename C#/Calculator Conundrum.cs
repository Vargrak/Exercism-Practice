using System;

public static class SimpleCalculator
{
    public static string Calculate(int operand1, int operand2, string operation)
    {
        //catches div/0 error
        if (operand2 == 0 && operation == "/")
        {
            return "Division by zero is not allowed.";
        }

        int result = operation switch
        {
            "+" => operand1 + operand2,
            "*" => operand1 * operand2,
            "/" => operand1 / operand2,
            //error checking in switch
            null => throw new ArgumentNullException("null"), 
            _ when operation == string.Empty => throw new ArgumentException("empty"),
            _ => throw new ArgumentOutOfRangeException($"{operation} is not a valid operation")
        };

        return $"{operand1} {operation} {operand2} = {result.ToString()}";
    }
}
