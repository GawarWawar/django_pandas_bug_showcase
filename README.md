# django_pandas_bug_showcase
CHECKED ON 18 OF SEPTEMBER 2024, BUG WAS FIXED

This is a small showcase of the bug within Django and Pandas interaction.
When using Pandas within Django and causing KeyError, server goes into shutdown without any error message or console message, and then it needs to be rebooted with runserver command again.
Tried using Gunicorn to boot up WSGI instance. When trying to recreate bug and access the key that doesnt exist, Gunicorn returns: "Worker (pid:81310) was sent SIGSEGV!"
  
I created several views to showcase this bug:

This views will show basic bihavior without any bugs:
- view without any DataFrame generation just with KeyError raise: /views/test_simple_raise_KeyError
- basic DataFrame generation, without any errors presented in json format: /views/test_show_dataframe
- test with DataFrame generation and KeyError catch with try-exept structure: /views/test_catch_KeyError_with_using_pandas
  
This views will cause bug to shutdown server:
- bug recreation with DataFrame generation without any KeyError catch: /views/recreate_bug
- bug recreation with DataFrame generation without any KeyError catch, without using .loc attribute of pd.DataFrame: /views/recreate_bug
- bug recreation with DataFrame generation and KeyError catch with try-exept structure, however we raise KeyError after catching it: /views/recreate_bug_with_raise_error_after_catching_KeyError
