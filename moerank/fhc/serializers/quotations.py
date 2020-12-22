from rest_framework import serializers
from moerank.fhc.models import Quotations, QuotationsVote
import base64

class QuotationsSerializer(serializers.ModelSerializer):
    '''
    语录序列化
    '''

    class Meta:
        model = Quotations
        fields = '__all__'


class QuotationsListSerializer(serializers.ModelSerializer):
    '''
    语录序列化 for request mthod is get
    '''
    content = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    vote_count = serializers.SerializerMethodField()

    class Meta:
        model = Quotations
        fields = '__all__'

    def get_content(self, obj):
        return base64.b64decode(obj.content[2:-1])

    def get_author(self, obj):
        return base64.b64decode(obj.author[2:-1])
    
    def get_vote_count(self, obj):
        return QuotationsVote.objects.filter(quotation=obj.id).count()


class QuotationsVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationsVote
        fields = '__all__'