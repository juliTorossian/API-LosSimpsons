-- SQLite

DROP TABLE IF EXISTS personaje;
CREATE TABLE IF NOT EXISTS personaje(
    persId         integer PRIMARY KEY,
    persNombre     text
);
DROP TABLE IF EXISTS frase;
CREATE TABLE IF NOT EXISTS frase(
    fraseId         integer PRIMARY KEY,
    frase           text,
    persId          integer,
    FOREIGN KEY (persId) REFERENCES personaje(persId)
);

INSERT INTO personaje(persNombre)
VALUES  ('Homero Simpson'),
        ('Bart Simpson'),
        ('Marge Bouvier'),
        ('Helen Alegria'),
        ('Barney Gomez'),
        ('Abe Simpson'),
        ('Homero Bart Marge Simpson')
;

INSERT INTO frase(frase, persId)
VALUES  ('A la grande le puse Cuca.', 1),
        ('¡¿Alguien quiere pensar en los niños?!', 4),
        ('Tiene todo el dinero del mundo, pero hay algo que no puede comprar… Un dinosaurio.', 1),
        ('¡No vives de ensalada!', 7),
        ('¿Ah, si? ¿Y si era tan listo por qué se murió?', 1),
        ('Disimula y ve despacio hacia el pastel.', 1),
        ('¡Oh, no! ¡Elecciones! ¿Es uno de esos días en que cierran las tabernas, no es cierto?', 5),
        ('Vive deprisa, muere joven y deja un cadáver obeso.', 2),
        ('Mi Homero no es comunista. Podrá ser mentiroso, puerco, idiota, comunista, pero nunca una estrella de porno.', 6),
        ('Niños: Hicieron su esfuerzo y fracasaron miserablemente. La lección es: nunca se esfuercen.', 1)
;

SELECT * FROM personaje;
SELECT * FROM frase;

SELECT  fraseId,
        frase,
        personaje.persNombre
FROM frase
LEFT JOIN personaje ON frase.persId = personaje.persId;
