using System;

public static class RotationalCipher
{
    public static string Cipher = "abcdefghijklmnopqrstuvwxyz";

    public static string CapitalCipher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public static string Rotate(string text, int shiftKey)
    {
        string result = "";
        foreach(char c in text)
        {
            if (char.IsUpper(c))
            {
                result += CapitalCipher[(CapitalCipher.IndexOf(c) + shiftKey) % 26];
            }
            else if (char.IsLower(c))
            {
                result += Cipher[(Cipher.IndexOf(c) + shiftKey) % 26];
            }
            else
            {
                result += c;
            }
        }
        return result;
    }
}