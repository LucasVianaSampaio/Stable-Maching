def stableMatching(n, menPreferences, womenPreferences):
    # Inicializar homens solteiros
    freeMen = set(range(n))
    # Inicializar cônjuges dos homens e mulheres como None
    manSpouse = [-1] * n
    womanSpouse = [-1] * n
    # Próxima mulher que cada homem vai propor
    proposalCount = [0] * n

    while freeMen:
        # Escolher um homem solteiro (agora usando set)
        man = freeMen.pop()
        # Mulher para quem o homem vai propor
        womanIndex = menPreferences[man][proposalCount[man]]
        proposalCount[man] += 1

        # Marido atual da mulher (se ela estiver casada)
        currentPartner = womanSpouse[womanIndex]

        if currentPartner == -1:
            # Se a mulher estiver solteira, aceitar a proposta
            womanSpouse[womanIndex] = man
            manSpouse[man] = womanIndex
        else:
            # Comparar o atual parceiro com o novo pretendente
            herPref = womenPreferences[womanIndex]
            if herPref.index(man) < herPref.index(currentPartner):
                # Se ela preferir o novo pretendente, trocá-los
                womanSpouse[womanIndex] = man
                manSpouse[man] = womanIndex
                freeMen.add(currentPartner)
            else:
                # Se ela preferir o atual, o homem continua solteiro
                freeMen.add(man)

    return manSpouse

menPreferences = [
    [0, 1, 2],
    [2, 1, 0],
    [0, 2, 1]
]

womenPreferences = [
    [1, 0, 2],
    [2, 0, 1],
    [0, 1, 2]
]

n = len(menPreferences)
print(stableMatching(n, menPreferences, womenPreferences))  # Saída esperada = [0, 2, 1]
