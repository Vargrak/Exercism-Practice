using System;
using System.Collections.Generic;

public class FacialFeatures
{
    public string EyeColor { get; }
    public decimal PhiltrumWidth { get; }

    public FacialFeatures(string eyeColor, decimal philtrumWidth)
    {
        EyeColor = eyeColor;
        PhiltrumWidth = philtrumWidth;
    }

    public bool Equals(FacialFeatures other) => (EyeColor == other.EyeColor) && (PhiltrumWidth == other.PhiltrumWidth);

    public int GetHashCode() => EyeColor.GetHashCode() + PhiltrumWidth.GetHashCode();
}

public class Identity
{
    public string Email { get; }
    public FacialFeatures FacialFeatures { get; }

    public Identity(string email, FacialFeatures facialFeatures)
    {
        Email = email;
        FacialFeatures = facialFeatures;
    }

    public bool Equals(Identity other) => (Email == other.Email) && (FacialFeatures.Equals(other.FacialFeatures));

    public int GetHashCode() => Email.GetHashCode() + FacialFeatures.GetHashCode();
}

public class Authenticator
{
    HashSet<int> RegistrationTable = new HashSet<int>();

    public static bool AreSameFace(FacialFeatures faceA, FacialFeatures faceB) => faceA.Equals(faceB);

    public bool IsAdmin(Identity identity) => identity.Equals(new Identity("admin@exerc.ism", new FacialFeatures("green", 0.9m)));

    public bool Register(Identity identity) => RegistrationTable.Add(identity.GetHashCode());

    public bool IsRegistered(Identity identity) => RegistrationTable.Contains(identity.GetHashCode());

    public static bool AreSameObject(Identity identityA, Identity identityB) => identityA == identityB;
}
