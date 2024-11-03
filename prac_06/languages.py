"""CP1404 Practical - Programming Language"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]
dynamic_languages = [language for language in languages if language.is_dynamic()]

print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
