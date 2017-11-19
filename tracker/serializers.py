from tracker.models import Countdown, Tomato
from django.contrib.auth.models import User
from rest_framework import serializers


class CountdownSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Countdown
        fields = ('url', 'id', 'title', 'due', 'user',)


class TomatoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Tomato
        fields = ('url', 'id', 'task', 'duration', 'completed', 'user')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    countdown = serializers.HyperlinkedRelatedField(many=True, view_name='countdown-detail', read_only=True)
    tomato = serializers.HyperlinkedRelatedField(many=True, view_name='tomato-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'countdown', 'tomato',)
