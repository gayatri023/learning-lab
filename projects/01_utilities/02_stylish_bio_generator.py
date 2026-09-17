import textwrap

name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter your passion in one line: ").strip()
emoji = input("Enter your fabvourite emoji: ").strip()
website = input("Enter your website: ").strip()

print("\nChoose your style: ")
print("1. Simple lines. ")
print("2. Vertical flair. ")
print("3. Emoji sandwich ")

style = input("Enter 1, 2 or 3: ").strip()

def generate_bio(Style):
	if style == "1":
		return f"{emoji} {name} | {profession} \n💡 {passion} \n {website}"
	elif style == "2":
		return f"{emoji} {name}\n {profession}🔥\n {passion} \n {website}🔥"
	elif style == "3":
		return f"{emoji*3}\n {name} - {profession}\n {passion} \n {website} \n {emoji*3}"

bio = generate_bio(style)

print("\nYour stylish bio: \n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)

save = input("Do you want to save this bio to a text file? (y/n): ").lower()

if save == "y":
	filename = f"{name.lower().replace(" ", "_")}_bio.txt"
	with open(filename, "w", encoding = "utf-8") as f:
		f.write(bio)
	print("file saved")

