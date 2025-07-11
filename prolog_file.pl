% Facts about animals
animal(ara, "Ara Parrot", "The Ara Parrot is an endangered species with brightly colored feathers.").
animal(white_stork, "White Stork", "The White Stork is an endangered species known for its long migration across continents.").
plant(red_oak, "Red Oak", "The Red Oak is a deciduous tree that is protected in some regions.").



% Facts about plants
plant(red_oak, "Red Oak", "The Red Oak is a deciduous tree that is protected in some regions.").

% General rules for providing information
information(animal, Name, Info) :- 
    animal(Name, _, Info).

information(plant, Name, Info) :- 
    plant(Name, _, Info).

% Mapping class to internal name (for different formats)
class_to_name("Ara Parrot", ara).
class_to_name("White Stork", white_stork).
class_to_name("Red Oak", red_oak).

% General rule for answering queries
answer(Class, Type, Answer) :-
    class_to_name(Class, InternalName),
    information(Type, InternalName, Answer).
