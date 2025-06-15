from django.db.models import Q, Count, Case, When, Value, BooleanField, F

from articles.models import Article
from users.models import User

user_cheolsu = User.objects.get(username='김철수')
user_younghee = User.objects.get(username='박영희')

article_django_basic = Article.objects.get(title='Django 기본')


# OR 조건 - 제목에 'Django'가 포함되거나, 내용에 '파이썬'이 포함된 게시물
article_or = Article.objects.filter(Q(title__icontains='django') | Q(content__icontains='파이썬'))
print("기사에 Django라는 Title or content에 파이썬을 포함하는 기사들:")
for article in article_or:
    print(f" -> {article.title}")

print("기사에 '김철수'가 작가면서 Title에 '기본'이 포함되는 기사:")
article_or_2 = Article.objects.filter(Q(author=user_cheolsu) & Q(title__contains='기본'))
for article in article_or_2:
    print(f" -> {article.title}")

print("기사에 '김철수'가 작가면서 Title에 '기본'을 제외하는 기사: -> AND NOT")
article_or_2 = Article.objects.filter(Q(author=user_cheolsu) & ~Q(title__contains='기본'))
for article in article_or_2:
    print(f" -> {article.title}")


# parent_comment = Comment.objects.create(content_object=article_django_basic, user=user_younghee, content='좋은글 잘봤습니다.')
# print(f" -> {user_younghee.username}님이 {article_django_basic.title}에 댓글을 작성했습니다.")
# reply_comment = Comment.objects.create(content_object=parent_comment, user=user_cheolsu, content='저도 동감합니다.')
# reply_comment_2 = Comment.objects.create(content_object=parent_comment, user=user_younghee, content='맞아요.')
# print(f" -> {user_younghee.username}님이 대댓글을 달았습니다.")
#
# Like.objects.create(user=user_younghee, content_object=article_django_basic)
# Like.objects.create(user=user_younghee, content_object=parent_comment)

article = Article.objects.annotate(comment_count=Count('comments'))
for article in article:
    print(f" -> {article.title}의 댓글 수: {article.comment_count}")

print("Case/When을 활용한 조건문 필드 추가")
django_articles = Article.objects.annotate(
    is_django_related=Case( # 1. 주석을 추가 + Case 경우에 따라서 다른 값을 주겠다.
        When(
            Q(title__icontains='django') | Q(title__icontains='orm'),
            then=Value(True)
        ), # 만약 이 조건이면 -> True
        default=Value(False),
        output_field=BooleanField()
    )
)

for article in django_articles:
    print(f" -> {article.title}, 장고관련 : {article.is_django_related}")

print("Case/When을 활용한 조건문 필드 추가 2차 가공 'TRUE'")
is_django_related_true = django_articles.filter(is_django_related=True)
for article in is_django_related_true:
    print(f" -> {article.title}, 장고관련 ✅: {article.is_django_related}")

print("Case/When을 활용한 조건문 필드 추가 2차 가공 'FALSE'")
is_django_related_false = django_articles.filter(is_django_related=False)
for article in is_django_related_false:
    print(f" -> {article.title}, 장고관련 ❌: {article.is_django_related}")


article = Article.objects.first()
print(f"실습 대상 게시글: {article.title}, 게시글의 조회수: {article.views}")

article.views = F('views') + 1
article.save()
article.refresh_from_db()
print(article.views)
