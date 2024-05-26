from langchain.tools import tool

class CaluculatorTools():

    @tool("Make a calculation")
    def calculate(operation):
        """Useful to perfom any mathematical calculations,
        like sum, minus, multiplication, division, etc.
        The input to this tool should be mathematical 
        experssion, a couple examples are '200*7' or '5000/2*10'.
        """

        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathemtical expression."