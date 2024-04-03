# def greet(name):
#     result = ["안녕", "하세요, " ,name, ", 오늘도 화이팅!"]
#     return " ".join(result)
# print(greet("요한"))

# def greet_with(name, location):
#   print(f'Hellow {name}')
#   print(f'What is it like in {location}?')

# greet_with(location = 'London', name = '요한')

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = list(input("Type your message:\n").lower())
  shift = int(input("Type the shift number:\n")) % 26

  def caesar(direction, text, shift):
    c_list = []
    if direction == 'decode':
      shift *= -1
    for letter in text:
      if letter in alphabet:
        position = (alphabet.index(letter))
        new_position = position + shift
        c_list.append(alphabet[new_position])
      elif letter not in alphabet:
        c_list.append(letter)

    return ''.join(c_list)

  print(caesar(direction, text, shift))
  retry = input("\n 다시 프로그램을 실행하시려면 Y를 입력해주세요 : ")
  if retry == 'y':
    continue
  else:
    break

print("\n\n카이사르 암호 생성기를 이용해주셔서 감사합니다!")
