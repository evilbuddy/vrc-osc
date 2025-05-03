def str_replace(text, search, replace):
    return text.replace(str(search), str(replace))

def str_replace_bulk(text, dictionary):
    for search, replace in dictionary.items():
        text = str_replace(text, "{" + search + "}", replace)

    return text

if __name__ == "__main__":
    print("You are not supposed to run this file !")
    print("This is to be imported to build modules for vrc-osc")
