-- advanced SQL task
-- trigger a decrease in items
CREATE TRIGGER decrease_quantity AFTER INSERT ON orders FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
