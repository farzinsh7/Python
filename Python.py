# data = "hello there my name is farzin shams you can send me a message if you want here is my email:me@farzinshams.com now guess my website?"
# find_email = data.find("@")
# print(find_email)
# find_space = data.find(" ", find_email)
# print(find_space)
# website = f"You website is: www.{data[find_email+1: find_space]}"
# print(website)
# for letter in 'banana':
#     print(letter)
# text = "X-DSPAM-Confidence:    0.8475"
# find_0 = text.find("0")
# find_num = text[find_0:]
# fnum = float(find_num)
# print(fnum)
# fname = input("Enter you file name: ")
# try:
#     rfile = open(fname)
# except:
#     print("We cant fine your file", fname)
#     quit()

# count = 0
# for line in rfile:
#     if line.startswith("_ "):
#         count += 1
# print(f"There are {count} _ in your file")

fname = input("Enter file name: ")
try:
    fhandle = open(fname)
    rfile = fhandle.read()
    rfile.rstrip()
except:
    print("Your file not defined!!!")
    quit()
print(rfile.upper())
