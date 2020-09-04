-- advanced SQL task
-- trigger a valid email reset
CREATE TRIGGER reset_valid_email BEFORE UPDATE ON users FOR EACH ROW IF NEW.email <> OLD.email UPDATE users SET valid_email = 0 WHERE email = NEW.email;
