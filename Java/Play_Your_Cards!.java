import java.util.HashMap;
import java.util.Map;

public class Blackjack 
{
    public Map<String, Integer> cards = new HashMap<String, Integer>(); 
    {
        cards.put("ace", 11);
        cards.put("two", 2);
        cards.put("three", 3);
        cards.put("four", 4);
        cards.put("five", 5);
        cards.put("six", 6);
        cards.put("seven", 7);
        cards.put("eight", 8);
        cards.put("nine", 9);
        cards.put("ten", 10);
        cards.put("jack", 10);
        cards.put("queen", 10);
        cards.put("king", 10);
    }
    

    public int parseCard(String card) 
    {
        if (cards.containsKey(card)) 
        {
            return cards.get(card);
        }
        return 0;
    }

    public boolean isBlackjack(String card1, String card2) 
    {
        if (cards.get(card1) + cards.get(card2) == 21)
        {
            return true;
        }
        return false;
    }

    public String largeHand(boolean isBlackjack, int dealerScore, String card1, String card2) 
    {
        if (card1 == "ace" && card2 == "ace") 
        {
            return "P";
        }
        else if (isBlackjack && dealerScore >= 10)
        {
            return "S";
        }
        else if (isBlackjack)
        {
            return "W";
        }
        else
        {
            return "H";
        }
    }

    public String smallHand(int handScore, int dealerScore) 
    {
        if (handScore >= 17)
        {
            return "S";
        }
        else if (handScore <= 11)
        {
            return "H";
        }
        else if (handScore >= 12 && handScore <= 16)
        {
            if (dealerScore >= 7)
            {
                return "H";
            }
            else
            {
                return "S";
            }
        }
        else
        {
            return "H";
        }

    }

    // FirstTurn returns the semi-optimal decision for the first turn, given the cards of the player and the dealer.
    // This function is already implemented and does not need to be edited. It pulls the other functions together in a
    // complete decision tree for the first turn.
    public String firstTurn(String card1, String card2, String dealerCard) 
    {
        int handScore = parseCard(card1) + parseCard(card2);
        int dealerScore = parseCard(dealerCard);

        if (20 < handScore) 
        {
            return largeHand(isBlackjack(card1, card2), dealerScore, card1, card2);
        } 
        else 
        {
            return smallHand(handScore, dealerScore);
        }
    }
}
