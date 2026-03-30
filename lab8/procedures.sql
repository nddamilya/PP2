-- procedures.sql

-- Удаляем старые процедуры
DROP PROCEDURE IF EXISTS upsert_contact(VARCHAR, VARCHAR);
DROP PROCEDURE IF EXISTS insert_single_contact(VARCHAR, VARCHAR);
DROP PROCEDURE IF EXISTS insert_bulk_contacts(TEXT[], TEXT[]);
DROP PROCEDURE IF EXISTS delete_contact_v8(TEXT);

-- Процедура для вставки или обновления одного контакта
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE username = p_name;
    ELSE
        INSERT INTO phonebook(username, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

-- Процедура для вызова вставки одного контакта из Python
CREATE OR REPLACE PROCEDURE insert_single_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    CALL upsert_contact(p_name, p_phone);
END;
$$;

-- Процедура массовой вставки (через массивы)
CREATE OR REPLACE PROCEDURE insert_bulk_contacts(p_names TEXT[], p_phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        CALL upsert_contact(p_names[i], p_phones[i]);
    END LOOP;
END;
$$;

-- Процедура удаления контакта по имени или телефону
CREATE OR REPLACE PROCEDURE delete_contact_v8(p_val TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook WHERE username = p_val OR phone = p_val;
END;
$$;