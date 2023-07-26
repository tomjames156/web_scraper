import re

languagesRegex = re.compile(r'html5|css3|react|js|sass')

sampleSoup = """<div class="languages">
<i class="fa-brands fa-html5"></i>
<i class="fa-brands fa-css3-alt"></i>
<i class="fa-brands fa-square-js"></i>
<i class="fa-brands fa-react"></i>
<i class="fa-brands fa-sass"></i>
</div>"""

abbr_languages = ['html5', 'css3', 'sass']

def get_languages_list(html_text):
    """Gets the languages used to build the project based on the icon used and returns them as a list"""

    languages_used = languagesRegex.findall(html_text)
    languages_used = [language.upper() if language in abbr_languages else language.title() for language in languages_used]
    languages_used = ['JavaScript' if language == 'Js' else language for language in languages_used]

    return languages_used

def get_languages_sentence(html_text):
    """This is a function that lists the languages used to build the project"""
    languages_list = get_languages_list(html_text)
    final = languages_list.pop()
    shortened_list = languages_list
    languages_sentence = ''
    for language in shortened_list:
        languages_sentence += f"{language}, "
    
    languages_sentence += f"and {final}."

    return languages_sentence


def get_languages_str(html_text):
    "Returns a str of languages used separated by commas"
    languages_list = get_languages_list(html_text)
    final = languages_list.pop()
    shortened_list = languages_list
    languages_str = ''
    for language in shortened_list:
        languages_str += f"{language}, "
    
    languages_str += f"{final}"

    return languages_str


print(get_languages_str("""<div class="languages">
<i class="fa-brands fa-html5"></i>
<i class="fa-brands fa-css3-alt"></i>
<i class="fa-brands fa-square-js"></i>
</div>"""))
