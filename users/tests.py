from datetime import datetime

from articles.models import Article
from users.models import User

user1 = User.objects.create(username='김철수', user_id='chulsoo')
user2 = User.objects.create(username='박영희', user_id='younghee')
user3 = User.objects.create(username='이민준', user_id='minjoon')
user4 = User.objects.create(username='김민준', user_id='kim_minjoon')

# user1의 가입 날짜를 과거로 수정
user1.date_joined = datetime(2024, 1, 15)
user1.save()

# 게시글 데이터 생성
Article.objects.create(author=user1, title='Django 기본', content='Django는 파이썬 기반의 웹 프레임워크입니다.')
Article.objects.create(author=user1, title='Django ORM', content='ORM을 사용하면 SQL 없이 데이터베이스를 조작할 수 있습니다.')
Article.objects.create(author=user2, title='Python 기초', content='파이썬은 배우기 쉬운 프로그래밍 언어입니다.')
Article.objects.create(author=user3, title='웹 개발 이야기', content='프론트엔드와 백엔드에 대한 이야기.')
Article.objects.create(author=user4, title='알고리즘 문제 풀이', content='코딩 테스트를 위한 알고리즘 공부법.')
print("--- 초기 데이터 설정 완료 ---\n")


def practice_queryset():
    """
    QuerySet 조회 및 필터링 실습 함수

    필드명__조회조건=값

    * 마치 SQL의 WHERE 절에 다양한 연산자(LIKE, >, <, IN 등)를 사용하는 것과 같다고 생각하시면 이해가 쉬울 거예요!

    1. exact	정확히 일치하는 값을 찾습니다. (기본값이므로 생략 가능)	Article.objects.filter(title__exact='Django 기본')
    2. iexact	대소문자를 구분하지 않고 정확히 일치하는 값을 찾습니다.	Article.objects.filter(title__iexact='django 기본')
    3. contains	특정 문자열을 포함하는 값을 찾습니다. (대소문자 구분)	Article.objects.filter(title__contains='Django')
    4. icontains	대소문자를 구분하지 않고 특정 문자열을 포함하는 값을 찾습니다.	Article.objects.filter(title__icontains='django')
    5. startswith	특정 문자열로 시작하는 값을 찾습니다.	Article.objects.filter(title__startswith='Django')
    6. istartswith	대소문자 구분 없이 특정 문자열로 시작하는 값을 찾습니다.	Article.objects.filter(title__istartswith='django')
    7. endswith	특정 문자열로 끝나는 값을 찾습니다.	Article.objects.filter(content__endswith='.')
    8. iendswith	대소문자 구분 없이 특정 문자열로 끝나는 값을 찾습니다.	Article.objects.filter(content__iendswith='.')
    9. in	리스트나 튜플, 쿼리셋 등 목록에 포함된 값 중 하나라도 일치하면 찾습니다.	User.objects.filter(username__in=['김철수', '박영희'])
    10. gt	(greater than) 특정 값보다 큰 값을 찾습니다. (초과)	Article.objects.filter(id__gt=10)
    11. gte	(greater than or equal to) 특정 값보다 크거나 같은 값을 찾습니다. (이상)	Article.objects.filter(id__gte=10)
    12. lt	(less than) 특정 값보다 작은 값을 찾습니다. (미만)	Article.objects.filter(date_joined__lt=date(2025,1,1))
    13. lte	(less than or equal to) 특정 값보다 작거나 같은 값을 찾습니다. (이하)	Article.objects.filter(date_joined__lte=date(2025,1,1))
    14 .isnull	값이 NULL인지 아닌지를 확인합니다. (True 또는 False)	User.objects.filter(user_id__isnull=True)

    """
    print("### QuerySet 실습 시작 ###\n")

    # 1. filter: 조건에 맞는 데이터 모두 가져오기
    print("1. 이름이 '김민준'인 사용자 찾기 (filter)")
    kim_users = User.objects.filter(username='김민준')
    for user in kim_users:
        print(f" -> 사용자: {user.username}, ID: {user.user_id}")
    print("-" * 20)

    # 2. exclude: 특정 조건을 제외한 데이터 가져오기
    print("2. '김민준'이 아닌 사용자들 찾기 (exclude)")
    other_users = User.objects.exclude(username='김민준')
    for user in other_users:
        print(f" -> 사용자: {user.username}")
    print("-" * 20)

    # 3. Field Lookups: __contains, __startswith
    print("3. 이름에 '민준'이 포함된 사용자 찾기 (username__contains)")
    minjoon_users = User.objects.filter(username__contains='민준')
    print(f" -> '민준' 포함 사용자 수: {minjoon_users.count()}")
    for user in minjoon_users:
        print(f"   - {user.username}")
    print("-" * 20)

    # 4. Field Lookups: __gt, __lte
    print("4. 2025년 1월 1일 이전에 가입한 사용자 찾기 (date_joined__lt)")
    early_users = User.objects.filter(date_joined__lt=datetime(2025, 1, 1))
    for user in early_users:
        print(f" -> 사용자: {user.username}, 가입일: {user.date_joined.strftime('%Y-%m-%d')}")
    print("-" * 20)

    # 5. Chaining: 여러 조건 연결하기
    print("5. '김철수'가 작성한 글 중 제목에 'ORM'이 포함된 글 찾기 (Chaining)")
    chulsoo = User.objects.get(username='김철수')
    orm_articles = Article.objects.filter(author=chulsoo).filter(title__contains='ORM')
    for article in orm_articles:
        print(f" -> 제목: {article.title}")
    print("-" * 20)

    # 6. order_by: 결과 정렬하기
    print("6. 모든 게시글을 최신순으로 정렬하기 (order_by)")
    # Article 모델은 TimeStampedModel을 상속받아 'created' 필드가 있습니다.
    latest_articles = Article.objects.order_by('-created')
    for article in latest_articles:
        print(f" -> [{article.created.strftime('%Y-%m-%d')}] {article.title}")
    print("-" * 20)

    # 7. Slicing: 결과 제한하기
    print("7. 가장 최근에 작성된 게시글 2개만 가져오기 (Slicing)")
    two_latest_articles = Article.objects.order_by('-created')[:2]
    for article in two_latest_articles:
        print(f" -> {article.title}")
    print("-" * 20)

    # 8. Field Lookup: __in
    print("8. '김철수'와 '이민준'이 작성한 모든 글 찾기 (__in)")
    authors_to_find = User.objects.filter(username__in=['김철수', '이민준'])
    articles_by_them = Article.objects.filter(author__in=authors_to_find)
    print(f" -> 찾은 게시글 수: {articles_by_them.count()}")
    for article in articles_by_them:
        print(f" -> 작성자: {article.author.username}, 제목: {article.title}")
    print("\n### QuerySet 실습 종료 ###")