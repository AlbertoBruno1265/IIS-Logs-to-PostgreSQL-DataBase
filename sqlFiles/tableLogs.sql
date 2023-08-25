CREATE TABLE IF NOT EXISTS tabelName
(
    id_log integer NOT NULL,
    id_datetime timestamp without time zone NOT NULL,
    date date,
    "time" time without time zone,
    s_ip text COLLATE pg_catalog."default",
    cs_method text COLLATE pg_catalog."default",
    cs_uri_stem text COLLATE pg_catalog."default",
    cs_uri_query text COLLATE pg_catalog."default",
    s_port integer,
    cs_username text COLLATE pg_catalog."default",
    cs_ip text COLLATE pg_catalog."default",
    c_user_agent text COLLATE pg_catalog."default",
    cs_refer text COLLATE pg_catalog."default",
    sc_status integer,
    sc_substatus integer,
    sc_win32_status integer,
    time_taken integer,
    CONSTRAINT logs_pkey PRIMARY KEY (id_log, id_datetime)
)
