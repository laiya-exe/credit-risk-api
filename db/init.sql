CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    cree_le TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    version_modele VARCHAR(50) NOT NULL,
    donnees JSONB NOT NULL,
    probabilite DOUBLE PRECISION CHECK (probabilite >= 0 AND probabilite <= 1) NOT NULL
);
