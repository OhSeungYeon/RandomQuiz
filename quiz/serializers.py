from rest_framework import serializers
from .models import Quiz

#시리얼라이저는 장고 모델 데이터를 JSON타입으로 바꿔주는 직렬화 코드이다.
#JSON 타입으로 뿌려주면 api 통신이 되는 것이며 내 데이터를 JSON으로 바꿔주는 기계라고 생각하면 된다.
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')