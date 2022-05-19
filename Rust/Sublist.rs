#[derive(Debug, PartialEq)]
pub enum Comparison {
    Equal,
    Sublist,
    Superlist,
    Unequal,
}

pub fn sublist<T: PartialEq>(_first_list: &[T], _second_list: &[T]) -> Comparison 
{
    if _first_list.len() == _second_list.len()
    {
        for i in 0.._first_list.len()
        {
            if _first_list[i] != _second_list[i]
            {
                return Comparison::Unequal;
            }
        }
        return Comparison::Equal;
    }
    else if _first_list.len() > _second_list.len()
    {
        list_test(_first_list, _second_list);
    }
    else if _second_list.len() > _first_list.len()
    {
        list_test(_second_list, _first_list);
    }
    return Comparison::Unequal;
}

pub fn list_test<T: PartialEq>(_listA: &[T], _listB: &[T]) -> bool
{
    let index = _listA.iter().position(|&x| x == _listB[0]);
    for i in 0.._listB.len()
    {
        if _listA[i+index] != _listB[i]
        {
            return Comparison::Unequal;
        }
    }
    r
}

