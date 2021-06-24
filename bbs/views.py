from django.shortcuts import render
from django.http import HttpResponse  # <- この行を追加
from bbs.models import Post  # modelsからPostモデルをインポート
from bbs.forms import PostForm  # <- これを追加
from django.shortcuts import render, redirect
def home(request):

    return HttpResponse('HOME')  # テスト。レスポンスを返す

def home_view(request):
    """
    パス bbs/ のテンプレートを出力するビュー
    """

    # request.methodによって処理を分岐
    if request.method == 'GET':
        return home_view_get(request)
    elif request.method == 'POST':
        return home_view_post(request)
    else:
        return HttpResponse('invalid method', status=400)


def home_view_get(request, form=None):
    """
    パス bbs/ の GET
    """
    context = {}  # コンテキストを作成

    context['title'] = '一行掲示板'  # ページのタイトル
    context['posts'] = Post.objects.all()  # Postのリストを取得

    #ここが謎
    if form:#formにデータがあれば
        context['form'] = form
    else:
        context['form'] = PostForm()  # フォームを保存

    # renderにコンテキストを渡しテンプレートを描画
    return render(request, 'bbs/home.html', context)


def home_view_post(request):
    """
    パス bbs/ の POST
    """
    form = PostForm(request.POST)
    if not form.is_valid():
        return home_view_get(request, form=form)

    form.save()
    return redirect('bbs_home')