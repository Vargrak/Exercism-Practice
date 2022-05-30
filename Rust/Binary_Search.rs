//Entry Function for exercise
pub fn find(array: &[i32], key: i32) -> Option<usize> 
{
    /* Match checks the original input for validity. In order:
    Empty list; first element equals key; single element list; last element less than key; first element greater than key; assign split list*/
    let (first, second) = match key
    {
        _ if array == [] => return None,
        _ if key == array[0] => return Some(0),
        _ if array.len() == 1 => return None,
        _ if array[array.len() - 1] < key => return None,
        _ if array[0] > key => return None,
        _ => array.split_at(array.len()/2),
    };

    //Match checks last element of first slice. If key is less than or equal to key, call search with the first slice, else call search with the second slice
    return match key
    {
        _ if first[first.len() - 1] >= key => search(first, key, 0),
        _ => search(second, key, first.len() as i32),
    };
}

//Actual search loop. Continually calls itself until the array is reduce to single element or the key index is found. index_tracker is the length of the first list and added to if the second list is called.
pub fn search(array: &[i32], key: i32, mut index_tracker: i32) -> Option<usize>
{
    let (first, second) = match key
    {
        _ if array.len() == 1 && key == array[0] => return Some(index_tracker as usize),
        _ if array.len() == 1 => return None,
        _ => array.split_at(array.len()/2),
    };

    return match key
    {
        _ if first[first.len() - 1] >= key => search(first, key, index_tracker),
        _ => search(second, key, index_tracker + first.len() as i32),
    };
}