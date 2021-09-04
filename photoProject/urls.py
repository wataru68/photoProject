from django.contrib import admin
from django.urls import path, include  # includeを追加
# auth.viewsをインポートしてauth_viewという記名で利用する
from django.contrib.auth import views as auth_views
from django.conf import settings  # settingsを追加
from django.conf.urls.static import static  # staticを追加

# URLパターンを登録するための変数
urlpatterns = [
    # リクエストされたURLのページへのフルパス部分がadmin/にマッチングした場合
    # admin.site.urlsを呼び出し、Django管理サイトを表示する
    path('admin/', admin.site.urls),

    # photoアプリのURLconf(photo.urls)を呼び出すURLパターン
    path('', include('photo.urls')),

    # accounts.urlsへのURLパターンを追加
    path('', include('accounts.urls')),

    # パスワードリセットのためのURLパターン
    # PasswordResetConfirmViewがプロジェクトのurls.pyを参照するのでここに記載
    # パスワードリセット申し込みページ
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name="password_reset.html"),
         name="password_reset"),

    # メール送信完了ページ
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="password_reset_sent.html"),
         name='password_reset_done'),

    # パスワードリセット完了ページ
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="password_reset_done.html"),
         name='password_reset_complete'),

]

# urlpatternsにmediaフォルダーのURLパターンを追加
urlpatterns += static(
    settings.MEDIA_URL,  # MEDIA_URL='/media/'
    document_root=settings.MEDIA_ROOT  # MEDIA_ROOTにリダイレクト
)
