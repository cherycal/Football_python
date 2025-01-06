__author__ = 'chance'

from modules import tools


@tools.connection_check
def main():
	print(f"Hello world")


if __name__ == "__main__":
	main()
