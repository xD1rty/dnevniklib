import setuptools

# Открытие README.md и присвоение его long_description.
with open("README.md", "r") as fh:
	long_description = fh.read()

# Определение requests как requirements для того, чтобы этот пакет работал. Зависимости проекта.
requirements = ["requests<=2.21.0"]

# Функция, которая принимает несколько аргументов. Она присваивает эти значения пакету.
setuptools.setup(
	name="dnevniklib",
	version="0.8",
	author="Ivan Kriventsev",
	author_email="dirtyhornet277@outlook.com",
	description="lib for automatization work with dnevnik mos",

	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/dirtyhornet277/dnevniklib",
	packages=setuptools.find_packages(),
	classifiers=[
	],
	python_requires='>=3.6',
)
