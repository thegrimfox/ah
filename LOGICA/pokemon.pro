%pokemones
pokemon(eevee,[normal, nill]).
pokemon(flareon, [fuego, nill]).
pokemon(vaporeon, [agua, nill]).
pokemon(jolteon, [electrico, nill]).
pokemon(espeon, [psiquico, nill]).
pokemon(umbreon, [siniestro, nill]).
pokemon(leafeon, [planta, nill]).
pokemon(glaceon, [hielo, nill]).
pokemon(sylveon, [hada, nill]).
pokemon(paras, [insecto, planta]).
pokemon(magnemite, [electrico, acero]).
pokemon(haunter, [fantasma, veneno]).
pokemon(castform, [normal, nill]).
pokemon(duskull, [fantasma, nill]).
pokemon(lucario, [lucha, acero]).
pokemon(regirock, [roca, nill]).
pokemon(metagross, [acero, psiquico]).
pokemon(raycuasa, [dragon, volador]).
pokemon(spoink, [psiquico, nill]).
pokemon(scizor, [bicho, acero]).
pokemon(gardevoir, [psiquico, hada]).
pokemon(torchic, [fuego, nill]).
pokemon(zigzagoon, [normal, nill]).
pokemon(cascoon,[ bicho, nill]).
pokemon(psyduck, [agua, nill]).
pokemon(taillow, [normal, volador]).
pokemon(makuhita, [lucha, nill]).
pokemon(sableye, [siniestro, fantasma]).
pokemon(aggron, [acero, roca]).
pokemon(electrike, [electrico, nill]).
pokemon(roselia, [planta, veneno]).
pokemon(sandslash,[ tierra, nill]).

% ventaja de tipo (A le gana a B)
efectivo(acero, hada).
efectivo(acero, hielo).
efectivo(acero, tierra).
efectivo(agua, fuego).
efectivo(agua, roca).
efectivo(agua, tierra).
efectivo(bicho, planta).
efectivo(bicho, psiquico).
efectivo(bicho, siniestro).
efectivo(dragon, dragon).
efectivo(electrico, agua).
efectivo(electrico, volador).
efectivo(fantasma, fantasma).
efectivo(fantasma, psiquico).
efectivo(fuego, acero).
efectivo(fuego, bicho).
efectivo(fuego, hielo).
efectivo(fuego, planta).
efectivo(hada, dragon).
efectivo(hada, lucha).
efectivo(hada, siniestro).
efectivo(hielo, planta).
efectivo(hielo, dragon).
efectivo(hielo, tierra).
efectivo(hielo, volador).
efectivo(lucha, acero).
efectivo(lucha, hielo).
efectivo(lucha, normal).
efectivo(lucha, roca).
efectivo(lucha, siniestro).
efectivo(planta, agua).
efectivo(planta, roca).
efectivo(planta, tierra).
efectivo(psiquico, lucha).
efectivo(psiquico, veneno).
efectivo(roca, fuego).
efectivo(roca, bicho).
efectivo(roca, hielo).
efectivo(roca, volador).
efectivo(siniestro, fantasma).
efectivo(siniestro, psiquico).
efectivo(tierra, acero).
efectivo(tierra, electrico).
efectivo(tierra, roca).
efectivo(tierra, veneno).
efectivo(tierra, fuego).
efectivo(veneno, planta).
efectivo(veneno, hada).
efectivo(volador, bicho).
efectivo(volador, planta).
efectivo(volador, lucha).

