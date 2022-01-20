protein_dict = {("AUG"):"Methionine",
                ("UUU", "UUC"):"Phenylalanine",
                ("UUA", "UUG"):"Leucine",
                ("UCU", "UCC", "UCA", "UCG"):"Serine",
                ("UAU", "UAC"):"Tyrosine",
                ("UGU", "UGC"):"Cysteine",
                ("UGG"):"Tryptophan",
                ("UAA", "UAG", "UGA"): "STOP"}

def proteins(strand):
    protein_list = []
    RNA_list = [strand[i:i+3] for i in range(0, len(strand), 3)]

    for group in RNA_list:
        protein = [protein_dict[key] for key in protein_dict if group in key]
        if protein == ["STOP"]:
            break
        else:
            protein_list += protein
    return protein_list