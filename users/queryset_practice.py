"""

1. exact - 정확하게 일치하는 값을 찾는다 -> User.obejct.filter(username__exact='홍길동')
2. iexact - 대소를 구분하지고 일치하는 값을 찾는다. -> Acticle.obejct.filter(title__iexact='재밌게 배우는 django')
3. contains - 특정 문자열을 포함하는 값을 찾는다.(대소구별) -> Acticle.obejct.filter(title__contains='django')
4. icontains - 특정 문자열을 포함하는 값을 찾는다.(대소구별안함) -> Acticle.obejct.filter(title__icontains='django')
5. startswith - 특정 문자열로 시작하는 값을 찾는다.(대소구별) -> Acticle.obejct.filter(title__startswith='django')
6. istartswith - 특정 문자열로 시작하는 값을 찾는다.(대소구별안함) -> Acticle.obejct.filter(title__istartswith='django')
7. endwith - 생략
8. iendwith - 생략
9. in - 값 중 하나라도 일치하면 찾는다. -> User.objects.filter(username__in=['홍길동', '김철수'])
10. gt - 초과 -> Article.objects.filter(views__gt=100)
11. gte - 이상 -> Article.objects.filter(views__gte=100)
12. lt - 미만 -> Article.objects.filter(views__lt=100)
13. lte - 이하 -> Article.objects.filter(views__lte=100)
14. isnull - 값이 Null인지 아닌지 확인. -> True, False -> User.objects.filter(user_id__isnull=True)

"""
from datetime import datetime

from articles.models import Article
from users.models import User

# user1 = User.objects.create(username='김철수', user_id='chulsoo')
# user2 = User.objects.create(username='박영희', user_id='younghee')
# user3 = User.objects.create(username='이민준', user_id='minjoon')
# user4 = User.objects.create(username='김민준', user_id='kim_minjoon')
#
# Article.objects.create(author=user1, title='Django 기본', content='Django는 파이썬 기반의 웹 프레임워크입니다.')
# Article.objects.create(author=user1, title='Django ORM', content='ORM을 사용하면 SQL 없이 데이터베이스를 조작할 수 있습니다.')
# Article.objects.create(author=user2, title='Python 기초', content='파이썬은 배우기 쉬운 프로그래밍 언어입니다.')
# Article.objects.create(author=user3, title='웹 개발 이야기', content='프론트엔드와 백엔드에 대한 이야기.')

# 1. filter
users = User.objects.filter(username='김민준')
for user in users:
    print(f" -> 사용자: {user.username}, ID: {user.user_id}")
print("-" * 20)

# 2. exclude
print("김민준이 아닌 사용자들 찾기")
users = User.objects.exclude(username='김민준')
for user in users:
    print(f" -> 사용자: {user.username}, ID: {user.user_id}")
print("-" * 20)

# 3. lookups:  __contains, __startswith
print("민준이 포함된 사용자 찾기")
users = User.objects.filter(username__contains='민준')
for user in users:
    print(f" -> 사용자: {user.username}, ID: {user.user_id}")
print("-" * 20)


print("Django로 시작하는 Article 검색")
articles = Article.objects.filter(title__startswith='Django')
for article in articles:
    print(f" -> 게시글: {article.title}, ID: {article.id}")
print("-" * 20)

print("4. 2025년 2월 2일 이전에 가입한 사용자 찾기")
users = User.objects.filter(date_joined__lt=datetime(2025, 2, 2))
for user in users:
    print(f" -> 사용자: {user.username}, ID: {user.user_id}")
print("-" * 20)

print("5. Chaining 여러조건 - 김철수가 작성한 글 중에서 title에 ORM이 포함되는 글 찾기")
user = User.objects.get(username='김철수')
articles = Article.objects.filter(author=user).filter(title__contains='ORM')
for article in articles:
    print(f" -> 게시글: {article.title}, ID: {article.id}")
print("-" * 20)

print("6. 김철수, 박영희 가 작성한 모든 글을 찾기")
users = User.objects.filter(username__in=['김철수', '박영희'])
articles = Article.objects.filter(author__in=users)
for article in articles:
    print(f" -> Author: {article.author.username}, 게시글: {article.title}, ID: {article.id}")
print("-" * 20)

