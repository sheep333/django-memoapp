from django import forms

from .models import Analyze,MemoAnalyze,QuestionAnalyze,FreeAnalyze


class AnalyzeForm(forms.ModelForm):
    """
    Analyze モデルの作成、更新に使われる Django フォーム。
    ModelForm を継承して作れば、HTMLで表示したいフィールドを
    指定するだけで HTML フォームを作ってくれる。
    """

    class Meta:
        model = Analyze
        fields = ['type_id']
    
    analyze_templates = (
        ('', '選択肢から選んでください><'),
        #継承先
        ('0', 'メモ型テンプレート'),
        ('1', '質問型テンプレート'),
        ('2', '自由型テンプレート'),
    )

    type = forms.ChoiceField(choices=,)

class MemoAnalyzeForm(forms.ModelForm):
    """
    Analyze モデルの作成、更新に使われる Django フォーム。
    ModelForm を継承して作れば、HTMLで表示したいフィールドを
    指定するだけで HTML フォームを作ってくれる。
    """

    class Meta:
        model = MemoAnalyze
        fields = ['subject', 'body']


class QuestionAnalyzeForm(forms.ModelForm):
    """
    Analyze モデルの作成、更新に使われる Django フォーム。
    ModelForm を継承して作れば、HTMLで表示したいフィールドを
    指定するだけで HTML フォームを作ってくれる。
    """

    class Meta:
        model = QuestionAnalyze
        fields = ['question', 'answer']


class FreeAnalyzeForm(forms.ModelForm):
    """
    Analyze モデルの作成、更新に使われる Django フォーム。
    ModelForm を継承して作れば、HTMLで表示したいフィールドを
    指定するだけで HTML フォームを作ってくれる。
    """

    class Meta:
        model = FreeAnalyze
        fields = ['content']
