from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import \
    ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Analyze
from .forms import AnalyzeForm

APPNAME = 'analyze'

class AnalyzeListView(ListView):
    """
    メモを一覧表示
    テンプレートは、何も指定しないと モデル名_list.html が使われる
    ListView は、パジネーションもやってくれる
    """
    model = Analyze
    paginate_by = 10  # 1ページに表示する件数


class AnalyzeDetailView(DetailView):
    """
    1つのメモを詳細表示
    テンプレートは、何も指定しないと モデル名_detail.html が使われる
    """
    model = Analyze


class AnalyzeCreateView(CreateView):
    """
    メモ 新規作成
    完了ページを作成し、success_url で指定して表示してもいいが、
    django.contrib.messages の機能で、メッセージを保存して
    リストビューなんかに戻した時に表示するのも簡潔で良い。
    """
    model = Analyze
    form_class = AnalyzeForm
    success_url = reverse_lazy('analyze_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を作成しました'.format(form.instance))
        return result


class AnalyzeUpdateView(UpdateView):
    """
    メモ 更新
    """
    model = Analyze
    form_class = AnalyzeForm

    success_url = reverse_lazy('analyze_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を更新しました'.format(form.instance))
        return result


class AnalyzeDeleteView(DeleteView):
    """
    メモ 削除
    デフォルトでは、get でリクエストすると確認ページ、
    post でリクエストすると削除を実行する、という動作。
    実際は、レコードを削除するのではなく有効フラグを消す(いわゆる論理削除)
    のケースが多いと思うので、そんな時はdeleteをオーバーライドしてその中で処理を書く。
    """
    model = Analyze
    form_class = AnalyzeForm

    success_url = reverse_lazy('analyze_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object))
        return result