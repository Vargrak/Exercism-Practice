#![allow(unused)]

use std::collections::HashMap;

pub fn can_construct_note(magazine: &[&str], note: &[&str]) -> bool
{
    // Create a HashMap of the magazine words
    let mut compare_map = HashMap::new();
    for word in magazine
    {
        // If word exists in the HashMap, increment the value
        if compare_map.contains_key(word)
        {
            *compare_map.get_mut(word).unwrap() += 1;
        }
        // Else, the (k, v) word, 1 is added
        else
        {
            compare_map.insert(word, 1);
        }
    }

    // Check if the note words are in the HashMap
    for word in note
    {
        // If the word is not in the HashMap, return false
        if !compare_map.contains_key(word)
        {
            return false;
        }
        else
        {   
            // If the word is in the HashMap, but only at 1, remove the word.
            if (*compare_map.get(word).unwrap() == 1)
            {
                compare_map.remove(word);
            }
            // Else, decrement the value of the word
            else
            {
                *compare_map.get_mut(word).unwrap() -= 1;
            }
        }
    }
    // If the for loop completes, return true
    return true;
}