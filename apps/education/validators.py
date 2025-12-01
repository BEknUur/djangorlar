def indentation_validator(indention:int)->None:
    if indention>5 or indention<0:
        raise ValueError("indention must be between 0 and 5")