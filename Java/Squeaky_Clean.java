class SqueakyClean
{
    static String clean(String identifier)
    {
        StringBuilder returnString = new StringBuilder();
        int i;

        for (i=0; i < identifier.length(); i++)
        {
            Character text = identifier.charAt(i);
            if(Character.isWhitespace(text))
            {
                returnString.append('_');
                continue;
            }
            else if (Character.isISOControl(text))
            {
                returnString.append("CTRL");
                continue;
            }
            else if (text == '-')
            {
                returnString.append(identifier.toUpperCase().charAt(i+1));
                i = i + 1;
                continue;
            }
            else if(!Character.isLetter(text))
            {
                continue;
            }
            else if(text >= 'α' && text <= 'ω')
            {
                continue;
            }
            else
            {
                returnString.append(text);
            }
        }
        return returnString.toString();
    }
}