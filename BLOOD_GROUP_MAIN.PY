# ABO blood group predictor (without Rh factor)

# Step 1: Define ABO genotypes for each phenotype
# IA - A allele 
# IB - B allele
# i  - O allele 
# A and B is dominant allele and O is recessive allele
abo_genotypes = {
    "A": [["IA", "IA"], ["IA", "i"]],
    "B": [["IB", "IB"], ["IB", "i"]],
    "AB": [["IA", "IB"]],
    "O": [["i", "i"]]   
}

# Step 2: Function to get phenotype from genotype
def get_abo_phenotype(alleles):
    if "IA" in alleles and "IB" in alleles:
        return "AB"
    elif "IA" in alleles:
        return "A"
    elif "IB" in alleles:
        return "B"
    else:
        return "O"

# Step 3: Function to predict child blood groups (ABO only)
def predict_abo_offspring_groups(father, mother):
    father = father.upper()
    mother = mother.upper()

    if father not in abo_genotypes or mother not in abo_genotypes:
        return ["Invalid parent blood group"]

    possible = set()

    for g1 in abo_genotypes[father]:
        for g2 in abo_genotypes[mother]:
            # combine alleles (one from each parent)
            for a1 in g1:
                for a2 in g2:
                    phenotype = get_abo_phenotype([a1, a2])
                    possible.add(phenotype)

    return possible


# --- Example Run ---
father = input("Enter FATHER's blood group (A, B, AB, or O): ").strip().upper()
mother = input("Enter MOTHER's blood group (A, B, AB, or O): ").strip().upper()

possible_groups = predict_abo_offspring_groups(father, mother)

print("\nPossible offspring blood groups (ABO only): ")
print(", ".join(possible_groups))