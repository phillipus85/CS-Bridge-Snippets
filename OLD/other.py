def synonym_for(synonym_name, cls):
    def decorator(original_func):
        def wrapper(*args, **kwargs):
            return original_func(*args, **kwargs)
        setattr(cls, synonym_name, wrapper)
        return original_func
    return decorator


class Canvas:
    def draw(self):
        print("Drawing on canvas")


# Apply the decorator after the class definition
Canvas.draw = synonym_for('draw_synonym', Canvas)(Canvas.draw)

# Example usage
canvas = Canvas()
canvas.draw()         # Original function call
canvas.draw_synonym()  # Synonym function call
