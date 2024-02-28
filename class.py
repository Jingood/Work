import hashlib

dig = []


class Member:
    members = []

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        Member.members.append(self)
        ho = hashlib.sha256(password.encode())
        hex_dig = ho.hexdigest()
        dig.append(hex_dig)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Username: {self.username}")

    def find_member_by_username(cls, username):
        for member in cls:
            if member.username == username:
                return member
        return None

    def __str__(self):
        return f"name: {self.name}, username: {self.username}"


def new():
    name = input("이름을 입력해주세요: ")
    username = input("닉네임을 입력해주세요: ")
    password = input("비밀번호를 입력해주세요: ")
    member = Member(name, username, password)
    return member


class Post:
    posts = []

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        Post.posts.append(self)

    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}, Author: {self.author}"


def p_new():
    title = input("제목을 입력해주세요: ")
    content = input("내용을 입력해주세요: ")
    author = input("닉네임을 입력해주세요: ")
    author_member = Member.find_member_by_username(Member.members, author)
    if author_member:
        post = Post(title, content, author)
        return post
    else:
        print("해당 닉네임을 가진 사용자를 찾을 수 없습니다.")
        return None


member1 = Member('sing', 'sang', 'song')
member2 = Member('read', 'lead', 'rid')
member3 = Member('coffee', 'copy', 'kopy')

post1 = Post('Bingo', 'turtle', member1.username)
post2 = Post('Arirang', 'SGwanabee', member1.username)
post3 = Post('Timeless', 'SGwanabee', member1.username)
post4 = Post('gun,germs,and steel', 'Jared Diamond', member2.username)
post5 = Post('Harry Potter And The Chamber of Secrets ',
             'J.K.Rowling', member2.username)
post6 = Post('Harry Potter And The Goblet of Fire',
             'J.K.Rowling', member2.username)
post7 = Post('americano', 'starbucks', member3.username)
post8 = Post('coldbrew', 'starbucks', member3.username)
post9 = Post('wonjocoffee', 'Backdabang', member3.username)

new_member = new()

new_post = p_new()

for member in Member.members:
    print(member)


for post in Post.posts:
    print(post)

for post in Post.posts:
    author_name = 'lead'
    if post.author == author_name:
        print(f'{post.title} by {author_name}')

for post in Post.posts:
    if 'SG' in post.content:
        print(post.title)

for hash in dig:
    print(hash)

Member.display(member1)
