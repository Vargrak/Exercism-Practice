use std::collections::HashSet;
use std::collections::HashMap;

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> 
{
    let mut original_word_map = HashMap::new();
    for c in word.to_lowercase().chars()
    { 
        if original_word_map.contains_key(&c)
        {
            *original_word_map.get_mut(&c).unwrap() += 1;
        }
        else
        {
            original_word_map.insert(c, 1);
        }
    }

    let mut result = HashSet::new();
    for possible_anagram in possible_anagrams
    {
        let mut possible_anagram_map = HashMap::new();
        for c in possible_anagram.to_lowercase().chars()
        {
            if possible_anagram_map.contains_key(&c)
            {
                *possible_anagram_map.get_mut(&c).unwrap() += 1;
            }
            else
            {
                possible_anagram_map.insert(c, 1);
            }
        }

        if original_word_map == possible_anagram_map
        {
            if possible_anagram.to_lowercase() != word.to_lowercase()
            {
                result.insert(*possible_anagram);
            }
        }
    }
    return result;
}
