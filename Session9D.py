name = "Amit Kumar"
print("ਤੁਹਾਡਾ ਨਾਮ ਇਹ ਹੈ:", name)
upper_case = name.upper()
print(upper_case)

Author_name = "messi"
cap_Author_name = Author_name.capitalize()
print("Author_name is:", Author_name)
print("Capitalize is:", cap_Author_name)
upper_case = Author_name.upper()
print(upper_case)

name = "amit, toypom, divjot, rohan"
print(name[0])
print(name, [len(name)-1])

idx = name.index('o')
print("index of 'o' is:", idx)

idx = name.index('divjot')
print("index of divjot is:", idx)

splitted_names = name.split(",")
print("splitted names are:", splitted_names)

for name in splitted_names:
    print(name.split())
print()

replaced_names = name.replace('r', 'd')
print(name)
print("replaced_names", len(replaced_names), replaced_names)

r_char_count = name.count('r', 0, len(name))
print("r occurs {} times".format(r_char_count))

essay = """An essay is, generally, a piece of writing that gives the author's own argument, but the definition is vague, overlapping with those of a letter, a paper, an article, a pamphlet, and a short story. Essays have traditionally been sub-classified as formal and informal."""

word = essay.split(" ")
print(word)
print(len(word))

number = "100"
print(number, type(number))

print(number.isdigit())
if number.isdigit():
    n = int(number)
    print("n is:", n)

files = ["song1.mp3", "song2.mp3", "image1.jpeg", "image2.png", "video1.mp4"]

print("Files which can be played in media")

for file in files:
    if file.endswith(".mp3") or file.endswith(".mp4"):
        print(file)

gmails = [
         "amitbanga17@gmail.com",
         "guri136@gmail.com",
         "rohanch@gmail.com",
         "harjor@gmail.com",
         "goru1235@gmail.com",
         "aniket176@gmail.com"
]

search_keyword = "g"
print("filtered gmail begins with", search_keyword)
for gmail in gmails:
    if gmail.startswith("g"):
        print(gmail)

print(end="=============================== \n")
for gmail in gmails:
    if search_keyword in gmail:
        print(gmail)
