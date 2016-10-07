Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> run_test()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    run_test()
NameError: name 'run_test' is not defined
>>> ================================ RESTART ================================
>>> 
>>> run_test()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    run_test()
NameError: name 'run_test' is not defined
>>> ================================ RESTART ================================
>>> 
>>> run_tests
<function run_tests at 0x02261A50>
#
>>> run_tests()
Trying:
    hit_100(72)
Expecting:
    Too low
ok
Trying:
    hit_100(135)
Expecting:
    Too high
ok
Trying:
    hit_100(100)
Expecting:
    Winner!
ok
2 items had no tests:
    __main__.hit_100
    __main__.run_tests
1 items passed all tests:
   3 tests in __main__
3 tests in 3 items.
3 passed and 0 failed.
Test passed.
>>> 
