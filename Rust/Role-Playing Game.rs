// This stub file contains items that aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

pub struct Player {
    pub health: u32,
    pub mana: Option<u32>,
    pub level: u32,
}

impl Player {
    pub fn revive(&self) -> Option<Player> 
    {
        if self.level > 9 
        {
            match self.health
            {
                0 => Some(Player { health: 100, mana: Some(100), level: self.level }),
                _ => None,
            }
        }
        else 
        {
            match self.health
            {
                0 => Some(Player { health: 100, mana: None, level: self.level }),
                _ => None,
            }
        }
    }


    pub fn cast_spell(&mut self, mana_cost: u32) -> u32 
    {
        if self.level > 9
        {
            if self.mana.unwrap() >= mana_cost
            {
                self.mana = Some(self.mana.unwrap() - mana_cost);
                return mana_cost * 2;
            }
            return 0;
        }
        if self.health < mana_cost
        {
            self.health = 0;
        }
        else
        {
            self.health = self.health - mana_cost;
        }
        return 0;
    }
}
