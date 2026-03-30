-- functions.sql

-- Удаляем старые функции
DROP FUNCTION IF EXISTS get_contacts_by_pattern(TEXT);
DROP FUNCTION IF EXISTS get_phonebook_paged(INT, INT);

-- Функция поиска контактов по шаблону
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(pattern TEXT)
RETURNS TABLE(id INT, username VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT t.id, t.username, t.phone
    FROM phonebook AS t
    WHERE t.username ILIKE '%' || pattern || '%'
       OR t.phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- Функция пагинации контактов
CREATE OR REPLACE FUNCTION get_phonebook_paged(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, username VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT t.id, t.username, t.phone
    FROM phonebook AS t
    ORDER BY t.username
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;