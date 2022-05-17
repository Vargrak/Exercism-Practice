
#[derive(Debug)]
pub enum CalculatorInput 
{
    Add,
    Subtract,
    Multiply,
    Divide,
    Value(i32),
}

pub fn evaluate(inputs: &[CalculatorInput]) -> Option<i32> 
{
    // Create stack and iterate over inputs
    let mut stack: Vec<i32> = Vec::new();
    for input in inputs
    {
        // If input is a value, push to stack
        if let CalculatorInput::Value(value) = input
        {
            stack.push(*value);
        }
        //Operators condition
        else
        {
            // If too few variables, return None
            if stack.len() < 2
            {
                return None;
            }
            //Assign variables and perform operation
            let x = stack.pop().unwrap();
            let y = stack.pop().unwrap();
            match input
            {
                CalculatorInput::Add => stack.push(y + x),
                CalculatorInput::Subtract => stack.push(y - x),
                CalculatorInput::Multiply => stack.push(y * x),
                CalculatorInput::Divide => stack.push(y / x),
                _ => return Option::None,
            }
        }
    }

    // If stack cannot return single result, return None
    if stack.len() == 1
    {
        return Option::Some(stack.pop().unwrap());
    }
    Option::None
}
