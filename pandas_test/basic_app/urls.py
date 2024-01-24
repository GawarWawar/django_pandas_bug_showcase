from django.urls import path
from . import views

urlpatterns = [
    path('test_show_dataframe', views.test_show_dataframe, name="test_show_dataframe"),
    path('test_simple_raise_KeyError', views.test_simple_raise_KeyError, name="test_simple_raise_KeyError"),
    path('test_catch_KeyError_with_using_pandas', views.test_catch_KeyError_with_using_pandas, name="test_catch_KeyError_with_using_pandas"),
    path('recreate_bug_with_raise_error_after_catching_KeyError', views.recreate_bug_with_raise_error_after_catching_KeyError, name="recreate_bug_with_raise_error_after_catching_KeyError"),
    path('recreate_bug', views.recreate_bug, name="recreate_bug"),
    path('recreate_bug_without_loc', views.recreate_bug_without_loc, name="recreate_bug_without_loc"),
]
