import argparse
from itertools import chain
from collections import deque
import apt

def main(args):
    packages_seen = set()
    dependencies = deque()

    def print_package(package):
        print(package.name, package.installed)
        packages_seen.add(package.name)

        or_dependencies = [dependency.or_dependencies
                           for dependency in package.installed.dependencies]
        dependencies.extend(chain.from_iterable(or_dependencies))

    cache = apt.cache.Cache()
    package = cache[args.package_name]
    print_package(package)

    while dependencies:
        dependency = dependencies.popleft()
        package_name = dependency.name

        # Skip virtual packages                                                                                                          
        if package_name not in cache:
            continue

        if package_name not in packages_seen:
            package = cache[dependency.name]
            print_package(package)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Print all package dependencies '
                                     'and their installed version')
    parser.add_argument('package_name', help='Package name')
    args = parser.parse_args()

    main(args)
