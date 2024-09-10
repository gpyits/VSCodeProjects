--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4 (Debian 16.4-1.pgdg120+1)
-- Dumped by pg_dump version 16.4 (Debian 16.4-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: causaassenza; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.causaassenza AS ENUM (
    'Chiusura Universitaria',
    'Maternita',
    'Malattia'
);


ALTER TYPE public.causaassenza OWNER TO postgres;

--
-- Name: denaro; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.denaro AS integer DEFAULT 0
	CONSTRAINT denaro_check CHECK ((VALUE >= 0));


ALTER DOMAIN public.denaro OWNER TO postgres;

--
-- Name: lavorononprogettuale; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.lavorononprogettuale AS ENUM (
    'Didattica',
    'Ricerca',
    'Missione',
    'Incontro Dipartimentale',
    'Incontro Accademico',
    'Altro'
);


ALTER TYPE public.lavorononprogettuale OWNER TO postgres;

--
-- Name: lavoroprogetto; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.lavoroprogetto AS ENUM (
    'Ricerca e Sviluppo',
    'Dimostrazione',
    'Management',
    'Altro'
);


ALTER TYPE public.lavoroprogetto OWNER TO postgres;

--
-- Name: numeroore; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.numeroore AS integer DEFAULT 0
	CONSTRAINT numeroore_check CHECK (((VALUE >= 0) AND (VALUE <= 8)));


ALTER DOMAIN public.numeroore OWNER TO postgres;

--
-- Name: posinteger; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.posinteger AS integer DEFAULT 0
	CONSTRAINT posinteger_check CHECK ((VALUE >= 0));


ALTER DOMAIN public.posinteger OWNER TO postgres;

--
-- Name: stringam; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.stringam AS character varying(100);


ALTER DOMAIN public.stringam OWNER TO postgres;

--
-- Name: strutturato; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.strutturato AS ENUM (
    'Ricercatore',
    'Professore Associato',
    'Professore Ordinario'
);


ALTER TYPE public.strutturato OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: assenza; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.assenza (
    id public.posinteger NOT NULL,
    persona public.posinteger NOT NULL,
    tipo public.causaassenza NOT NULL,
    giorno date NOT NULL
);


ALTER TABLE public.assenza OWNER TO postgres;

--
-- Name: attivitanonprogettuale; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attivitanonprogettuale (
    id public.posinteger NOT NULL,
    persona public.posinteger NOT NULL,
    tipo public.lavorononprogettuale NOT NULL,
    giorno date NOT NULL,
    oredurata public.numeroore NOT NULL
);


ALTER TABLE public.attivitanonprogettuale OWNER TO postgres;

--
-- Name: attivitaprogetto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attivitaprogetto (
    id public.posinteger NOT NULL,
    persona public.posinteger NOT NULL,
    progetto public.posinteger NOT NULL,
    wp public.posinteger NOT NULL,
    giorno date NOT NULL,
    tipo public.lavoroprogetto NOT NULL,
    oredurata public.numeroore NOT NULL
);


ALTER TABLE public.attivitaprogetto OWNER TO postgres;

--
-- Name: persona; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.persona (
    id public.posinteger NOT NULL,
    nome public.stringam NOT NULL,
    cognome public.stringam NOT NULL,
    posizione public.strutturato NOT NULL,
    stipendio public.denaro NOT NULL
);


ALTER TABLE public.persona OWNER TO postgres;

--
-- Name: progetto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.progetto (
    id public.posinteger NOT NULL,
    nome public.stringam NOT NULL,
    inizio date NOT NULL,
    fine date NOT NULL,
    budget public.denaro NOT NULL,
    CONSTRAINT progetto_check CHECK ((fine > inizio))
);


ALTER TABLE public.progetto OWNER TO postgres;

--
-- Name: wp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.wp (
    progetto public.posinteger NOT NULL,
    id public.posinteger NOT NULL,
    nome public.stringam NOT NULL,
    inizio date NOT NULL,
    fine date NOT NULL,
    CONSTRAINT wp_check CHECK ((fine > inizio))
);


ALTER TABLE public.wp OWNER TO postgres;

--
-- Data for Name: assenza; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.assenza (id, persona, tipo, giorno) FROM stdin;
\.


--
-- Data for Name: attivitanonprogettuale; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attivitanonprogettuale (id, persona, tipo, giorno, oredurata) FROM stdin;
\.


--
-- Data for Name: attivitaprogetto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attivitaprogetto (id, persona, progetto, wp, giorno, tipo, oredurata) FROM stdin;
\.


--
-- Data for Name: persona; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.persona (id, nome, cognome, posizione, stipendio) FROM stdin;
\.


--
-- Data for Name: progetto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.progetto (id, nome, inizio, fine, budget) FROM stdin;
\.


--
-- Data for Name: wp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.wp (progetto, id, nome, inizio, fine) FROM stdin;
\.


--
-- Name: assenza assenza_persona_giorno_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assenza
    ADD CONSTRAINT assenza_persona_giorno_key UNIQUE (persona, giorno);


--
-- Name: assenza assenza_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assenza
    ADD CONSTRAINT assenza_pkey PRIMARY KEY (id);


--
-- Name: attivitanonprogettuale attivitanonprogettuale_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attivitanonprogettuale
    ADD CONSTRAINT attivitanonprogettuale_pkey PRIMARY KEY (id);


--
-- Name: attivitaprogetto attivitaprogetto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attivitaprogetto
    ADD CONSTRAINT attivitaprogetto_pkey PRIMARY KEY (id);


--
-- Name: persona persona_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.persona
    ADD CONSTRAINT persona_pkey PRIMARY KEY (id);


--
-- Name: progetto progetto_nome_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.progetto
    ADD CONSTRAINT progetto_nome_key UNIQUE (nome);


--
-- Name: progetto progetto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.progetto
    ADD CONSTRAINT progetto_pkey PRIMARY KEY (id);


--
-- Name: wp wp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.wp
    ADD CONSTRAINT wp_pkey PRIMARY KEY (id, progetto);


--
-- Name: wp wp_progetto_nome_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.wp
    ADD CONSTRAINT wp_progetto_nome_key UNIQUE (progetto, nome);


--
-- Name: assenza assenza_persona_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assenza
    ADD CONSTRAINT assenza_persona_fkey FOREIGN KEY (persona) REFERENCES public.persona(id);


--
-- Name: attivitanonprogettuale attivitanonprogettuale_persona_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attivitanonprogettuale
    ADD CONSTRAINT attivitanonprogettuale_persona_fkey FOREIGN KEY (persona) REFERENCES public.persona(id);


--
-- Name: attivitaprogetto attivitaprogetto_persona_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attivitaprogetto
    ADD CONSTRAINT attivitaprogetto_persona_fkey FOREIGN KEY (persona) REFERENCES public.persona(id);


--
-- Name: attivitaprogetto attivitaprogetto_progetto_wp_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attivitaprogetto
    ADD CONSTRAINT attivitaprogetto_progetto_wp_fkey FOREIGN KEY (progetto, wp) REFERENCES public.wp(progetto, id);


--
-- Name: wp wp_progetto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.wp
    ADD CONSTRAINT wp_progetto_fkey FOREIGN KEY (progetto) REFERENCES public.progetto(id);


--
-- PostgreSQL database dump complete
--

