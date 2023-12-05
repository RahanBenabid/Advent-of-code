match in re.finditer(pattern, line, re.IGNORECASE):
            if any(re.search(patternb, match.group(), re.IGNORECASE) for patternb in patternsb):
                matches.append