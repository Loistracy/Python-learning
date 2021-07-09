
message = input(">")
words = message.split(' ')
emojis = {
    "Happy" : "😃",
    "sad" : "😞",
    "love" : "👩‍❤️‍👨",
    "hate" : "💔"
}
output = ""
for word in words:
 output += emojis.get(word , word) + ""
print(output)