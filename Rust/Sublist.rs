#[derive(Debug, PartialEq)]
pub enum Comparison {
    Equal,
    Sublist,
    Superlist,
    Unequal,
}

pub fn sublist<T: PartialEq>(_first_list: &[T], _second_list: &[T]) -> Comparison 
{
    // If the first list is equal length to the second list, check if they are equal
    if _first_list.len() == _second_list.len()
    {
        //Iter through each item in the lists
        for i in 0.._first_list.len()
        {
            //If any item is not equal, return unequal
            if _first_list[i] != _second_list[i]
            {
                return Comparison::Unequal;
            }
        }
        return Comparison::Equal;
    }
    //If the first list is longer, then pass the first list as the superlist to A_superlist_of_B
    else if _first_list.len() > _second_list.len()
    {
        //If A is a superlist, return superlist
        if A_superlist_of_B(_first_list, _second_list) == true
        {
            return Comparison::Superlist;
        }
    }
    //Else if second list is longer, pass it as A
    else if _second_list.len() > _first_list.len()
    {
        if A_superlist_of_B(_second_list, _first_list) == true
        {
            return Comparison::Sublist;
        }
    }
    //If none of the above, return unequal
    return Comparison::Unequal;
}

pub fn A_superlist_of_B<T: PartialEq>(_listA: &[T], _listB: &[T]) -> bool
{
    //Grabs the index position of the first item from the second list, where it occurs in the first list
    let index = _listA.iter().position(|x| x == &_listB[0]).unwrap();
    //Iter-Equality check like above
    for i in 0.._listB.len()
    {
        if _listA[i+index] != _listB[i]
        {
            //If any item is not equal, but there is more to check, recursively calls itself
            let (left, right) = _listA.split_at(index);
            if right.len() > _listB.len()
            {
                return A_superlist_of_B(right , _listB)
            }
            return false;
        }
    }
    return true;
}
