import importlib

def load_tool(tool_path: str):
    """Load a tool dynamically given its full path."""
    print(f"Processing tool path: {tool_path}")  # Debugging statement
    try:
        # Split the tool path to get module path, class name, and method name
        module_path, class_name, method_name = tool_path.rsplit('.', 2)
        
        # Import the module dynamically
        module = importlib.import_module(module_path)
        # Get the class from the module
        cls = getattr(module, class_name)
        # Get the method from the class
        return getattr(cls, method_name)
    except ValueError as e:
        raise ValueError(f"Error processing tool path '{tool_path}': {e}")
    except ImportError as e:
        raise ImportError(f"Module '{module_path}' could not be imported: {e}")
    except AttributeError as e:
        raise AttributeError(f"Class or method not found in '{tool_path}': {e}")

# Example usage
if __name__ == "__main__":
    tools_to_load = [
        'tools.searching.SearchTools.search_internet',
        'tools.calculating.CalculatorTools.calculate'
    ]
    for tool_path in tools_to_load:
        tool_function = load_tool(tool_path)
        print(f"Loaded tool: {tool_function}")