% sin ventaja de tipo (C no tiene ventaja contra D)
ineficaz(acero, acero).
ineficaz(acero, agua).
ineficaz(acero, electrico).
ineficaz(acero, fuego).
ineficaz(agua, agua).
ineficaz(agua, dragon).
ineficaz(agua, planta).
ineficaz(bicho, acero).
ineficaz(bicho, fantasma).
ineficaz(bicho, hada).
ineficaz(bicho, fuego).
ineficaz(bicho, lucha).
ineficaz(bicho, veneno).
ineficaz(bicho, volador).
ineficaz(dragon, acero).
ineficaz(dragon, hada).
ineficaz(electrico, dragon).
ineficaz(electrico, electrico).
ineficaz(electrico, planta).
ineficaz(electrico, tierra).
ineficaz(fantasma, siniestro).
ineficaz(fantasma, normal).
ineficaz(fuego, agua).
ineficaz(fuego, dragon).
ineficaz(fuego, fuego).
ineficaz(fuego, hielo).
ineficaz(hada, acero).
ineficaz(hada, fuego).
ineficaz(hada, veneno).
ineficaz(hielo, acero).
ineficaz(hielo, agua).
ineficaz(hielo, fuego).
ineficaz(hielo, hielo).
ineficaz(lucha, bicho).
ineficaz(lucha, hada).
ineficaz(lucha, psiquico).
ineficaz(lucha, veneno).
ineficaz(lucha, volador).
ineficaz(lucha, fantasma).
ineficaz(normal, acero).
ineficaz(normal, roca).
ineficaz(normal, fantasma).
ineficaz(planta, acero).
ineficaz(planta, bicho).
ineficaz(planta, dragon).
ineficaz(planta, fuego).
ineficaz(planta, planta).
ineficaz(planta, veneno).
ineficaz(planta, volador).
ineficaz(psiquico, acero).
ineficaz(psiquico, psiquico).
ineficaz(psiquico, siniestro).
ineficaz(roca, acero).
ineficaz(roca, lucha).
ineficaz(roca, tierra).
ineficaz(roca, roca).
ineficaz(siniestro, hada).
ineficaz(siniestro, lucha).
ineficaz(siniestro, siniestro).
ineficaz(tierra, bicho).
ineficaz(tierra, planta).
ineficaz(tierra, volador).
ineficaz(veneno, fantasma).
ineficaz(veneno, roca).
ineficaz(veneno, tierra).
ineficaz(veneno, veneno).
ineficaz(veneno, acero).
ineficaz(acero, electrico).
ineficaz(acero, electrico).
ineficaz(acero, roca).

%reglas de combate

%registro de lista
equipo(X, [X|_]).
equipo(X, [_|Banca]) :- equipo(X, Banca).

%efectivo contra pokemon A
eficiente(Tipos_de_X, Tipos_de_Y) :- 
    equipo(Tipo_X, Tipos_de_X), 
    equipo(Tipo_Y, Tipos_de_Y), 
    efectivo(Tipo_X,Tipo_Y).

%ineficaz contra pokemon A
ineficiente(Tipos_de_X, Tipos_de_Y):- 
    \+ (equipo(Tipo_X,Tipos_de_X), 
    equipo(Tipo_Y,Tipos_de_Y), 
    ineficaz(Tipo_X,Tipo_Y)).

%mi pokemon gana o no
vencer(Pokemon_X, Pokemon_Y) :- 
    pokemon(Pokemon_X, Tipos_de_X),
    pokemon(Pokemon_Y, Tipos_de_Y), eficiente(Tipos_de_X, Tipos_de_Y),
    ineficiente(Tipos_de_X, Tipos_de_Y).

%rival(nombre_rival, [pokemon_X, pokemon_Y, pokemon_Z]).
rival(roger,[castform, flareon, lucario]).
rival(juana,[raycuasa, aggron, gardevoir]).
rival(lopez,[duskull, regirock, taillow]).
rival(emma, [eevee, glaceon, umbreon]).
rival(sofia,[vaporeon, magnemite, haunter]).
rival(hugo, [lucario, metagross, zigzagoon]).

%seleccion de pokemon y empezar pelea
batalla(Oponente, Pokemon_jugador) :- 
    rival(Oponente, Pokemon_rival),
    writeln("Pokemon del jugador: "), writeln(Pokemon_jugador),
    write("Pokemon de "), write(Oponente), writeln(":"),
    writeln(Pokemon_rival),
    pelea(Pokemon_jugador, Pokemon_rival).

%realizacion del combate
pelea([], _) :- 
    writeln("Has sido derrotado.").
pelea(_, []) :- 
    writeln("has ganado la batalla.").
pelea([P1|Banca1], [P2|Banca2]) :- 
    (vencer(P1,P2) -> write(P1), write(" derrota a "), writeln(P2), pelea([P1|Banca1], Banca2);
    vencer(P2, P1) -> write(P2), write(" derrota a "), writeln(P1), pelea(Banca1, [P2|Banca2]);
    write(P1), write(" y "), write(P2), writeln(" empatan "), pelea(Banca1, Banca2)).

%ejecutar duelo pokémon
hora_del_duelo(Oponente, Pokemon_jugador) :- 
    rival(Oponente, _), 
    batalla(Oponente, Pokemon_jugador).

%seleccion de Oponente
elige_rival(Oponente) :- 
    writeln("elige con quien quieres pelear: roger, juana, lopez, emma, sofia, hugo"),
    read(Oponente).

%seleccionar pokemons
pokemon_ve(Pokemon_jugador) :- 
    writeln("elige los pokemon con los que lucharas (ejemplo: [flareon, vaporeon, jolteon]): "),
    read(Pokemon_jugador).

%inicia el combate
iniciar_combate :- 
    elige_rival(Oponente),
    pokemon_ve(Pokemon_jugador),
    hora_del_duelo(Oponente, Pokemon_jugador).