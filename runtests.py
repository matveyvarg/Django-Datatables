import os
import sys

import pytest
from django.test.runner import DiscoverRunner

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')
    print(os.getenv('DJANGO_SETTINGS_MODULE'))
    import django
    django.setup()
    test_runner = DiscoverRunner(verbosity=1)
    failures = test_runner.run_tests(['tests'])
    if failures:
        sys.exit(failures)

    # return pytest.main()


if __name__ == '__main__':
    sys.exit(main())