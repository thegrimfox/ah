animal(coyote).
animal(elefante).
animal(pudu).
animal(oso).
animal(panda).
animal(guacamayo).
animal(lobo).
animal(rinoceronte).
animal(dragon_de_comodo).
animal(carpincho).

mas_grande(elefante, rinoceronte).
mas_grande(rinoceronte, oso).
mas_grande().
mas_grande().
mas_grande().
mas_grande().
mas_grande().

mas_grande(A1, A2):- mas_grande(A1, X), mas_grande(X, A2)